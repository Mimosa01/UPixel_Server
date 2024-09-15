from typing import Optional, List

from pydantic import BaseModel


class SRect(BaseModel):
    index_rect: int
    index_color: int
    current_index: Optional[int] = None


class SPictures(BaseModel):
    is_coloring: bool
    palette: List[str]
    grid: int
    rects: List[SRect]
