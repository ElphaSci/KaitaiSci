meta:
  id: loop
  endian: le
  imports:
    - LoopHeader
    - ViewCell
    - Cell
    - View
    

params:
  - id: file_offset
    type: u2
  - id: cell_rec_size
    type: u1
seq:
  - id: header
    type: loop_header
    
    
instances:
  files_cells_offset:
    value: file_offset + header.cells_offset
  cells:
    type: view_cell(file_offset, header.cells_offset + _index*cell_rec_size)
    repeat: expr
    repeat-expr: header.num_cells