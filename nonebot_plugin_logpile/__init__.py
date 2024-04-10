from typing import Any, Dict, List, Tuple, Union

from nonebot import get_plugin_config, logger
from nonebot.plugin import PluginMetadata

from .config import Config, LevelName

__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-logpile",
    description="将 nonebot 的日志记录保存到本地文件",
    usage="",
    type="library",
    homepage="https://github.com/A-kirami/nonebot-plugin-logpile",
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
    if isinstance(levels, str):
        return [
            {
                "sink": pc.logpile_path / "{time:YYYY-MM-DD}.log",
                "level": levels,
                **LOG_CONFIG,
            }
        ]
    return [
        {
            "sink": pc.logpile_path / level.lower() / "{time:YYYY-MM-DD}.log",
            "level": level,
            "filter": lambda record, level=level: record["level"].name == level,
            **LOG_CONFIG,
        }
        for level in levels
    ]


for handler in file_handler(pc.logpile_level):
    logger.add(**handler)
