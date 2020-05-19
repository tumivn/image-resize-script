from PIL import Image, ImageOps, ImageFont, ImageDraw
from os import listdir
from os.path import isfile, join
import ntpath


def resize(input_image, output_image, border, text):
    img = Image.open(input_image)

    # resize
    baseWidth = 2048
    wpercent = (baseWidth / float(img.size[0])) if img.size[1] < img.size[0] else baseWidth / float(img.size[1])
    wsize = baseWidth if img.size[1] < img.size[0] else int((float(img.size[0]) * float(wpercent)))
    hsize = int((float(img.size[1]) * float(wpercent))) if img.size[1] < img.size[0] else baseWidth
    img = img.resize((wsize, hsize), Image.ANTIALIAS)

    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border)

        if text:
            fontSize =30
            draw = ImageDraw.Draw(bimg)
            # font = ImageFont.truetype(<font-file>, <font-size>)
            font = ImageFont.truetype("arial.ttf", fontSize)
            ascent, descent = font.getmetrics()
            (textWidth, textBaseline), (offset_x, offset_y) = font.font.getsize(text)
            # draw.text((x, y),text,(r,g,b))
            # draw top left
            # draw.text((10, 2), text, (255, 255, 255), font=font)
            # draw bottom right
            draw.text((bimg.size[0] - textWidth - 10, bimg.size[1] - fontSize - 10), text, (255, 255, 255), font=font)
    else:
        raise RuntimeError('Border is not an integer or tuple!')

    bimg.save(output_image)


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def resize_images(input_folder, output_folder, text):
    files = [f for f in listdir(input_folder) if isfile(join(input_folder, f)) and f.endswith(".jpg")]
    for f in files:
        resize(f'{input_folder}/{f}', output_image=f'{output_folder}/{path_leaf(f)}', border=44, text=text)


if __name__ == '__main__':
    resize_images("input", "output", "© lê hoàng dũng | tumivn.com")



