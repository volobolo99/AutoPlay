"""Pixel-based status-bar extraction inspired by MMORPG CV pipelines."""
from __future__ import annotations

import cv2
import numpy as np


def bar_ratio(
    image: np.ndarray,
    roi: tuple[int, int, int, int],
    color_lower: tuple[int, int, int],
    color_upper: tuple[int, int, int],
) -> float:
    """Estimate filled-bar percentage using an HSV color mask.

    ``roi`` is ``(x, y, width, height)``. This is intentionally game-agnostic;
    NosTale-specific color ranges and coordinates belong in configuration.
    """
    x, y, w, h = roi
    crop = image[y:y + h, x:x + w]
    if crop.size == 0:
        return 0.0
    hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
    lower = np.array(color_lower, dtype=np.uint8)
    upper = np.array(color_upper, dtype=np.uint8)
    mask = cv2.inRange(hsv, lower, upper)
    return float(np.count_nonzero(mask)) / float(mask.size)


def horizontal_fill(
    image: np.ndarray,
    roi: tuple[int, int, int, int],
    color_lower: tuple[int, int, int],
    color_upper: tuple[int, int, int],
    min_pixels_per_column: int = 1,
) -> float:
    """Estimate horizontal fill from the left edge of a bar."""
    x, y, w, h = roi
    crop = image[y:y + h, x:x + w]
    if crop.size == 0:
        return 0.0
    hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(
        hsv,
        np.array(color_lower, dtype=np.uint8),
        np.array(color_upper, dtype=np.uint8),
    )
    column_counts = np.count_nonzero(mask, axis=0)
    filled = column_counts >= min_pixels_per_column
    if not np.any(filled):
        return 0.0
    # Use the rightmost detected filled column to preserve a stable bar ratio.
    return float(np.flatnonzero(filled)[-1] + 1) / float(w)
