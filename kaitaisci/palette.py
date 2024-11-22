# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct

from kaitaisci import palette_header

if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))


class Palette(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = palette_header.PaletteHeader(self._io)
        self.colors = [None] * (256)
        for i in range(256):
            _on =  ((i >= self.header.first_color) and (i < (self.header.num_colors + self.header.first_color)))
            if _on == True:
                self.colors[i] = Palette.PalEntry(self._io, self, self._root)
            elif _on == False:
                self.colors[i] = Palette.PalEntryEmpty(self._io, self, self._root)


    class PalEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if self._parent.header.triple_color == 0:
                self.remap = self._io.read_u1()

            self.red = self._io.read_u1()
            self.green = self._io.read_u1()
            self.blue = self._io.read_u1()


    class PalEntryEmpty(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass

        @property
        def remap(self):
            if hasattr(self, '_m_remap'):
                return self._m_remap if hasattr(self, '_m_remap') else None

            if self._parent.header.triple_color == 0:
                self._m_remap = 0

            return self._m_remap if hasattr(self, '_m_remap') else None

        @property
        def red(self):
            if hasattr(self, '_m_red'):
                return self._m_red if hasattr(self, '_m_red') else None

            self._m_red = 0
            return self._m_red if hasattr(self, '_m_red') else None

        @property
        def green(self):
            if hasattr(self, '_m_green'):
                return self._m_green if hasattr(self, '_m_green') else None

            self._m_green = 0
            return self._m_green if hasattr(self, '_m_green') else None

        @property
        def blue(self):
            if hasattr(self, '_m_blue'):
                return self._m_blue if hasattr(self, '_m_blue') else None

            self._m_blue = 0
            return self._m_blue if hasattr(self, '_m_blue') else None

