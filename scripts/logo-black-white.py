#!/usr/bin/env python3
"""
Convert legacy-logo.png to black background with white logo text.
Run from project root: python scripts/logo-black-white.py
Requires: pip install Pillow
"""

from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Install Pillow first: pip install Pillow")
    raise SystemExit(1)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOGO_PATH = PROJECT_ROOT / "public" / "legacy-logo.png"
BACKUP_PATH = PROJECT_ROOT / "public" / "legacy-logo-original.png"


def main():
    if not LOGO_PATH.exists():
        print(f"Logo not found: {LOGO_PATH}")
        raise SystemExit(1)

    img = Image.open(LOGO_PATH)
    img = img.convert("RGBA")
    w, h = img.size

    # Create new image: black background, white where logo was visible
    out = Image.new("RGBA", (w, h), (0, 0, 0, 255))
    pixels = img.load()
    out_pixels = out.load()

    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            # If pixel was visible (alpha above threshold), make it white
            if a > 30:
                out_pixels[x, y] = (255, 255, 255, 255)
            else:
                out_pixels[x, y] = (0, 0, 0, 255)

    # Backup original if we haven't already
    if not BACKUP_PATH.exists():
        img.save(BACKUP_PATH)
        print(f"Original saved to {BACKUP_PATH.name}")

    out.save(LOGO_PATH)
    print(f"Updated {LOGO_PATH} — black background, white logo")


if __name__ == "__main__":
    main()
