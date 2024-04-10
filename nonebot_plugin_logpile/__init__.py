from datetime import datetime
from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata
from typing import Any, Dict, List, Tuple, Union, get_args

from nonebot import logger

from .config import Config, LevelName

__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-logpile",
    description="将 nonebot 的日志记录保存到本地文件",
    usage="",
    config=Config,
)
pc = get_plugin_config(Config)

LOG_CONFIG = {
    "rotation": "00:00",
    "enqueue": True,
    "encoding": "utf-8",
    "retention": f"{pc.logpile_retention} days",
}


def file_handler(
    levels: Union[LevelName, Tuple[LevelName]],
) -> List[Dict[str, Any]]:
    if not isinstance(levels, tuple):
        level_names = get_args(LevelName)
        # check if level exists
        level_index = level_names.index(levels)
        levels = tuple([level_names[level_index]])
    return [
        {
            "sink": pc.logpile_path
            / level.lower()
            / f"{level.lower()}-{datetime.now().date()}.log",
            "level": level,
            **LOG_CONFIG,
        }
        for level in levels
    ]


for handler in file_handler(pc.logpile_level):
    logger.add(**handler)
