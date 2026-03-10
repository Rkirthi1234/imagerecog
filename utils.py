from PIL import Image, ImageFilter
import io


def load_image(image_file) -> Image.Image:

    image = Image.open(image_file).convert("RGB")

    # Resize if too large (keeps aspect ratio)
    max_size = 1024
    if max(image.size) > max_size:
        image.thumbnail((max_size, max_size), Image.LANCZOS)

    # Mild sharpening to improve captioning accuracy
    image = image.filter(ImageFilter.SHARPEN)

    return image


def image_to_bytes(image: Image.Image) -> bytes:
    buf = io.BytesIO()
    image.save(buf, format="JPEG", quality=95)
    return buf.getvalue()