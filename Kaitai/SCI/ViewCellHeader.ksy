meta:
  id: view_cell_header
  endian: le
    
seq:
- id: width
  type: u2
- id: height
  type: u2
- id: x_shift
  type: s2
- id: y_shift
  type: s2
- id: transparent_color
  type: u1
- id: compression
  type: u1
- id: flags
  type: u2
- id: image_and_pack_size
  type: s4
- id: image_size
  type: s4
- id: palette_offset
  type: s4
  doc: "Relative to end of cell header"
- id: image_offset
  type: s4
  doc: "Relative to start of file, after offset"
- id: pack_data_offset
  type: s4
- id: lines_offset
  type: s4
- id: link_table_offset
  type: s4
- id: link_number
  type: s2
  
instances:
  has_links:
    value: link_number != 0
  pack_size:
    value: image_and_pack_size - image_size
    if: compression != 0
  line_size:
    value: height * 4 * 2
    if: lines_offset != 0
  