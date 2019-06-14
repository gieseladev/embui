""""Colour related things."""

import colorsys
from typing import Tuple

__all__ = ["Colour"]


def _shift(n: int, mask: int, shift: int) -> int:
    return (n << shift) & mask


def _unshift(n: int, mask: int, shift: int) -> int:
    return (n & mask) >> shift


class Colour(int):
    """Discord colour representation."""

    def __repr__(self) -> str:
        return f"Colour({self!r})"

    def __str__(self) -> str:
        return f"#{self:0>6x}"

    @property
    def r(self) -> int:
        """Red value of the colour."""
        return _unshift(self, 0xFF0000, 16)

    @property
    def g(self) -> int:
        """Green value of the colour."""
        return _unshift(self, 0x00FF00, 8)

    @property
    def b(self) -> int:
        """Blue value of the colour."""
        return _unshift(self, 0x0000FF, 0)

    def as_tuple(self) -> Tuple[int, int, int]:
        """Get a 3-tuple containing the red, green, and blue values.

        Returns:
            Tuple containing the values of the 3 colours as integers
            in the closed interval [0, 255].
        """
        return self.r, self.g, self.b

    @classmethod
    def from_rgb(cls, r: int, g: int, b: int):
        """Create a new colour from the RGB values.

        Provided values must be in the closed interval [0, 255]. Invalid
        values are truncated.

        Args:
            r: Red value.
            g: Green value.
            b: Blue value.

        Returns:
            A new colour instance with the given values.
        """
        return cls(_shift(r, 0xFF0000, 16) +
                   _shift(g, 0x00FF00, 8) +
                   _shift(b, 0x0000FF, 0))

    @classmethod
    def from_rgb_float(cls, r: float, g: float, b: float):
        """Same as `from_rgb` but values are provided as percentages [0, 1]."""
        return cls.from_rgb(int(r * 0xFF), int(g * 0xFF), int(b * 0xFF))

    @classmethod
    def from_hsv(cls, hue: int, sat: int, val: int):
        """Create a Colour instance from the HSV coordinates.

        Args:
            hue: Hue
            sat: Saturation
            val: Value

        Returns:
            A new colour reflecting the provided HSV coordinates.
        """
        rgb_float = colorsys.hsv_to_rgb(hue / 0xFF, sat / 0xFF, val / 0xFF)
        return cls.from_rgb_float(*rgb_float)

    @classmethod
    def from_hls(cls, hue: int, light: int, sat: int):
        """Create a Colour instance from the HLS coordinates.

        All values should be in the closed interval [0, 255]. Invalid values
        are truncated.

        Args:
            hue: Hue.
            light: Lightness.
            sat: Saturation.

        Returns:
            A new colour reflecting the provided HLS coordinates.
        """
        rgb_float = colorsys.hls_to_rgb(hue / 0xFF, light / 0xFF, sat / 0xFF)
        return cls.from_rgb_float(*rgb_float)
