# Codex Pet banner

The banner uses the original eight built-in pet sprites from OpenAI's public
Codex Pet CDN: Codex, Dewey, Fireball, Rocky, Seedy, Stacky, BSOD, and Null Signal.
Character artwork belongs to OpenAI; this community repository is not affiliated
with or endorsed by OpenAI.

- Catalog: https://github.com/openai/codex/blob/main/codex-rs/tui/src/pets/catalog.rs
- CDN source: https://github.com/openai/codex/blob/main/codex-rs/tui/src/pets/asset_pack.rs
- Sprite URL pattern: `https://persistent.oaistatic.com/codex/pets/v1/<id>-spritesheet-v4.webp`
- Idle timing: six frames lasting 1680, 660, 660, 840, 840, and 1920 milliseconds.
- The terminal panel cycles through GPT-6.1 Sol, GPT-6 Astra, and GPT-6 Luna with a blinking cursor. Model names were checked against the official catalog on October 11, 2026.

Regenerate with Python 3, curl, and ImageMagick:

```sh
python3 scripts/generate-pet-banner.py
```

To reuse downloaded sprites, pass `--assets-dir /path/to/sprites`, containing
`codex.webp`, `dewey.webp`, and the other pet IDs. Only the final GIF is committed.
