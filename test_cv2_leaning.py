"""Tests for the module name cv2_learning."""

import pprint
import cv2_learning


def test_package_info():
    """Shows package versions of the nympy and cv libs."""
    print("OpenCv: ", cv2_learning.CV2_VER)
    print("Numpy: ", cv2_learning.NP_VER)
    print("MatPlotLib: ", cv2_learning.MATPLOTLIB_VER)


def test_read_img():
    """Reads and shows an image."""

    expected = cv2_learning.read_img("testWriteImg.jpg")
    pprint.pprint(expected)
    assert expected is True, "Something went wrong."


def test_write_img():
    """docstring"""

    expected = cv2_learning.write_img("saveImage1.jpg", "testWriteImg.jpg")
    print(expected)
    assert expected is True, "Saving image went wrong."


def main():
    """docstring"""

    test_read_img()
    test_write_img()
    test_package_info()


if __name__ == "__main__":
    main()
