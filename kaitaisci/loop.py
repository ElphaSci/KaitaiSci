# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct

from kaitaisci import loop_header, view_cell

if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Loop(KaitaiStruct):
    def __init__(self, file_offset, cell_rec_size, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.file_offset = file_offset
        self.cell_rec_size = cell_rec_size
        self._read()

    def _read(self):
        self.header = loop_header.LoopHeader(self._io)

    @property
    def files_cells_offset(self):
        if hasattr(self, '_m_files_cells_offset'):
            return self._m_files_cells_offset if hasattr(self, '_m_files_cells_offset') else None

        self._m_files_cells_offset = (self.file_offset + self.header.cells_offset)
        return self._m_files_cells_offset if hasattr(self, '_m_files_cells_offset') else None

    @property
    def based_on_loop(self):
        return self.header.based_on_loop

    @property
    def mirror(self):
        return self.header.mirror

    @property
    def cells(self):
        if hasattr(self, '_m_cells'):
            return self._m_cells if hasattr(self, '_m_cells') else None

        self._m_cells = [None] * (self.header.num_cells)
        for i in range(self.header.num_cells):
            self._m_cells[i] = view_cell.ViewCell(self.file_offset, (self.header.cells_offset + (i * self.cell_rec_size)), self._io, _parent=self)

        return self._m_cells if hasattr(self, '_m_cells') else None


