# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1280, 340
img = Image.new("RGB", (W, H), "#071A12")
draw = ImageDraw.Draw(img)

# Dark green gradient background
for y in range(H):
    t = y / (H - 1)
    r = int(7 + (12 - 7) * t)
    g = int(26 + (42 - 26) * t)
    b = int(18 + (28 - 18) * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Subtle green grid
for x in range(0, W, 40):
    draw.line([(x, 0), (x, H)], fill=(20, 55, 38))
for y in range(0, H, 40):
    draw.line([(0, y), (W, y)], fill=(20, 55, 38))

# Emerald accent bars
green_a = (34, 197, 94)
green_b = (16, 185, 129)
for x in range(W):
    t = x / (W - 1)
    c = (
        int(green_a[0] * (1 - t) + green_b[0] * t),
        int(green_a[1] * (1 - t) + green_b[1] * t),
        int(green_a[2] * (1 - t) + green_b[2] * t),
    )
    draw.line([(x, 0), (x, 4)], fill=c)
    draw.line([(x, H - 5), (x, H - 1)], fill=c)

font_path = next(
    (
        p
        for p in [
            r"C:\Windows\Fonts\segoeuib.ttf",
            r"C:\Windows\Fonts\arialbd.ttf",
            r"C:\Windows\Fonts\calibrib.ttf",
        ]
        if os.path.exists(p)
    ),
    None,
)
regular_path = next(
    (
        p
        for p in [
            r"C:\Windows\Fonts\segoeui.ttf",
            r"C:\Windows\Fonts\arial.ttf",
            r"C:\Windows\Fonts\calibri.ttf",
        ]
        if os.path.exists(p)
    ),
    None,
)

name_font = ImageFont.truetype(font_path, 64) if font_path else ImageFont.load_default()
role_font = ImageFont.truetype(regular_path, 28) if regular_path else ImageFont.load_default()
sub_font = ImageFont.truetype(regular_path, 22) if regular_path else ImageFont.load_default()


def center_text(text, font, y, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (W - tw) // 2
    draw.text((x, y), text, font=font, fill=fill)


center_text("Muhammad Ammar Shaikh", name_font, 100, (240, 253, 244))
center_text("AI / ML Engineer  |  Full-Stack Developer", role_font, 185, (74, 222, 128))
center_text("Building production AI systems", sub_font, 230, (167, 199, 178))

out = os.path.join(os.path.dirname(__file__), "..", "assets", "profile-header.png")
out = os.path.abspath(out)
os.makedirs(os.path.dirname(out), exist_ok=True)
img.save(out, "PNG", optimize=True)
print("saved", out, os.path.getsize(out))
