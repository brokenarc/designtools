import xml.etree.ElementTree as ET
from collections.abc import Mapping, Sequence
from typing import Any

from ._svg import (ATTRIB_ARIA, ATTRIB_CORE, ATTRIB_EVENT_DOC, ATTRIB_EVENT_DOC_ELEM,
                   ATTRIB_EVENT_GLOBAL, ATTRIB_EVENT_GRAPHIC, ATTRIB_PRESENTATION,
                   ATTRIB_PROCESSING, ATTRIB_STYLE, ELEMENTS, )

__LOWER_ELEMENTS = [e.lower() for e in ELEMENTS]


def svg_tag_guard(tag: str | ET.Element) -> str | ET.Element:
    """Raise a ``ValueError`` if ``tag`` is not a valid SVG element (ignoring case). Otherwise, return
    ``tag``."""
    name = tag.strip() if type(tag) is str else tag.tag
    if name.lower() not in __LOWER_ELEMENTS:
        raise ValueError(f"{name} is not a valid SVG element.")

    return tag


def _prep_key_name(key: str):
    """Adjusts a given key name for checking against an allowed name list. Does the following:

         - removes any leading or trailing whitespace
         - removes any leading or trailing `_` (underscore) characters
         - replaces remaining `_` (underscore) characters with `-` (dash)
         - converts to lowercase
    """
    return key.strip().strip("_").replace("_", "-").lower()


def attr_filter(allowed: Sequence[str], given: Mapping[str, str]):
    """Creates a new attribute mapping by:

        - filtering a ``given`` mapping of attributes against a list of ``allowed`` attributes
        - discards keys with a value of ``None``
        - normalizes the attribute key names against the allowed list, including replacing `_` (underscore)
          with `-` (dash).
        - converts attribute values to ``str``
    """
    allowed_map = {attrib.lower(): attrib for attrib in allowed}
    prepared = {}

    for key, value in given.items():
        prep_key = _prep_key_name(key)
        if (prep_key in allowed_map) and (value is not None):
            prepared[allowed_map[prep_key]] = str(value)

    return prepared


class SVGElement(ET.Element):
    """Subclasses Element to guard against illegal elements and filter attributes."""

    def __init__(self, **attrib: Any) -> None:
        super().__init__(
            svg_tag_guard(self.__class__._tag()),
            attr_filter(self.__class__._attr(), attrib),
        )

    @staticmethod
    def _tag() -> str:
        """Subclasses override this method to define the tag name."""
        return "none"

    @staticmethod
    def _attr() -> Sequence[str]:
        """Subclasses override this method to define allowed attributes."""
        return tuple()

    def append(self, subelement: ET.Element):
        super().append(svg_tag_guard(subelement))

    def extend(self, subelements: Sequence[ET.Element]):
        for s in subelements:
            self.append(s)


class SVG(SVGElement):
    ATTRIB = (("height", "preserveAspectRatio", "viewBox", "width", "x", "xmlns", "y")
              + ATTRIB_CORE + ATTRIB_STYLE + ATTRIB_PROCESSING + ATTRIB_EVENT_GLOBAL
              + ATTRIB_EVENT_GRAPHIC + ATTRIB_EVENT_DOC + ATTRIB_EVENT_DOC_ELEM
              + ATTRIB_PRESENTATION + ATTRIB_ARIA
              )

    @staticmethod
    def _tag() -> str:
        return "svg"

    @staticmethod
    def _attr() -> Sequence[str]:
        return SVG.ATTRIB


class Circle(SVGElement):
    ATTRIB = (
        ("cx", "cy", "r", "pathLength")
        + ATTRIB_CORE + ATTRIB_STYLE + ATTRIB_PROCESSING + ATTRIB_EVENT_GLOBAL
        + ATTRIB_EVENT_GRAPHIC + ATTRIB_PRESENTATION + ATTRIB_ARIA
    )

    @staticmethod
    def _tag() -> str:
        return "circle"

    @staticmethod
    def _attr() -> Sequence[str]:
        return Circle.ATTRIB


class Defs(SVGElement):
    ATTRIB = (
        ATTRIB_CORE + ATTRIB_STYLE + ATTRIB_EVENT_GLOBAL + ATTRIB_EVENT_GRAPHIC
        + ATTRIB_EVENT_DOC_ELEM + ATTRIB_PRESENTATION
    )

    @staticmethod
    def _tag() -> str:
        return "defs"

    @staticmethod
    def _attr() -> Sequence[str]:
        return Defs.ATTRIB


class Group(SVGElement):
    ATTRIB = (
        ATTRIB_CORE + ATTRIB_STYLE + ATTRIB_PROCESSING + ATTRIB_EVENT_GLOBAL
        + ATTRIB_EVENT_GRAPHIC + ATTRIB_PRESENTATION + ATTRIB_ARIA
    )

    @staticmethod
    def _tag() -> str:
        return "g"

    @staticmethod
    def _attr() -> Sequence[str]:
        return Group.ATTRIB


class LinearGradient(SVGElement):
    ATTRIB = (
        ("gradientUnits", "gradientTransform", "href", "spreadMethod", "x1", "x2", "y1", "y2")
        + ATTRIB_CORE + ATTRIB_STYLE + ATTRIB_EVENT_GLOBAL + ATTRIB_EVENT_DOC_ELEM
        + ATTRIB_PRESENTATION
    )

    @staticmethod
    def _tag() -> str:
        return "linearGradient"

    @staticmethod
    def _attr() -> Sequence[str]:
        return LinearGradient.ATTRIB


class RadialGradient(SVGElement):
    ATTRIB = (
        ("cx", "cy", "fr", "fx", "fy", "gradientUnits", "gradientTransform", "href", "r",
         "spreadMethod")
        + ATTRIB_CORE + ATTRIB_STYLE + ATTRIB_EVENT_GLOBAL + ATTRIB_EVENT_DOC_ELEM
        + ATTRIB_PRESENTATION
    )

    @staticmethod
    def _tag() -> str:
        return "radialGradient"

    @staticmethod
    def _attr() -> Sequence[str]:
        return RadialGradient.ATTRIB


class Rect(SVGElement):
    ATTRIB = (
        ("x", "y", "width", "height", "rx", "ry", "pathLength")
        + ATTRIB_CORE + ATTRIB_STYLE + ATTRIB_PROCESSING + ATTRIB_EVENT_GLOBAL
        + ATTRIB_EVENT_GRAPHIC + ATTRIB_PRESENTATION + ATTRIB_ARIA
    )

    @staticmethod
    def _tag() -> str:
        return "rect"

    @staticmethod
    def _attr() -> Sequence[str]:
        return Rect.ATTRIB


class Stop(SVGElement):
    ATTRIB = (
        ("offset", "stop-color", "stop-opacity")
        + ATTRIB_CORE + ATTRIB_STYLE + ATTRIB_EVENT_GLOBAL + ATTRIB_EVENT_DOC_ELEM
        + ATTRIB_PRESENTATION
    )

    @staticmethod
    def _tag() -> str:
        return "stop"

    @staticmethod
    def _attr() -> Sequence[str]:
        return Stop.ATTRIB
