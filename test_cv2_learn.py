"""Tests for the module name cv2_learning."""

import cv2
import numpy as np
import pprint
import cv2_learn


def test_package_info():
    """Shows package versions of the nympy and cv libs."""
    print("OpenCv: ", cv2.__version__)
    print("Numpy: ", np.__version__)


def test_read_img():
    """Reads and shows an image."""

    expected = cv2_learn.read_img("testWriteImg.jpg")
    pprint.pprint(expected)
    assert expected is True, "Something went wrong."


def test_write_img():
    """docstring"""

    expected = cv2_learn.write_img("saveImage1.jpg", "testWriteImg.jpg")
    pprint.pprint(expected)
    assert expected is True, "Saving image went wrong."


def main():
    """docstring"""

    test_read_img()
    test_write_img()
    test_package_info()


if __name__ == "__main__":
    main()
