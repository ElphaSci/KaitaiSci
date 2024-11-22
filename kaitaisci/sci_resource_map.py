# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Resmap(KaitaiStruct):

    class ResType(Enum):
        view = 0
        pic = 1
        script = 2
        text = 3
        sound = 4
        memory = 5
        vocab = 6
        font = 7
        cursor = 8
        patch = 9
        bitmap = 10
        palette = 11
        cd_audio = 12
        audio = 13
        sync = 14
        message = 15
        map = 16
        heap = 17
        audio_36 = 18
        sync_36 = 19
        translation = 20
        robot = 21
        vmd = 22
        chunk = 23
        animation = 24
        etc = 25
        duck = 26
        clut = 27
        tga = 28
        zzz = 29
        mac_icon_bar_pict_n = 30
        mac_icon_bar_pict_s = 31
        mac_pict = 32
        rave = 33
        invalid = 34
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self._raw_indices = self._io.read_bytes_term(255, False, True, True)
        _io__raw_indices = KaitaiStream(BytesIO(self._raw_indices))
        self.indices = Resmap.Indices(_io__raw_indices, self, self._root)
        self.entries_offset = self._io.read_u2le()
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x34\x12\x00\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x34\x12\x00\x00", self.magic, self._io, u"/seq/2")
        self.entries = []
        i = 0
        while not self._io.is_eof():
            self.entries.append(Resmap.Entry(self._io, self, self._root))
            i += 1


    class Indices(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.index = []
            i = 0
            while not self._io.is_eof():
                self.index.append(Resmap.Index(self._io, self, self._root))
                i += 1



    class Index(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.resource_type = KaitaiStream.resolve_enum(Resmap.ResType, self._io.read_u1())
            self.offset = self._io.read_u2le()


    class Entry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.resource_number = self._io.read_u2le()
            self.offset = self._io.read_u4le()



def load_resource_map(filename: str):
    map : Resmap = Resmap.from_file(filename)
    # Assume the first entry.offset is the offset of the very first entry (i.e. assume it's ordered..)
    index = map.indices.index
    res_type_map = {idx.resource_type:{} for idx in index}
    entry_start_pos = index[0].offset
    cur_pos = entry_start_pos
    cur_idx = 0
    cur_type_entry = index[cur_idx]
    next_type_offset = index[cur_idx+1].offset
    at_last_idx = False
    for res_entry in map.entries:
        #  if we have moved to the next resource type, increment the index
        if cur_pos >= next_type_offset and cur_idx+1 < len(index):
            cur_idx += 1
            cur_type_entry = index[cur_idx]
            if cur_idx+1 == len(index):
                at_last_idx = True
            if not at_last_idx:
                next_type_offset = index[cur_idx+1].offset

        # add the entry to the map
        res_num = res_entry.resource_number
        res_offset = res_entry.offset
        res_type_map[cur_type_entry.resource_type][res_num] = res_offset
        # increment our position
        cur_pos += 6
    return res_type_map

if __name__ == '__main__':
    map = load_resource_map("/Resources/ressci/resmap.000")






