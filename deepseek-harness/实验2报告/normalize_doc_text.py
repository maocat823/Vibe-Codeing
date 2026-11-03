# -*- coding: utf-8 -*-
import io, sys

def normalize(src, dst):
    raw = io.open(src, 'r', encoding='utf-8').read()
    out = []
    for ch in raw:
        o = ord(ch)
        if ch == '\r':
            out.append('\n')
        elif ch == '\x07':   # cell/row end
            out.append('\n')
        elif ch == '\x0b':   # line break
            out.append('\n')
        elif ch == '\x0c':   # page break
            out.append('\n\n=====[page]=====\n\n')
        elif ch == '\x1e':   # non-breaking hyphen-ish
            out.append('-')
        elif o < 32 and ch not in ('\n', '\t'):
            out.append('')
        else:
            out.append(ch)
    txt = ''.join(out)
    # collapse 3+ newlines
    while '\n\n\n' in txt:
        txt = txt.replace('\n\n\n', '\n\n')
    io.open(dst, 'w', encoding='utf-8').write(txt)
    print('wrote', dst, 'len', len(txt))

normalize(r"D:\Vibe-Codeing\deepseek-harness\xuqian_text.txt", r"D:\Vibe-Codeing\deepseek-harness\xuqian_norm.txt")
normalize(r"D:\Vibe-Codeing\deepseek-harness\guide_text.txt", r"D:\Vibe-Codeing\deepseek-harness\guide_norm.txt")
