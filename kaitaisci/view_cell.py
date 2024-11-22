# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
from PIL import Image
from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct

from kaitaisci import view_cell_header, link
from kaitaisci.view_cell_header import ViewCellHeader

if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class ViewCell(KaitaiStruct):
    def __init__(self, file_offset, cell_offset, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.file_offset = file_offset
        self.cell_offset = cell_offset
        self._read()

    def _read(self):
        pass

    @property
    def im_offset(self):
        if hasattr(self, '_m_im_offset'):
            return self._m_im_offset if hasattr(self, '_m_im_offset') else None

        self._m_im_offset = ((self.file_offset + self.cell_offset) + self.header.image_offset)
        return self._m_im_offset if hasattr(self, '_m_im_offset') else None

    @property
    def header(self):
        if hasattr(self, '_m_header'):
            return self._m_header if hasattr(self, '_m_header') else None

        _pos = self._io.pos()
        self._io.seek((self.file_offset + self.cell_offset))
        self._m_header : ViewCellHeader = view_cell_header.ViewCellHeader(self._io)
        self._io.seek(_pos)
        return self._m_header if hasattr(self, '_m_header') else None

    @property
    def image(self):
        if hasattr(self, '_m_image'):
            return self._m_image if hasattr(self, '_m_image') else None

        _pos = self._io.pos()
        self._io.seek((self.file_offset + self.header.image_offset))
        self._m_image = self._io.read_bytes(((self.header.width * self.header.height) if self.header.compression == 0 else self.header.image_size))
        self._io.seek(_pos)
        return self._m_image if hasattr(self, '_m_image') else None


    @property
    def palette(self):
        if hasattr(self, '_m_palette'):
            return self._m_palette if hasattr(self, '_m_palette') else None

        self._m_palette = self._parent._parent.palette
        return self._m_palette if hasattr(self, '_m_palette') else None

    @property
    def links(self):
        if hasattr(self, '_m_links'):
            return self._m_links if hasattr(self, '_m_links') else None

        if self.header.has_links:
            _pos = self._io.pos()
            self._io.seek((self.file_offset + self.header.link_table_offset))
            self._m_links = [None] * (self.header.link_number)
            for i in range(self.header.link_number):
                self._m_links[i] = link.Link(self._io)

            self._io.seek(_pos)

        return self._m_links if hasattr(self, '_m_links') else None

    @property
    def pack(self):
        if hasattr(self, '_m_pack'):
            return self._m_pack if hasattr(self, '_m_pack') else None

        if self.header.compression != 0:
            _pos = self._io.pos()
            self._io.seek((self.file_offset + self.header.pack_data_offset))
            self._m_pack = self._io.read_bytes(self.header.pack_size)
            self._io.seek(_pos)

        return self._m_pack if hasattr(self, '_m_pack') else None

    @property
    def lines(self):
        if hasattr(self, '_m_lines'):
            return self._m_lines if hasattr(self, '_m_lines') else None

        if self.header.lines_offset != 0:
            _pos = self._io.pos()
            self._io.seek((self.file_offset + self.header.lines_offset))
            self._m_lines = self._io.read_bytes(self.header.line_size)
            self._io.seek(_pos)
        return self._m_lines if hasattr(self, '_m_lines') else None


    @property
    def y_shift(self):
        return self.header.y_shift

    @property
    def x_shift(self):
        return self.header.x_shift


    @property
    def width(self):
        return self.header.width

    @property
    def height(self):
        return self.header.height

    @property
    def is_compressed(self):
        if hasattr(self, '_m_is_compressed'):
            return self._m_is_compressed if hasattr(self, '_m_is_compressed') else None

        self._m_is_compressed = self._parent._parent.header.compressed
        return self._m_is_compressed if hasattr(self, '_m_is_compressed') else None



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
        if self.is_compressed:
            return self.get_compressed_pil_image(draw, transparent)
        return self.get_uncompressed_pil_image(draw, transparent)

    def get_compressed_pil_image(self, draw=False, transparent=True):
        ptags = iter(self.image)
        pdata = iter(self.pack)
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