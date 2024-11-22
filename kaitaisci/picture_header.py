# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class PictureHeader(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.cell_offset = self._io.read_s2le()
        self.num_cells = self._io.read_s1()
        self.is_compressed = self._io.read_bits_int_be(1) != 0
        self._io.align_to_byte()
        self.cell_rec_size = self._io.read_u2le()
        self.palette_offset = self._io.read_u2le()
        self.skip_bytes = self._io.read_bytes(2)
        self.width = self._io.read_u2le()
        self.height = self._io.read_u2le()


