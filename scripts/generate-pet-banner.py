"""Build the README GIF from the official eight-pet CDN catalog.

Requires Python 3, curl, and ImageMagick. Pass --assets-dir to reuse downloads.
"""
import argparse
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CDN = "https://persistent.oaistatic.com/codex/pets/v1"
PETS = [("codex", "Codex"), ("dewey", "Dewey"), ("fireball", "Fireball"),
        ("rocky", "Rocky"), ("seedy", "Seedy"), ("stacky", "Stacky"),
        ("bsod", "BSOD"), ("null-signal", "Null Signal")]
# Idle frame durations from codex-rs/tui/src/pets/model.rs.
DURATIONS = [1680, 660, 660, 840, 840, 1920]

def run(*args):
    subprocess.run(args, check=True)

def idle_frame(time_ms):
    time_ms %= sum(DURATIONS)
    for index, duration in enumerate(DURATIONS):
        if time_ms < duration:
            return index
        time_ms -= duration
    raise AssertionError("Invalid animation time")

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--assets-dir", type=Path)
options = parser.parse_args()
with tempfile.TemporaryDirectory(prefix="codex-pet-banner-") as scratch:
    work = Path(scratch)
    assets = options.assets_dir or work
    assets.mkdir(parents=True, exist_ok=True)
    sprites = {}
    for pet, _ in PETS:
        sheet = assets / f"{pet}.webp"
        if not sheet.exists():
            run("curl", "-fsSL", "--max-time", "30", f"{CDN}/{pet}-spritesheet-v4.webp", "-o", str(sheet))
        dimensions = subprocess.check_output(["magick", "identify", "-format", "%wx%h", str(sheet)], text=True)
        if dimensions != "1536x1872":
            raise ValueError(f"Unexpected dimensions for {pet}: {dimensions}")
        for index in range(6):
            output = work / f"{pet}-{index}.png"
            run("magick", str(sheet), "-crop", f"192x208+{index * 192}+0", "+repage",
                "-filter", "Point", "-resize", "96x104", str(output))
            sprites[pet, index] = output
    # Text is painted separately; sprites retain their original pixel artwork.
    base = work / "base.png"
    command = ["magick", "-size", "960x224", "xc:#090f1a", "-fill", "#153044",
               "-draw", "rectangle 24,82 936,83", "-fill", "#62ead5",
               "-draw", "rectangle 24,26 27,62", "-font", "Helvetica",
               "-fill", "#edf6fc", "-pointsize", "25", "-annotate", "+42+49", "AWESOME CODEX CLI",
               "-fill", "#87a5bc", "-pointsize", "11", "-annotate", "+43+69", "A LITTLE COMPANY FOR YOUR NEXT BIG IDEA.",
               "-fill", "#62ead5", "-pointsize", "10", "-annotate", "+800+48", "/pets  •  ALL SYSTEMS GO"]
    for index, (_, name) in enumerate(PETS):
        command += ["-fill", "#9bb3c8", "-pointsize", "11", "-gravity", "North",
                    "-annotate", f"{index * 120 + 60 - 480:+d}+199", name]
    command += [str(base)]
    run(*command)
    frames = []
    for frame in range(60):
        path = work / f"frame-{frame:03}.png"
        command = ["magick", str(base), "-gravity", "NorthWest"]
        for index, (pet, _) in enumerate(PETS):
            sprite_index = idle_frame(frame * 110 + index * 660)
            command += [str(sprites[pet, sprite_index]), "-geometry", f"+{index * 120 + 12}+90", "-composite"]
        command += [str(path)]
        run(*command)
        frames.append(str(path))
    run("magick", "-delay", "11", *frames, "-loop", "0", "-layers", "Optimize",
        str(ROOT / "assets/codex-pet-banner.gif"))
    print("Created assets/codex-pet-banner.gif (60 frames, 6.6-second loop)")
