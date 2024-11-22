meta:
  id: view_header
  endian: le
  
seq:
  - id: loop_table_offset # header size
    type: u2
  - id: num_loops
    type: u1
  - id: strip_view
    type: u1
  - id: compressed # split view?
    type: b1le
  - id: view_size # resolution
    type: u1
  - id: num_cells
    type: u2
  - id: palette_offset
    type: u4
  - id: loop_rec_size # loop hgeader size
    type: u1
  - id: cell_rec_size #cell header size
    type: u1
  - id: x_res
    type: u2
  - id: y_res
    type: u2
  - id: version
    type: u1
  - id: future_use
    type: u1

instances:
  has_links:
    value: cell_rec_size == 0x034