from datetime import datetime
from typing import Any, Dict, List, Tuple, Union, get_args

from nonebot import get_driver, logger

from .config import Config, LevelName

pc = Config.parse_obj(get_driver().config)

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
        minimum = level_names.index(levels)
        levels = level_names[minimum:]
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
