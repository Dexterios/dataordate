from ast import Str
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List


@dataclass
class ID():
    name:str
    discription:List[Str]
    foto: Path
    BIRTHDAY: datetime
