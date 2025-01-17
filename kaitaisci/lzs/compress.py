#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
General-purpose sliding-window lossless compression
Based on LZ77/78 work
Aiming to be suitable for embedded systems

This code is licensed according to the MIT license as follows:
----------------------------------------------------------------------------
Copyright (c) 2017 Craig McQueen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
----------------------------------------------------------------------------
"""

from kaitaisci.lzs.lzs import *

def compress(in_data):
    # Make the compression coder, with a chosen length coder
    LZCM = LZCMCoder(OffsetCoder1(7,11), LengthCoder1)
#    LZCM = LZCMCoder(OffsetCoder2(12), LengthCoder8)
    compressed_data = LZCM.compress(in_data)
    encoded = LZCM.encode(compressed_data)
    return encoded

def main():
    if 1:
        with open(sys.argv[1], "rb") as in_stream, open(sys.argv[2], "wb") as out_stream:
            in_data = in_stream.read()
            compressed_data = compress(in_data)
            out_stream.write(compressed_data)

if __name__ == '__main__':
    main()
