# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class ViewCellHeader(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.width = self._io.read_s2le()
        self.height = self._io.read_s2le()
        self.x_shift = self._io.read_s2le()
        self.y_shift = self._io.read_s2le()
        self.transparent_color = self._io.read_u1()
        self.compression = self._io.read_u1()
        self.flags = self._io.read_s2le()
        self.image_and_pack_size = self._io.read_u4le()
        self.image_size = self._io.read_u4le()
        self.palette_offset = self._io.read_u4le()
        self.image_offset = self._io.read_u4le()
        self.pack_data_offset = self._io.read_u4le()
        self.lines_offset = self._io.read_u4le()
        self.link_table_offset = self._io.read_s4le()
        self.link_number = self._io.read_s2le()

    @property
    def has_links(self):
        if hasattr(self, '_m_has_links'):
            return self._m_has_links if hasattr(self, '_m_has_links') else None

        self._m_has_links = self.link_number != 0
        return self._m_has_links if hasattr(self, '_m_has_links') else None

    @property
    def pack_size(self):
        if hasattr(self, '_m_pack_size'):
            return self._m_pack_size if hasattr(self, '_m_pack_size') else None

        if self.compression != 0:
            self._m_pack_size = (self.image_and_pack_size - self.image_size)

        return self._m_pack_size if hasattr(self, '_m_pack_size') else None

    @property
    def line_size(self):
        if hasattr(self, '_m_line_size'):
            return self._m_line_size if hasattr(self, '_m_line_size') else None

        if self.lines_offset != 0:
            self._m_line_size = ((self.height * 4) * 2)

        return self._m_line_size if hasattr(self, '_m_line_size') else None


