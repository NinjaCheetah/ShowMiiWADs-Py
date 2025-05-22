# "modules/config.py" licensed under the MIT license
# Copyright 2025 NinjaCheetah and Contributors

import os
import json
import pathlib


def get_config_file() -> pathlib.Path:
    config_dir = pathlib.Path(os.path.join(
        os.environ.get('APPDATA') or
        os.environ.get('XDG_CONFIG_HOME') or
        os.path.join(os.environ['HOME'], '.config'),
        "ShowMiiWADs-Py"
    ))
    config_dir.mkdir(exist_ok=True)
    return config_dir.joinpath("config.json")


def save_config(config_data: dict) -> None:
    config_file = get_config_file()
    print(f"writing data: {config_data}")
    open(config_file, "w").write(json.dumps(config_data, indent=4))


def update_setting(config_data: dict, setting: str, value: any) -> None:
    config_data[setting] = value
    save_config(config_data)


def add_new_folder(config_data: dict, path: str) -> None:
    try:
        paths = config_data["folder_paths"]
    except KeyError:
        paths = []
    paths.insert(0, path)
    if len(paths) > 5:
        paths.remove(5)
    config_data["folder_paths"] = paths
    save_config(config_data)
