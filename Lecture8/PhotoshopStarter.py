"""
Implements some functionality of a Photoshop program!

Remember that the SimpleImage properties include:
    pixel.x pixel.y pixel.red pixel.green pixel.blue
    image.width image.height
where each SimpleImage is made up of many pixels.
"""
from simpleimage import SimpleImage


def red_channel(filename):
    """
    Given an image from `filename`, remove all
    blue and green colors from the photo to enhance
    the red channel of its pixels (the R in RGB).
    Return the updated image.
    """
    pass


def darker(filename):
    """
    Given an image from `filename`, make the image
    darker by halving its RGB values.
    Return the updated image.
    """
    pass


def right_half(filename):
    """
    Given an image from `filename`, make the
    image's right half darker by halving its RGB
    values. Return the updated image.

    Use int division to compute where right half
    begins. Also try doing the bottom half!
    """
    pass


def right_quarter(filename):
    """
    As above, but darken only the LOWER RIGHT
    quarter. Return the updated image.

    YOU TRY IT!
    """
    pass


def grayscale(filename):
    """
    Change the image to be grayscale using the
    "average" technique and return it.
    """
    pass


def curb_repair(filename):
    """
    Detect the red curb pixels and change them
    to gray.
    """
    pass


def stop_leaves(front_filename, back_filename):
    """
    Detect red areas of stop sign (`front_filename`)
    and replace them with pixels from the
    corresponding x,y of the `back_filename`.
    Return the updated image.
    """
    pass


def main():
    """
    Run your desired photoshop functions here.
    You should save the return value of the image and then
    call .show() to visualize the output of your program.
    """
    original_poppy = SimpleImage('images/poppy.png')
    original_poppy.show()

    # original_dandelion = SimpleImage('images/dandelion.png')
    # original_dandelion.show()
    #
    # original_curb = SimpleImage('images/curb.png')
    # original_curb.show()
    #
    # original_stop = SimpleImage('images/stop.png')
    # original_stop.show()
    #
    # original_leaves = SimpleImage('images/leaves.png')
    # original_leaves.show()


if __name__ == '__main__':
    main()