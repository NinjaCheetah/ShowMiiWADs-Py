# "modules/lz77.py" licensed under the MIT license
# Copyright 2025 NinjaCheetah and Contributors

import pathlib

from rust_modules import *

def compress_lz77(file_path: pathlib.Path, progress_callback=None):
    _ = progress_callback  # This is just to shut PyCharm up about unused variables.
    data = file_path.read_bytes()
    compressed_data = rs_compress_lz77(data)
    file_path.with_suffix(".lz77").write_bytes(compressed_data)
    return file_path

def decompress_lz77(file_path: pathlib.Path, progress_callback=None):
    _ = progress_callback
    data = file_path.read_bytes()
    try:
        decompressed_data = rs_decompress_lz77(data)
    except ValueError:
        return None
    file_path.with_suffix(".out").write_bytes(decompressed_data)
    return file_path
