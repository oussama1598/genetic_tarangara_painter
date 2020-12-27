import cv2
import numpy as np

from app.helpers import math


class GeneticPainter:
    def __init__(self, source_image_path, stages=1, generations=100, brush_strokes_count=10):
        self.stages = stages
        self.generations = generations
        self.brush_strokes_count = brush_strokes_count

        self.gray_image = cv2.imread(source_image_path, cv2.IMREAD_GRAYSCALE)
        self.images_history = [
            np.zeros(
                (
                    self.gray_image.shape[0],
                    self.gray_image.shape[1]
                ),
                np.uint8
            )
        ]

    def _create_sampling_mask(self, stage):
        return None

    def _calculate_brush_ranges(self, stage):
        

    def generate(self):
        for stage in range(self.stages):
            for i in range(self.generations):
                pass
