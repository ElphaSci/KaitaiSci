meta:
  id: view_cell
  endian: le
  imports:
    - ViewCellHeader
    - Palette
    - View
    - Link
params:
  - id: file_offset
    type: u2
  - id: cell_offset
    type: u2
  
instances:
  is_compressed:
    value:  _parent.as<loop>._parent.as<view>.header.compressed
  palette:
    value: _parent.as<loop>._parent.as<view>.palette
  im_offset:
    value: file_offset + cell_offset + header.image_offset
  header:
    pos: file_offset + cell_offset 
    type: view_cell_header
  image:
    pos: file_offset + header.image_offset
    size: header.compression == 0 ? header.width  * header.height : header.image_size
  pack:
    pos: file_offset + header.pack_data_offset
    size: header.pack_size
    if: header.compression != 0
  lines:
    pos: file_offset + header.lines_offset
    size: header.line_size
    if: header.lines_offset != 0
  links:
    pos: file_offset + header.link_table_offset
    if: header.has_links
    type: link
    repeat: expr
    repeat-expr: header.link_number
  