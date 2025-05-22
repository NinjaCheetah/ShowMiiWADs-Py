# "modules/coredata.py" licensed under the MIT license
# Copyright 2025 NinjaCheetah and Contributors

import re

import libWiiPy


def process_wad_info(file_name, title: libWiiPy.title.Title) -> dict:
    wad_info = {}
    wad_info["name"] = file_name
    wad_info["type"] = title.tmd.get_title_type()
    wad_info["channel_name"] = ""
    banner_data = title.get_content_by_index(0)
    banner_u8 = libWiiPy.archive.U8Archive()
    try:
        banner_u8.load(banner_data)
        if banner_u8.imet_header.magic != "":
            channel_title = banner_u8.imet_header.get_channel_names(banner_u8.imet_header.LocalizedTitles.TITLE_ENGLISH)
            wad_info["channel_name"] = channel_title
    except TypeError:
        pass
    wad_info["ascii_tid"] = ""
    ascii_tid = ""
    try:
        ascii_tid = (bytes.fromhex(title.tmd.title_id[8:].replace("00", "30"))).decode("ascii")
    except UnicodeDecodeError:
        pass
    pattern = r"^[a-z0-9!@#$%^&*]{4}$"
    if re.fullmatch(pattern, ascii_tid, re.IGNORECASE):
        wad_info["ascii_tid"] = ascii_tid
    wad_info["size_blocks"] = f"{title.get_title_size_blocks()}-{title.get_title_size_blocks(True)}"
    wad_info["version"] = f"{title.tmd.title_version}"
    wad_info["size_mb"] = f"{round(title.get_title_size() / 1048576, 2)} - {round(title.get_title_size(True) / 1048576, 2)} MB"
    wad_info["ios"] = f"IOS{int(title.tmd.ios_tid[-2:], 16)}"
    if title.tmd.title_id == "0000000100000002":
        match title.tmd.title_version_converted[-1:]:
            case "U":
                wad_info["region"] = "USA"
            case "E":
                wad_info["region"] = "EUR"
            case "J":
                wad_info["region"] = "JPN"
            case "K":
                wad_info["region"] = "KOR"
            case _:
                wad_info["region"] = "None"
    elif title.tmd.get_title_type() == "System":
        wad_info["region"] = "None"
    else:
        wad_info["region"] = title.tmd.get_title_region()
    wad_info["contents"] = f"{title.tmd.num_contents}"
    return wad_info
