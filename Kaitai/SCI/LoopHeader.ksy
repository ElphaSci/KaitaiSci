meta:
  id: loop_header
  endian: le
  
seq:
  - id: based_on_loop
    type: s1
  - id: mirror
    type: b1le
  - id: num_cells
    type: u1
  - id: cont_loop
    type: s1
  - id: start_cel
    type: s1
  - id: end_cel
    type: s1
  - id: repeat_count
    type: u1
  - id: step_size
    type: u1
  - id: palette_offset
    type: s4
  - id: cells_offset
    type: s4
