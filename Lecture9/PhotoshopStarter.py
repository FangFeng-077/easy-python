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
    image = SimpleImage(filename)
    for pixel in image:
        pixel.blue = 0
        pixel.green = 0
    return image


def darker(filename):
    """
    Given an image from `filename`, make the image
    darker by halving its RGB values.
    Return the updated image.
    """
    image = SimpleImage(filename)
    for pixel in image:
        pixel.green = pixel.green // 2
        pixel.blue = pixel.blue // 2
        pixel.red = pixel.red // 2
    return image


def right_half(filename):
    """
    Given an image from `filename`, make the
    image's right half darker by halving its RGB
    values. Return the updated image.

    Use int division to compute where right half
    begins. Also try doing the bottom half!
    """
    image = SimpleImage(filename)
    for pixel in image:
        if pixel.x >= image.width // 2:
            pixel.green = pixel.green // 2
            pixel.blue = pixel.blue // 2
            pixel.red = pixel.red // 2
    return image


def right_quarter(filename):
    """
    As above, but darken only the LOWER RIGHT
    quarter. Return the updated image.

    YOU TRY IT!
    """
    image = SimpleImage(filename)
    for pixel in image:
        if (pixel.x >= image.width // 2 and
                pixel.y >= image.height // 2):
            pixel.green = pixel.green // 2
            pixel.blue = pixel.blue // 2
            pixel.red = pixel.red // 2
    return image


def grayscale(filename):
    """
    Change the image to be grayscale using the
    "average" technique and return it.
    """
    image = SimpleImage(filename)
    for pixel in image:
        average = (pixel.red + pixel.blue + pixel.green) // 3
        pixel.green = average
        pixel.blue = average
        pixel.red = average
    return image


def curb_repair(filename):
    """
    Detect the red curb pixels and change them
    to gray.
    """
    image = SimpleImage(filename)
    for pixel in image:
        average = (pixel.red + pixel.blue + pixel.green) // 3
        if pixel.red >= average * 1.1:
            pixel.green = average
            pixel.blue = average
            pixel.red = average
    return image


def stop_leaves(front_filename, back_filename):
    """
    Detect red areas of stop sign (`front_filename`)
    and replace them with pixels from the
    corresponding x,y of the `back_filename`.
    Return the updated image.
    """
    pass


def mirror(filename):
    """
    Copy the original image
    to the right half of "out", but as a horizontally reversed
    mirror image. So the left half is a regular copy,
    and the right half is a mirror image.
    """
    pass


def shrink(filename):
    """
    Create a new "out" image half the width and height
    of the original.
    Set pixels at x=0 1 2 3 in out, from x=0 2 4 6 in original,
    and likewise in the y direction.
    """
    image = SimpleImage(filename)   # the original image
    out = SimpleImage.blank(image.width // 2, image.height // 2)
    # NOTE: we're looping x,y over out, not original
    for y in range(out.height):
        for x in range(out.width):
            pixel_out = out.get_pixel(x, y)
            # your code here
            pass
    return out


def flip_horizontal(filename):
    pass


def main():
    """
    Run your desired photoshop functions here.
    You should save the return value of the image and then
    call .show() to visualize the output of your program.
    """
    # original_poppy = SimpleImage('images/poppy.png')
    # original_poppy.show()
    #
    # red_poppy = red_channel('images/poppy.png')
    # red_poppy.show()
    #
    # dark_poppy = darker('images/poppy.png')
    # dark_poppy.show()
    #
    # original_dandelion = SimpleImage('images/dandelion.png')
    # original_dandelion.show()
    #
    # dark_half_dandelion = right_half('images/dandelion.png')
    # dark_half_dandelion.show()
    #
    # dark_quarter_dandelion = right_quarter('images/dandelion.png')
    # dark_quarter_dandelion.show()
    #
    # gray_dandelion = grayscale('images/dandelion.png')
    # gray_dandelion.show()
    #
    # original_curb = SimpleImage('images/curb.png')
    # original_curb.show()
    #
    # new_curb = curb_repair('images/curb.png')
    # new_curb.show()
    #
    original_stop = SimpleImage('images/stop.png')
    original_stop.show()

    original_leaves = SimpleImage('images/leaves.png')
    original_leaves.show()


if __name__ == '__main__':
    main()