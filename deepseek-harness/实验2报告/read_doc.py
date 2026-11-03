# -*- coding: utf-8 -*-
"""Pure-python reader: OLE2 compound file -> WordDocument stream -> FIB/piece-table text."""
import struct, sys, io

class Ole:
    def __init__(self, data):
        self.data = data
        assert data[:8] == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1', 'not OLE2'
        self.ssz = 1 << struct.unpack('<H', data[30:32])[0]
        self.mssz = 1 << struct.unpack('<H', data[32:34])[0]
        self.num_fat = struct.unpack('<I', data[44:48])[0]
        self.first_dir = struct.unpack('<I', data[48:52])[0]
        self.cutoff = struct.unpack('<I', data[56:60])[0]
        self.first_minifat = struct.unpack('<I', data[60:64])[0]
        self.num_minifat = struct.unpack('<I', data[64:68])[0]
        self.first_difat = struct.unpack('<I', data[68:72])[0]
        self.num_difat = struct.unpack('<I', data[72:76])[0]

        difat = list(struct.unpack('<109I', data[76:512]))
        sec = self.first_difat
        for _ in range(self.num_difat):
            if sec >= 0xFFFFFFFA:
                break
            raw = self._sector(sec)
            vals = struct.unpack('<128I', raw[:512])
            difat.extend(vals[:127])
            sec = vals[127]

        self.fat = []
        for fs in difat[:self.num_fat]:
            if fs >= 0xFFFFFFFA:
                break
            raw = self._sector(fs)
            self.fat.extend(struct.unpack('<%dI' % (self.ssz // 4), raw))

        self.dirents = self._read_dir()

    def _sector(self, n):
        off = 512 + n * self.ssz
        return self.data[off:off + self.ssz]

    def _chain(self, start, fat):
        out, cur, visited = [], start, set()
        while cur < 0xFFFFFFFA and cur not in visited:
            visited.add(cur)
            out.append(cur)
            if cur >= len(fat):
                break
            cur = fat[cur]
        return out

    def _read_dir(self):
        chunks = [self._sector(s) for s in self._chain(self.first_dir, self.fat)]
        raw = b''.join(chunks)
        ents = []
        for i in range(len(raw) // 128):
            e = raw[i * 128:(i + 1) * 128]
            nlen = struct.unpack('<H', e[64:66])[0]
            name = e[:max(0, nlen - 2)].decode('utf-16le', errors='replace')
            typ = e[66]
            start = struct.unpack('<I', e[116:120])[0]
            size = struct.unpack('<Q', e[120:128])[0]
            ents.append({'name': name, 'type': typ, 'start': start, 'size': size})
        return ents

    def find(self, name):
        for e in self.dirents:
            if e['name'] == name:
                return e
        return None

    def stream(self, name):
        e = self.find(name)
        if e is None:
            return None
        chunks = [self._sector(s) for s in self._chain(e['start'], self.fat)]
        return b''.join(chunks)[:e['size']]


def extract_text(path):
    data = open(path, 'rb').read()
    ole = Ole(data)
    wd = ole.stream('WordDocument')
    if not wd:
        raise ValueError('no WordDocument stream')
    flags = struct.unpack('<H', wd[0x0A:0x0C])[0]
    tbl_name = '1Table' if (flags & 0x0200) else '0Table'
    table = ole.stream(tbl_name) or ole.stream('0Table') or ole.stream('1Table')
    fcClx = struct.unpack('<I', wd[0x01A2:0x01A6])[0]
    lcbClx = struct.unpack('<I', wd[0x01A6:0x01AA])[0]
    clx = table[fcClx:fcClx + lcbClx]
    plc, i = None, 0
    while i < len(clx):
        t = clx[i]
        if t == 0x01:
            cb = struct.unpack('<H', clx[i + 1:i + 3])[0]
            i += 3 + cb
        elif t == 0x02:
            lcb = struct.unpack('<I', clx[i + 1:i + 5])[0]
            plc = clx[i + 5:i + 5 + lcb]
            break
        else:
            break
    if plc is None:
        raise ValueError('no piece table')
    n = (len(plc) - 4) // 12
    cps = struct.unpack('<%dI' % (n + 1), plc[:4 * (n + 1)])
    base = 4 * (n + 1)
    outs = []
    for k in range(n):
        cp0, cp1 = cps[k], cps[k + 1]
        cnt = cp1 - cp0
        if cnt <= 0:
            continue
        pcd = plc[base + k * 8:base + k * 8 + 8]
        val = struct.unpack('<I', pcd[2:6])[0]
        compressed = bool(val & 0x40000000)
        fc = val & 0x3FFFFFFF
        if compressed:
            off = fc // 2
            raw = wd[off:off + cnt]
            try:
                txt = raw.decode('gbk', errors='replace')
            except Exception:
                txt = raw.decode('cp1252', errors='replace')
        else:
            off = fc
            raw = wd[off:off + cnt * 2]
            txt = raw.decode('utf-16le', errors='replace')
        outs.append(txt)
    return ''.join(outs)


if __name__ == '__main__':
    p = sys.argv[1]
    out = sys.argv[2]
    txt = extract_text(p)
    with io.open(out, 'w', encoding='utf-8') as f:
        f.write(txt)
    print('wrote', out, 'chars', len(txt))
