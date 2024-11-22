meta:
  id: view
  file-extension: v56
  endian: le
  imports:
    - ViewHeader
    - Palette
    - ViewCell
    - LoopHeader
    - Loop
    

types:
  patch_info: 
    seq:
      - id: version
        type: s4


seq:
  - id: patch_info
    type: patch_info
    size: 26
  - id: header
    type: view_header


  
instances:
  offset:
    value: patch_info._sizeof
  palette:
    pos: offset + header.palette_offset
    type: palette
  loops:
    pos: offset + header.loop_table_offset + 2 # why so much magic?!?
    type: loop(offset, header.cell_rec_size)
    repeat: expr
    repeat-expr: header.num_loops
