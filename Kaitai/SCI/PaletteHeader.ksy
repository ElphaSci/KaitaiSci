meta:
  id: palette_header
  endian: le
  
enums:
  pal_patch_version:
    0x8B: version_8b
    0x0B: version_0b
    0x0E: version_0e
  
seq:
  - id: pal_id
    type: s2
  - id: unk_bytes_1
    size: 11 
  - id: data_length
    type: u2
  - id: unk_bytes_2
    size: 10 
  - id: first_color
    type: s2
  - id: unk_bytes_3
    size: 2 
  - id: num_colors
    type: s2
  - id: exfour_color
    type: s1
  - id: triple_color
    type: s1
  - id: unk_bytes_4
    size: 4
    
instances:
  pal_patch_version:
    value: size
    enum: pal_patch_version