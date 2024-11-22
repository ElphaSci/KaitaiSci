# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
import os

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum

from kaitaisci import picture_header, palette, cell, skip

if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Picture(KaitaiStruct):

    @classmethod
    def from_file(cls, filename):
        pic = super().from_file(filename)
        # store the file name as id
        pic.id = os.path.splitext(os.path.split(filename)[-1])[0]
        return pic

    class P56PatchVersion(Enum):
        version_101 = 257
        version_8081 = 32897
        version_8181 = 33153
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.patch_info = KaitaiStream.resolve_enum(Picture.P56PatchVersion, self._io.read_s4le())
        self.header = picture_header.PictureHeader(self._io)
        self._raw_skip = self._io.read_bytes((((self.offset + self.header.cell_offset) - 14) - 4))
        _io__raw_skip = KaitaiStream(BytesIO(self._raw_skip))
        self.skip = skip.Skip(_io__raw_skip)
        self.cells = [None] * (self.header.num_cells)
        for i in range(self.header.num_cells):
            self.cells[i] = cell.Cell(0, self.header.cell_offset, self._io, _parent=self)


    @property
    def offset(self):
        if hasattr(self, '_m_offset'):
            return self._m_offset if hasattr(self, '_m_offset') else None

        self._m_offset = (26 if self.patch_info == Picture.P56PatchVersion.version_8081 else 4)
        return self._m_offset if hasattr(self, '_m_offset') else None

    @property
    def palette_size(self):
        if hasattr(self, '_m_palette_size'):
            return self._m_palette_size if hasattr(self, '_m_palette_size') else None

        _pos = self._io.pos()
        self._io.seek(self.header.palette_offset)
        self._m_palette_size = self._io.read_s4le()
        self._io.seek(_pos)
        return self._m_palette_size if hasattr(self, '_m_palette_size') else None

    @property
    def palette(self):
        if hasattr(self, '_m_palette'):
            return self._m_palette if hasattr(self, '_m_palette') else None

        _pos = self._io.pos()
        self._io.seek((self.header.palette_offset + 4))
        self._m_palette = palette.Palette(self._io)
        self._io.seek(_pos)
        return self._m_palette if hasattr(self, '_m_palette') else None


def main():
    resource_root = "/home/caleb/git/Realm_World_Creator"
    filename = "%s/Resources/56_Files/3.p56" % resource_root
    pic : Picture = Picture.from_file(filename)
    pic.cells[0].display_palette(draw=False)
    pic.cells[0].get_pil_image(draw=False)

    # filename_decomp = "%s/scires/KaitaiSCI/decomp_1250.v56" % resource_root
    # pic : Picture = Picture.from_file(filename)
    # pic.cells[0].display_palette(draw=True)
    # pic.cells[0].get_pil_image(draw=True)

if __name__ == '__main__':
    main()
