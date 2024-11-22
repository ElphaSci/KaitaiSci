meta:
  id: palette
  endian: le
  imports:
    - PaletteHeader
  
seq:
  - id: header
    type: palette_header
  - id: colors
    repeat: expr
    repeat-expr: 256
    type: 
      switch-on: _index >= header.first_color and _index < (header.num_colors + header.first_color)
      cases:
        true: pal_entry
        false: pal_entry_empty
    
    
types:
  pal_entry:
    seq:
      - id: remap
        type: u1
        if: _parent.header.triple_color == 0
      - id: red
        type: u1
      - id: green
        type: u1
      - id: blue
        type: u1
  pal_entry_empty:
    instances:
      remap:
        value: 0
        if: _parent.header.triple_color == 0
      red:
        value: 0
      green:
        value: 0
      blue:
        value: 0