from simpleimage import SimpleImage


def red_channel(filename):
    """
    Creates an image for the given filename.
    Changes the image as follows:
    For every pixel, set green and blue values to 0
    yielding the red channel.
    Return the changed image.
    """
    image = SimpleImage(filename)
    for pixel in image:
        pixel.green = 0
        pixel.blue = 0
    return image


def darker(filename):
    """
    Makes the image darker by halving red,green,blue values.
    Returns the changed image.
    """
    # Demonstrate looping over all the pixels of an image,
    # using pixel.xxx in the loop to change each pixel,
    # int division, relative var updates.
    image = SimpleImage(filename)
    for pixel in image:
        pixel.red = pixel.red // 2
        pixel.green = pixel.green // 2
        pixel.blue = pixel.blue // 2
        # Could use += shorthand:
        # pixel.blue //= 2
    return image


def right_half(filename):
    """
    Change and return the image:
    make right half of the image
    to be 50% as bright. Use int division
    to compute where right half begins.
    Properties reminder:
      pixel.x pixel.y image.width image.height
    Also try bottom half:
      pixel.y >= image.height // 2
    """
    image = SimpleImage(filename)
    for pixel in image:
        # if pixel is in right half of image
        # (e.g. width is 100, right half begins at x=50)
        if pixel.x >= image.width // 2:
            pixel.red *= 0.5
            pixel.green *= 0.5
            pixel.blue *= 0.5
    return image


def right_quarter(filename):
    """
    As above, but do the lower right quarter.
    Use "and" to combine 2 <= tests.
    """
    image = SimpleImage(filename)
    for pixel in image:
        if (pixel.x >= image.width // 2 and
                pixel.y >= image.height // 2):
            pixel.red *= 0.5
            pixel.green *= 0.5
            pixel.blue *= 0.5
    return image


def grayscale(filename):
    """
    Change the image to be grayscale
    using the "average" technique
    and return it.
    """
    image = SimpleImage(filename)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        pixel.red = average
        pixel.green = average
        pixel.blue = average
    return image


def curb_repair1(filename):
    """
    Detect the red curb pixels, change them
    to 180/180/180 gray.
    This code does the gray setting,
    but the hurdle factor needs to be adjusted.
    Looks ok but not great.
    """
    image = SimpleImage(filename)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red >= average * 1.0:
            pixel.red = 180
            pixel.blue = 180
            pixel.green = 180
    return image


def curb_repair2(filename):
    """
    Detect the red curb pixels, change them
    to grayscale. The code here is complete:
    factor is adjusted and grayscale is in.
    This looks good!
    """
    image = SimpleImage(filename)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red >= average * 1.1:
            pixel.red = average
            pixel.blue = average
            pixel.green = average
    return image


def stop_leaves(front_filename, back_filename):
    """
    Implement stop_leaves as described.
    Detect red areas of stop sign.
    Replace red pixels with pixels from corresponding x,y
    from back image.
    """
    image = SimpleImage(front_filename)
    back = SimpleImage(back_filename)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red >= average * 1.6:
            # the key line:
            pixel_back = back.get_pixel(pixel.x, pixel.y)
            pixel.red = pixel_back.red
            pixel.green = pixel_back.green
            pixel.blue = pixel_back.blue
    return image


def main():
    """
    Run your desired photoshop functions here.
    You should save the return value of the image and then
    call .show() to visualize the output of your program.
    """
    original_poppy = SimpleImage('images/poppy.png')
    original_poppy.show()

    original_dandelion = SimpleImage('images/dandelion.png')
    original_dandelion.show()

    redder_poppy = red_channel('images/poppy.png')
    redder_poppy.show()

    darker_poppy = darker('images/poppy.png')
    darker_poppy.show()

    right_half_poppy = right_half('images/poppy.png')
    right_half_poppy.show()

    right_quarter_poppy = right_quarter('images/poppy.png')
    right_quarter_poppy.show()

    grayscale_poppy = grayscale('images/poppy.png')
    grayscale_poppy.show()

    grayscale_dandelion = grayscale('images/dandelion.png')
    grayscale_dandelion.show()

    original_curb = SimpleImage('images/curb.png')
    original_curb.show()

    curb_repair_first = curb_repair1('images/curb.png')
    curb_repair_first.show()

    curb_repair_second = curb_repair2('images/curb.png')
    curb_repair_second.show()

    original_stop = SimpleImage('images/stop.png')
    original_stop.show()

    original_leaves = SimpleImage('images/leaves.png')
    original_leaves.show()

    stop_leaves_replaced = stop_leaves('images/stop.png', 'images/leaves.png')
    stop_leaves_replaced.show()


if __name__ == '__main__':
    main()
