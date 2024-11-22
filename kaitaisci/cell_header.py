# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class CellHeader(KaitaiStruct):
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
        self.z_depth = self._io.read_s2le()
        self.x_pos = self._io.read_s2le()
        self.y_pos = self._io.read_s2le()
        self.unknown_bytes = self._io.read_bytes(2)


