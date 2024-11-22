# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class PaletteHeader(KaitaiStruct):

    class PalPatchVersion(Enum):
        version_0b = 11
        version_0e = 14
        version_8b = 139
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.pal_id = self._io.read_s2le()
        self.unk_bytes_1 = self._io.read_bytes(11)
        self.data_length = self._io.read_u2le()
        self.unk_bytes_2 = self._io.read_bytes(10)
        self.first_color = self._io.read_s2le()
        self.unk_bytes_3 = self._io.read_bytes(2)
        self.num_colors = self._io.read_s2le()
        self.exfour_color = self._io.read_s1()
        self.triple_color = self._io.read_s1()
        self.unk_bytes_4 = self._io.read_bytes(4)

    @property
    def pal_patch_version(self):
        if hasattr(self, '_m_pal_patch_version'):
            return self._m_pal_patch_version if hasattr(self, '_m_pal_patch_version') else None

        self._m_pal_patch_version = KaitaiStream.resolve_enum(PaletteHeader.PalPatchVersion, self.size)
        return self._m_pal_patch_version if hasattr(self, '_m_pal_patch_version') else None


