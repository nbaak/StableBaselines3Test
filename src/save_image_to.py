
from typing import List
from PIL import Image
import numpy as np


def save_image_to(frame, filename="frame.png"):
    im = Image.fromarray(frame)
    im.save(filename)


def save_images_as_animation(frames: List[np.ndarray], filename: str = "video.gif", duration: int = 10, loop: int = 1) -> None:
    def frame_generator():
        for frame in frames:
            yield Image.fromarray(frame)

    first_frame = next(frame_generator())  # Get the first frame
    first_frame.save(
        filename,
        save_all=True,
        append_images=frame_generator(),  # Use generator instead of list
        duration=duration,
        loop=loop
    )
