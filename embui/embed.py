"""Embed."""

import dataclasses
import datetime
from typing import List, Optional

from .colour import Colour
from .image import Image

__all__ = ["Author", "Field", "Footer", "Embed"]


@dataclasses.dataclass(frozen=True)
class Author:
    name: Optional[str] = None
    icon_url: Optional[Image] = None
    url: Optional[str] = None


@dataclasses.dataclass(frozen=True)
class Field:
    name: str = None
    value: str = None
    inline: Optional[bool] = None


@dataclasses.dataclass(frozen=True)
class Footer:
    text: Optional[str] = None
    icon_url: Optional[Image] = None


@dataclasses.dataclass()
class Embed:
    title: Optional[str] = None
    description: Optional[str] = None
    colour: Optional[Colour] = None

    image: Optional[Image] = None
    thumbnail: Optional[Image] = None

    author: Author = dataclasses.field(default_factory=Author)
    footer: Footer = dataclasses.field(default_factory=Footer)
    fields: List[Field] = dataclasses.field(default_factory=list)

    url: Optional[str] = None
    timestamp: Optional[datetime.datetime] = None
