from PIL import Image


def load_image(image_file):

    image = Image.open(image_file).convert("RGB")

    return image