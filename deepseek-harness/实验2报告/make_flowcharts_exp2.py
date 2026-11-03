# -*- coding: utf-8 -*-
"""生成实验二(顺序结构) 4 个任务的流程图 PNG。"""
import os
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = r"C:\Windows\Fonts\simhei.ttf"
OUT_DIR = r"D:\Vibe-Codeing\deepseek-harness\flowcharts2"
os.makedirs(OUT_DIR, exist_ok=True)


def F(size):
    return ImageFont.truetype(FONT_PATH, size)


class Flow:
    def __init__(self, width=900):
        self.w = width
        self.items = []  # (shape, text)

    def add(self, shape, text):
        self.items.append((shape, text))

    def render(self, name):
        pad_top, pad_bottom = 30, 30
        gap = 54          # arrow gap between shapes
        line_h = 40       # per text line
        # measure each box height
        heights = []
        for shape, text in self.items:
            lines = self._wrap(text, 30, 560)
            text_h = max(1, len(lines)) * line_h
            if shape in ("start", "end"):
                bh = max(72, text_h + 24)
            elif shape == "diamond":
                bh = max(110, text_h + 50)
            else:
                bh = max(80, text_h + 26)
            heights.append(bh)
        total_h = pad_top + sum(heights) + gap * (len(self.items) - 1) + pad_bottom
        img = Image.new("RGB", (self.w, total_h), "white")
        d = ImageDraw.Draw(img)
        cx = self.w // 2
        y = pad_top
        boxes = []
        for i, (shape, text) in enumerate(self.items):
            bh = heights[i]
            cy = y + bh // 2
            boxes.append((shape, text, y, bh))
            y += bh + gap
        # draw arrows first (behind)
        for i in range(len(boxes) - 1):
            shape, text, by, bh = boxes[i]
            nxt = boxes[i + 1]
            self._arrow(d, cx, by + bh, cx, nxt[2], arrow=True)
        # draw boxes
        for shape, text, by, bh in boxes:
            self._shape(d, cx, by, bh, shape, text)
        img.save(os.path.join(OUT_DIR, name))

    def _wrap(self, text, size, max_w):
        f = F(size)
        lines = []
        for para in text.split("\n"):
            cur = ""
            for ch in para:
                if self._tw(cur + ch, f) <= max_w:
                    cur += ch
                else:
                    lines.append(cur)
                    cur = ch
            lines.append(cur)
        return lines

    def _tw(self, s, f):
        return f.getlength(s)

    def _shape(self, d, cx, by, bh, shape, text):
        x0, x1 = cx - 240, cx + 240
        y0, y1 = by, by + bh
        if shape == "start" or shape == "end":
            d.ellipse([cx - 90, y0, cx + 90, y1], outline="black", width=2)
        elif shape == "diamond":
            d.polygon([(cx, y0), (x1, (y0 + y1) // 2), (cx, y1), (x0, (y0 + y1) // 2)], outline="black")
        elif shape == "io":  # parallelogram
            off = 34
            d.polygon([(x0 + off, y0), (x1, y0), (x1 - off, y1), (x0, y1)], outline="black")
        else:  # process
            d.rectangle([x0, y0, x1, y1], outline="black", width=2)
        lines = self._wrap(text, 30, 560 if shape != "diamond" else 380)
        f = F(30)
        th = len(lines) * 40
        ty = (y0 + y1) // 2 - th // 2 + 8
        for ln in lines:
            tw = self._tw(ln, f)
            d.text((cx - tw / 2, ty), ln, font=f, fill="black")
            ty += 40

    def _arrow(self, d, x1, y1, x2, y2, arrow=True):
        d.line([x1, y1, x2, y2], fill="black", width=2)
        if arrow:
            import math
            ang = math.atan2(y2 - y1, x2 - x1)
            al = 14
            d.line([x2, y2, x2 + al * math.cos(ang + math.radians(155)), y2 + al * math.sin(ang + math.radians(155))], fill="black", width=2)
            d.line([x2, y2, x2 + al * math.cos(ang - math.radians(155)), y2 + al * math.sin(ang - math.radians(155))], fill="black", width=2)


def build(name, items):
    f = Flow()
    for s, t in items:
        f.add(s, t)
    f.render(name)


# 1. 和差积商
build("fc2_1.png", [
    ("start", "开始"),
    ("io", "输入两个整数 a、b"),
    ("proc", "sum = a + b\ndiff = a - b\nprod = a * b\nquot = a / b"),
    ("io", "输出 和、差、积、商"),
    ("end", "结束"),
])

# 2. 圆面积
build("fc2_2.png", [
    ("start", "开始"),
    ("io", "输入半径 r"),
    ("proc", "area = PI * r * r"),
    ("io", "输出 area（保留2位小数）"),
    ("end", "结束"),
])

# 3. 3门课程成绩
build("fc2_3.png", [
    ("start", "开始"),
    ("io", "输入 s1、s2、s3"),
    ("proc", "total = s1 + s2 + s3\navg = total / 3.0"),
    ("proc", "求最大值 max、最小值 min"),
    ("io", "输出 total、avg、max、min"),
    ("end", "结束"),
])

# 4. 进制转换
build("fc2_4.png", [
    ("start", "开始"),
    ("io", "输入十进制整数 n"),
    ("io", "输出 n 的十进制、八进制、十六进制"),
    ("end", "结束"),
])

print("flowcharts2 done")
