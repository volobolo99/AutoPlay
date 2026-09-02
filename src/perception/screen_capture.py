"""Cross-platform baseline capture. A Windows Graphics Capture adapter can replace this."""
from __future__ import annotations
from time import monotonic
import numpy as np
from perception.interfaces import CaptureBackend, Frame

class MSSCapture(CaptureBackend):
    def __init__(self, monitor: int | dict = 1):
        self.monitor = monitor
        self._sct = None

    def capture(self) -> Frame:
        if self._sct is None:
            import mss
            self._sct = mss.mss()
        shot = np.asarray(self._sct.grab(self.monitor))[:, :, :3]
        return Frame(image=shot, timestamp=monotonic(), source="mss")
