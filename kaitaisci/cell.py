# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
import struct

from PIL import Image
from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO

from kaitaisci import cell_header, skip

if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Cell(KaitaiStruct):
    def __init__(self, file_offset, cell_offset, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.file_offset = file_offset
        self.cell_offset = cell_offset
        self._read()

    def _read(self):
        self._raw_skip_to_cell = self._io.read_bytes(self.file_offset)
        _io__raw_skip_to_cell = KaitaiStream(BytesIO(self._raw_skip_to_cell))
        self.skip_to_cell = skip.Skip(_io__raw_skip_to_cell)
        self.header = cell_header.CellHeader(self._io)
        self._raw_skip_to_image = self._io.read_bytes(self.relative_image_offset)
        _io__raw_skip_to_image = KaitaiStream(BytesIO(self._raw_skip_to_image))
        self.skip_to_image = skip.Skip(_io__raw_skip_to_image)
        self.image = self._io.read_bytes(((self.header.width * self.header.height) if self.header.compression == 0 else self.header.image_size))

    @property
    def relative_image_offset(self):
        if hasattr(self, '_m_relative_image_offset'):
            return self._m_relative_image_offset if hasattr(self, '_m_relative_image_offset') else None

        self._m_relative_image_offset = ((self.header.image_offset - 44) - self.cell_offset)
        return self._m_relative_image_offset if hasattr(self, '_m_relative_image_offset') else None

    @property
    def palette(self):
        if hasattr(self, '_m_palette'):
            return self._m_palette if hasattr(self, '_m_palette') else None

        self._m_palette = self._parent.palette
        return self._m_palette if hasattr(self, '_m_palette') else None




    def get_uncompressed_pil_image(self, draw=False, transparent=True):
        image = self.image
        pal_data = self.palette.colors
        rgba_im = []
        for x in image:
            color = [pal_data[x].red, pal_data[x].green, pal_data[x].blue, 255]
            if transparent and x == self.header.transparent_color:
                color[-1] = 0
            rgba_im += color
        width = int(len(rgba_im) / (self.header.height * 4))
        pil_im = Image.frombuffer('RGBA', (width, self.header.height), bytes(rgba_im), 'raw', 'RGBA', 0, 1)
        if draw:
            import matplotlib.pyplot as plt
            plt.imshow(pil_im, interpolation='none')
            plt.show()
        return pil_im

    def get_pil_image(self, draw=False, transparent=True):
        if self.header.compression == 0:
            return self.get_uncompressed_pil_image(draw, transparent)
        return self.get_compressed_pil_image(draw, transparent)

    def get_compressed_pil_image(self, draw=False, transparent=True):
        ptags = iter(self.image)
        pdata = iter(self._pack)
        pal_data = self.palette.colors
        rgba_im = []
        last_pal_entry = pal_data[255]
        # this is typically the transparent color, if not, it will set that below
        last_rgba = [last_pal_entry.red, last_pal_entry.green, last_pal_entry.blue, 0]
        last_rgba_opaque = [last_pal_entry.red, last_pal_entry.green, last_pal_entry.blue, 255]
        for i in range(self.header.height):
            cur_width = 0
            while cur_width < self.header.width:
                switch = next(ptags)
                if switch >> 6 == 2:
                    color = next(pdata)
                    pal_entry = pal_data[color]
                    if color == self.header.transparent_color and transparent:
                        rgba_im.extend([pal_entry.red, pal_entry.green, pal_entry.blue, 0] * (switch - 0x80))
                    else:
                        rgba_im.extend([pal_entry.red, pal_entry.green, pal_entry.blue, 255] * (switch - 0x80))
                    cur_width += switch - 0x80
                elif switch >> 6 == 3:
                    if 255 != self.header.transparent_color or not transparent:
                        rgba_im.extend(last_rgba_opaque * (switch - 0xC0))
                    else:
                        rgba_im.extend(last_rgba * (switch - 0xC0))
                    cur_width += switch - 0xC0
                else:
                    for j in range(switch):
                        col = next(pdata)
                        pal_entry = pal_data[col]
                        if col == self.header.transparent_color and transparent:
                            rgba_im.extend([pal_entry.red, pal_entry.green, pal_entry.blue, 0])
                        else:
                            rgba_im.extend([pal_entry.red, pal_entry.green, pal_entry.blue, 255])
                    cur_width += switch
        pil_im = Image.frombuffer('RGBA', (self.header.width, self.header.height), bytes(rgba_im), 'raw',
                                  'RGBA', 0, 1)
        if draw:
            import matplotlib.pyplot as plt
            plt.imshow(pil_im, interpolation='none')
            plt.show()
        return pil_im

    def display_palette(self, draw=True):
        flat_rgb_list = [[x.red, x.green, x.blue] for x in self.palette.colors]
        rgba_im = []
        for x in flat_rgb_list:
            rgba_im.extend(x)
        pil_im = Image.frombuffer('RGB', (16, 16), bytes(rgba_im), 'raw', 'RGB', 0, 1)
        if draw:
            import matplotlib.pyplot as plt
            plt.imshow(pil_im, interpolation='none')
            plt.show()
        else:
            return pil_im
