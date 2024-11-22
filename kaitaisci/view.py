# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
import os

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO

from kaitaisci import palette, loop, view_header

if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class View(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()


    @classmethod
    def from_file(cls, filename):
        view = super().from_file(filename)
        # store the file name as id
        view.id = os.path.splitext(os.path.split(filename)[-1])[0]
        return view

    def _read(self):
        self._raw_patch_info = self._io.read_bytes(26)
        _io__raw_patch_info = KaitaiStream(BytesIO(self._raw_patch_info))
        self.patch_info = View.PatchInfo(_io__raw_patch_info, self, self._root)
        self.header = view_header.ViewHeader(self._io)

    class PatchInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.version = self._io.read_s4le()


    @property
    def offset(self):
        if hasattr(self, '_m_offset'):
            return self._m_offset if hasattr(self, '_m_offset') else None

        self._m_offset = 26
        return self._m_offset if hasattr(self, '_m_offset') else None

    @property
    def palette(self):
        if hasattr(self, '_m_palette'):
            return self._m_palette if hasattr(self, '_m_palette') else None

        _pos = self._io.pos()
        self._io.seek((self.offset + self.header.palette_offset))
        self._m_palette = palette.Palette(self._io)
        self._io.seek(_pos)
        return self._m_palette if hasattr(self, '_m_palette') else None

    @property
    def loops(self):
        if hasattr(self, '_m_loops'):
            return self._m_loops if hasattr(self, '_m_loops') else None

        _pos = self._io.pos()
        self._io.seek(((self.offset + self.header.loop_table_offset) + 2))
        self._m_loops = [None] * (self.header.num_loops)
        for i in range(self.header.num_loops):
            self._m_loops[i] = loop.Loop(self.offset, self.header.cell_rec_size, self._io, _parent=self)

        self._io.seek(_pos)
        return self._m_loops if hasattr(self, '_m_loops') else None

def main():
    resource_root = "/home/caleb/git/Realm_World_Creator"
    filename = "%s/Resources/56_Files/1250.v56" % resource_root
    view : View = View.from_file(filename)
    view.loops[0].cells[0].display_palette(draw=True)
    view.loops[0].cells[0].get_pil_image(draw=True)

    filename_decomp = "%s/scires/KaitaiSCI/decomp_1250.v56" % resource_root
    view : View = View.from_file(filename)
    view.loops[0].cells[0].display_palette(draw=True)
    view.loops[0].cells[0].get_pil_image(draw=True)

if __name__ == '__main__':
    main()

