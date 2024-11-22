# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum

from kaitaisci.lzs.decompress import decompress
from kaitaisci.picture import Picture
from kaitaisci.view import View

if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))


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


class Ressci(KaitaiStruct):

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.resources = []
        while not self._io.is_eof():
            self.resources.append(Ressci.Resource(self._io, self, self._root))

    class Resource(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(ResType, self._io.read_u1())
            self.number = self._io.read_u2le()
            self.packed_size = self._io.read_u4le()
            self.unpacked_size = self._io.read_u4le()
            self.compression_type = self._io.read_u2le()
            self.data = self._io.read_bytes(self.packed_size)

        @property
        def lzs_compression(self):
            if hasattr(self, '_m_lzs_compression'):
                return self._m_lzs_compression if hasattr(self, '_m_lzs_compression') else None

            self._m_lzs_compression = self.compression_type == 32
            return self._m_lzs_compression if hasattr(self, '_m_lzs_compression') else None

        @property
        def unpacked_data(self):
            if hasattr(self, '_unpacked_data'):
                return self._unpacked_data if hasattr(self, '_unpacked_data') else None

            self._unpacked_data = get_unpacked_data(self)
            return self._unpacked_data if hasattr(self, '_unpacked_data') else None

    @property
    def resource_map(self):
        if hasattr(self, '_resource_map'):
            return self._resource_map if hasattr(self, '_resource_map') else None

        self._resource_map = {restype: {} for restype in ResType}
        for r in self.resources:
            resource: Ressci.Resource = r
            num = resource.number
            self._resource_map[resource.type][num] = resource
        return self._resource_map

    def has_resource(self, type: ResType, num: int):
        if type in self.resource_map.keys():
            return num in self.resource_map[type].keys()
        return False

    def get_pic(self, pic_num: int) -> Picture:
        pic_header = bytearray([0x81] * 2 + [0x00] * 2)
        pic_res : Ressci.Resource = self.resource_map[ResType.pic][pic_num]
        bin_dat = pic_header + pic_res.unpacked_data
        pic = Picture.from_bytes(bin_dat)
        pic.id = pic_res.number
        return pic

    def get_view(self, view_num: int) -> View:
        view_header = bytearray([0x80, 0x80] + [0x00] * 24)
        view_res : Ressci.Resource = self.resource_map[ResType.view][view_num]
        view = View.from_bytes(view_header + view_res.unpacked_data)
        view.id = view_res.number
        return view


def get_unpacked_data(resource: Ressci.Resource):
    if (resource.compression_type == 32):
        return decompress(resource.data)
    return resource.data


def draw_pic(pic_res: Ressci.Resource, cell=0):
    pic_header = bytearray([0x81] * 2 + [0x00] * 2)
    bin_dat = pic_header + get_unpacked_data(pic_res)
    p: Picture = Picture.from_bytes(bin_dat)
    if len(p.cells) > cell:
        p.cells[cell].get_pil_image(draw=True)


def draw_view(view_res: Ressci.Resource, loop=0, cell=0):
    view_header = bytearray([0x80, 0x80] + [0x00] * 24)
    v = View.from_bytes(view_header + get_unpacked_data(view_res))
    if len(v.loops) > loop and len(v.loops[loop].cells) > cell:
        v.loops[loop].cells[cell].get_pil_image(draw=True)


if __name__ == '__main__':
    ressci_path = "/home/caleb/IdeaProjects/kotlinrealm/scikot/src/test/resources/res/RESSCI.000"
    # ressci_path = "/home/caleb/PycharmProjects/Realm_World_Creator/Resources/ressci/ressci.000"
    res = Ressci.from_file(ressci_path)
    pic = res.get_view(101)
    pic.loops[0].cells[0].get_pil_image(draw=True)

    # pic = Picture.from_file("/home/caleb/IdeaProjects/kotlinrealm/scikot/src/test/resources/pictures/3_original.p56")
    # cell = pic.cells[0]
    # cell.get_pil_image(draw=True)
    # res_map = {restype: {} for restype in ResType}
    # for r in res.resources:
    #     resource: Ressci.Resource = r
    #     num = resource.number
    #     res_map[resource.type][num] = resource
    #
    # res1250 = res_map[ResType.view][1250]
    # draw_view(res1250)
    #
    # pic3: Ressci.Resource = res_map[ResType.pic][3]
    # draw_pic(pic3)
