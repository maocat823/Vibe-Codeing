# -*- coding: utf-8 -*-
"""生成实验二程序的“运行结果”控制台截图 PNG（浅色主题，适合打印）。"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = r"D:\Vibe-Codeing\deepseek-harness\console2"
os.makedirs(OUT_DIR, exist_ok=True)

BODY_FONT = r"C:\Windows\Fonts\msyh.ttc"
TITLE_FONT = r"C:\Windows\Fonts\msyh.ttc"


def make(lines, title, name, width=880):
    body = ImageFont.truetype(BODY_FONT, 26)
    title_f = ImageFont.truetype(TITLE_FONT, 18)
    line_h = 42
    pad = 22
    title_h = 34
    # compute needed width for the longest line
    need = max(body.getlength(ln) for ln in lines) + pad * 2
    w = max(width, int(need) + 20)
    h = title_h + pad * 2 + line_h * len(lines)
    img = Image.new("RGB", (w, h), "white")
    d = ImageDraw.Draw(img)
    # window frame
    d.rectangle([0, 0, w - 1, h - 1], outline=(150, 150, 150), width=1)
    # title bar
    d.rectangle([0, 0, w - 1, title_h - 1], fill=(235, 235, 235), outline=(150, 150, 150))
    d.text((12, (title_h - 20) // 2), title, font=title_f, fill=(50, 50, 50))
    # body
    y = title_h + pad
    for ln in lines:
        d.text((pad, y), ln, font=body, fill=(25, 25, 25))
        y += line_h
    img.save(os.path.join(OUT_DIR, name))


make([
    "请输入两个整数：6 3",
    "和：9",
    "差：3",
    "积：18",
    "商：2.00",
], "命令提示符 - exp2_1.exe", "con2_1.png")

make([
    "请输入圆的半径：2.5",
    "圆的面积为：19.63",
], "命令提示符 - exp2_2.exe", "con2_2.png")

make([
    "请输入3门课程的成绩：80 90 100",
    "总分：270",
    "平均分：90.0",
    "最高分：100",
    "最低分：80",
], "命令提示符 - exp2_3.exe", "con2_3.png")

make([
    "请输入一个十进制整数：255",
    "十进制：255",
    "八进制：377",
    "十六进制：ff",
], "命令提示符 - exp2_4.exe", "con2_4.png")

print("console2 done")
