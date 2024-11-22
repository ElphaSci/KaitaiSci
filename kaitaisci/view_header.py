# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class ViewHeader(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.loop_table_offset = self._io.read_u2le()
        self.num_loops = self._io.read_u1()
        self.unknown_byte = self._io.read_bytes(1)
        self.compressed = self._io.read_bits_int_le(1) != 0
        self._io.align_to_byte()
        self.view_size = self._io.read_u1()
        self.num_cells = self._io.read_u2le()
        self.palette_offset = self._io.read_u4le()
        self.loop_rec_size = self._io.read_u1()
        self.cell_rec_size = self._io.read_u1()
        self.x_res = self._io.read_u2le()
        self.y_res = self._io.read_u2le()

    @property
    def has_links(self):
        if hasattr(self, '_m_has_links'):
            return self._m_has_links if hasattr(self, '_m_has_links') else None

        self._m_has_links = self.cell_rec_size == 52
        return self._m_has_links if hasattr(self, '_m_has_links') else None


