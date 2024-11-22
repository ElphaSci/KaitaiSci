meta:
  id: ressci
  endian: le
  
seq:
  - id: resources
    type: resource
    # repeat: expr
    # repeat-expr: 100
    repeat: eos

types:
  resource:
    seq:
      - id: type
        type: u1
        enum: res_type
      - id: number
        type: u2
      - id: packed_size
        type: u4
      - id: unpacked_size
        type: u4
      - id: compression_type
        type: u2
      - id: data
        type:
          switch-on: compression_type
          cases:
            32: compressed_data
            0: uncompressed_data
    instances:
      lzs_compression:
        value: compression_type == 32
    #   unpacked_data:
    #     size: unpacked_size
    #     # process: lzs_decompress(data)
    #     if: lzs_compression
        
    types:
      compressed_data:
        seq:
          - id: data
            size: _parent.packed_size
            # process: lzs_decompress(data)
            if: _parent.lzs_compression
      uncompressed_data:
        seq:
          - id: data
            size: _parent.packed_size
        

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
