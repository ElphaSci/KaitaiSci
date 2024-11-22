meta:
  id: picture_header
  endian: le
seq:
- id: cell_offset # pic header soze
  type: u2
- id: num_cells
  type: u1
- id: is_compressed # split flag
  type: b1
- id: cell_rec_size # cell header size
  type: u2
- id: palette_offset
  type: u4
- id: width
  type: u2
- id: height
  type: u2
  
