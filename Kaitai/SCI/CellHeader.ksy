meta:
  id: cell_header
  endian: le
  imports:
    - Palette

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
    type: s2
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
  - id: z_depth
    type: s2
  - id: x_pos
    type: s2
  - id: y_pos
    type: s2
  - id: unknown_bytes
    size: 2
  
  