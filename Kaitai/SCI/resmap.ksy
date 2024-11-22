meta:
  id: resmap
  endian: le
  
seq:
  - id: indices
    type: indices
    terminator: 0xff
  - id: entries_offset
    type: u2
  - id: magic
    contents: [0x34, 0x12, 0x00, 0x00]
  - id: entries
    type: entry
    repeat: eos
    
    
types:
  indices:
    seq:
      - id: index
        type: index
        repeat: eos
  index:
    seq:
      - id: resource_type
        type: u1
        enum: res_type
      - id: offset
        type: u2
  entry:
    seq:
      - id: resource_number
        type: u2
      - id: offset
        type: u4
        

enums:
  res_type:
    0: view
    1: pic
    2: script
    3: text
    4: sound
    5: memory
    6: vocab
    7: font
    8: cursor
    9: patch
    10: bitmap
    11: palette
    12: cd_audio
    13: audio
    14: sync
    15: message
    16: map
    17: heap
    18: audio_36
    19: sync_36
    20: translation
    21: robot
    22: vmd
    23: chunk
    24: animation
    25: etc
    26: duck
    27: clut
    28: tga
    29: zzz
    30: mac_icon_bar_pict_n
    31: mac_icon_bar_pict_s
    32: mac_pict
    33: rave
    34: invalid