"""Fast OpenCV template matching primitives for game UI elements."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np


@dataclass(frozen=True)
class Match:
    x: int
    y: int
    width: int
    height: int
    score: float

    @property
    def center(self) -> tuple[int, int]:
        return (self.x + self.width // 2, self.y + self.height // 2)


def match_template(
    image: np.ndarray,
    template: np.ndarray,
    threshold: float = 0.85,
    grayscale: bool = True,
) -> list[Match]:
    """Return non-overlapping template matches above ``threshold``.

    The implementation deliberately stays small and deterministic so it can
    be used by perception modules without introducing a stateful detector.
    """
    if grayscale:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if image.ndim == 3 else image
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY) if template.ndim == 3 else template

    ih, iw = image.shape[:2]
    th, tw = template.shape[:2]
    if th > ih or tw > iw:
        return []

    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    ys, xs = np.where(result >= threshold)
    candidates = [
        Match(int(x), int(y), tw, th, float(result[y, x]))
        for y, x in zip(ys, xs)
    ]
    candidates.sort(key=lambda m: m.score, reverse=True)

    selected: list[Match] = []
    for candidate in candidates:
        if all(_iou(candidate, other) < 0.25 for other in selected):
            selected.append(candidate)
    return selected


def load_template(path: str | Path, grayscale: bool = True) -> np.ndarray:
    flag = cv2.IMREAD_GRAYSCALE if grayscale else cv2.IMREAD_COLOR
    template = cv2.imread(str(path), flag)
    if template is None:
        raise FileNotFoundError(path)
    return template


def _iou(a: Match, b: Match) -> float:
    ax2, ay2 = a.x + a.width, a.y + a.height
    bx2, by2 = b.x + b.width, b.y + b.height
    ix1, iy1 = max(a.x, b.x), max(a.y, b.y)
    ix2, iy2 = min(ax2, bx2), min(ay2, by2)
    iw, ih = max(0, ix2 - ix1), max(0, iy2 - iy1)
    inter = iw * ih
    union = a.width * a.height + b.width * b.height - inter
    return inter / union if union else 0.0
