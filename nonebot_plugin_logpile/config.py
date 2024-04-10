from pathlib import Path
from typing import Literal, Tuple, Union

from pydantic import BaseModel, Extra, validator

LevelName = Literal["TRACE", "DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "CRITICAL"]


class Config(BaseModel, extra=Extra.ignore):
    logpile_path: Path = Path.cwd() / "logs"
    logpile_level: Union[LevelName, Tuple[LevelName]] = "ERROR"
    logpile_retention: int = 14

    @validator("logpile_path")
    def check_path(cls, v: Path) -> Path:
        if v.exists() and not v.is_dir():
            raise ValueError("必须是有效的文件目录")
        v.mkdir(parents=True, exist_ok=True)
        return v
