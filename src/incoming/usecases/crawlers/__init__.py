from dataclasses import dataclass
from functools import cached_property


class Crawler:
    pass


@dataclass
class Page:
    """Datos retornados por los scrapers"""

    url: str
    title: str
    detail: str

    @cached_property
    def lower_title(self) -> str:
        return self.title.lower()

    @cached_property
    def lower_detail(self) -> str:
        return self.detai.lower()
