"""This module is used to learn the OpenCV library."""

import pathlib
import cv2
import numpy as np


def display_image(image_path: str, display_img: bool = True) -> bool:
    """A function that opens an image."""

    if pathlib.Path(image_path).exists():
        img = cv2.imread(image_path)
        if display_img:
            cv2.imshow("myImage", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return True


def set_image_grayscale(image_path: str, show_img: bool = False) -> cv2.Mat:
    """A function that sets an image to grayscale.

    Args:
        image_path: The path to the image.
        show_img: Whether to show the image.
    Returns:
        The image in grayscale.
    Example:
        >>> set_image_grayscale("image.jpg")
        <cv2.Mat object>
        >>> set_image_grayscale("image.jpg", True)
        <cv2.Mat object>
        >>> set_image_grayscale("image.jpg", False)
        <cv2.Mat object>
        >>> set_image_grayscale("image.jpg", True)
        <cv2.Mat object>
    """

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Could not read the image.")
        return None
    if show_img:
        cv2.imshow("myImage", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image


def resize_image(
    image_path: str,
    width: int,
    height: int,
    show_img: bool = False,
) -> cv2.Mat:
    """A function that resizes an image.

    Args:
        image_path: The path to the image.
        width: The width of the image.
        height: The height of the image.
        show_img: Whether to show the image.
    Returns:
        The resized image.
    Example:
        >>> resize_image("image.jpg", 100, 100)
        <cv2.Mat object>
        >>> resize_image("image.jpg", 100, 100, True)
        <cv2.Mat object>
        >>> resize_image("image.jpg", 100, 100, False)
        <cv2.Mat object>
        >>> resize_image("image.jpg", 100, 100, True)
        <cv2.Mat object>
    """

    img = cv2.imread(image_path)
    if img is None:
        print("Could not read the image.")
        return False
    resize_image = cv2.resize(img, (width, height))
    if show_img:
        cv2.imshow("myImage", resize_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return resize_image


def resize_by_multiplier(
    image_path: str,
    multiplier: float,
    show_img: bool = False,
) -> cv2.Mat:
    """A function that resizes an im age by a multiplier.

    Args:
        image_path: The path to the image.
        multiplier: The multiplier to resize the image.
        show_img: Whether to show the image.
    Returns:
        The resized image.
    Example:
        >>> resize_by_multiplier("image.jpg", 0.5)
        <cv2.Mat object>
        >>> resize_by_multiplier("image.jpg", 0.5, True)
        <cv2.Mat object>
        >>> resize_by_multiplier("image.jpg", 0.5, False)
        <cv2.Mat object>
        >>> resize_by_multiplier("image.jpg", 0.5, True)
        <cv2.Mat object>
    """

    image = cv2.imread(image_path)
    if image is None:
        print("Could not read the image.")
        return False
    resize_image = cv2.resize(image, None, fx=multiplier, fy=multiplier)
    if show_img:
        cv2.imshow("myImage", resize_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return resize_image


def flip_image(
    image_path: str,
    flip_code: int = 0,
    show_img: bool = False,
) -> cv2.Mat:
    """A function that flips an image.

    Args:
        image_path: The path to the image.
        flip_code: The code to flip the image.
        show_img: Whether to show the image.
    Returns:
        The flipped image.
    Example:
        >>> flip_image("image.jpg", 0)
        <cv2.Mat object>
        >>> flip_image("image.jpg", 0, True)
        <cv2.Mat object>
        >>> flip_image("image.jpg", 0, False)
        <cv2.Mat object>
        >>> flip_image("image.jpg", 0, True)
        <cv2.Mat object>
    """

    img = cv2.imread(image_path)
    if img is None:
        print("Could not read the image.")
        return False
    flip_image = cv2.flip(img, flip_code)

    if show_img:
        cv2.imshow("myImage", flip_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return flip_image


def save_image(
    image_path: str,
    image: cv2.Mat,
    show_img: bool = False,
) -> cv2.Mat:
    """A function that saves an image.

    Args:
        image_path: The path to the image.
        image: The image to save.
        show_img: Whether to show the image.
    Returns:
        The saved image.
    Example:
        >>> save_image("image.jpg", image)
        <cv2.Mat object>
        >>> save_image("image.jpg", image, True)
        <cv2.Mat object>
        >>> save_image("image.jpg", image, False)
        <cv2.Mat object>
        >>> save_image("image.jpg", image, True)
        <cv2.Mat object>
    """

    cv2.imwrite(image_path, image)
    if show_img:
        cv2.imshow("myImage", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image


def change_rgb_intercatively(image_path: str) -> cv2.Mat:
    """A function that changes the RGB of an image interactively.

    Args:
        image_path: The path to the image.
    Returns:
        The image with the changed RGB.
    Example:
        >>> change_rgb_intercatively("image.jpg")
        <cv2.Mat object>
        >>> change_rgb_intercatively("image.jpg", True)
        <cv2.Mat object>
        >>> change_rgb_intercatively("image.jpg", False)
        <cv2.Mat object>
        >>> change_rgb_intercatively("image.jpg", True)
        <cv2.Mat object>
    """

    # Create a window.
    cv2.namedWindow("MyWindow")

    # Create a var that will contain the fill color.
    fill_value = np.array([255, 255, 255], np.uint8)

    # Add an auxiliary function to call from each trackbar_callback function.
    def _trackbar_callback(idx, value):
        fill_value[idx] = value

    # Add trackers into the window.
    cv2.createTrackbar("R", "MyWindow", 255, 255, lambda v: _trackbar_callback(2, v))
    cv2.createTrackbar("G", "MyWindow", 255, 255, lambda v: _trackbar_callback(1, v))
    cv2.createTrackbar("B", "MyWindow", 255, 255, lambda v: _trackbar_callback(0, v))

    # Create an event loop.
    while True:
        image = np.full((500, 500, 3), fill_value)
        cv2.imshow("MyWindow", image)
        key = cv2.waitKey(27)
        if key == 27:
            break
    cv2.destroyAllWindows()
    return image


def main():
    """The main function."""

    display_image("image.jpg")
    display_image("image1.jpg")
    # set_image_grayscale("image1.jpg")
    # resize_image("image.jpg", 100, 100)
    # resize_by_multiplier("image.jpg", 0.5)
    # flip_image("image.jpg", -1)

    # Save image.
    # flipped_image = flip_image("image.jpg", -1)
    # save_image("image_flipped.jpg", flipped_image)
    # # display_image("image_flipped.jpg")


if __name__ == "__main__":
    main()
