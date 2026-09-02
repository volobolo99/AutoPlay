"""Optional Ultralytics tracking adapter with a dependency-free fallback contract."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any
import numpy as np

@dataclass
class Detection:
    label: str
    confidence: float
    bbox: tuple[float, float, float, float]
    track_id: int | None = None

class UltralyticsTracker:
    def __init__(self, model_path: str, tracker: str = "botsort.yaml"):
        from ultralytics import YOLO
        self.model = YOLO(model_path)
        self.tracker = tracker

    def detect(self, frame: np.ndarray) -> list[Detection]:
        results = self.model.track(frame, persist=True, tracker=self.tracker, verbose=False)
        detections: list[Detection] = []
        for result in results:
            boxes = getattr(result, "boxes", None)
            if boxes is None:
                continue
            ids = boxes.id.int().tolist() if boxes.id is not None else [None] * len(boxes)
            for box, conf, cls, tid in zip(boxes.xyxy.tolist(), boxes.conf.tolist(), boxes.cls.int().tolist(), ids):
                detections.append(Detection(str(result.names[cls]), float(conf), tuple(map(float, box)), tid))
        return detections
