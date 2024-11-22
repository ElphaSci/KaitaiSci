meta:
  id: picture
  file-extension: p56
  endian: le
  imports:
    - PictureHeader
    - Palette
    - CellHeader
    - Cell
    - Skip

enums:
  p56_patch_version:
    0x0101: version_101
    0x8081: version_8081
    0x8181: version_8181


seq:
- id: patch_info
  type: s4
  enum: p56_patch_version
- id: header
  type: picture_header
- id: skip
  type: skip
  size: offset + header.cell_offset - sizeof<picture_header> - sizeof<s4>
- id: cells
  type: cell(0, header.cell_offset)
  repeat: expr
  repeat-expr: header.num_cells
  
  
  
instances:
  offset:
    value: 'patch_info == p56_patch_version::version_8081 ? 26 : 4'
  palette_size:
    pos: header.palette_offset
    type: s4
  palette:
    pos: header.palette_offset + sizeof<s4>
    type: palette