from pydantic import BaseModel, validator
from PIL import Image
from io import BytesIO


class ImageModel(BaseModel):
    data: bytes

    @validator("data")
    def validate_image_format(cls, v: bytes) -> bytes:
        try:
            im = Image.open(BytesIO(v))
            fmt = im.format
            im.verify()
            im.close()
            allowed = ("JPEG", "PNG")
            if fmt not in allowed:
                raise ValueError(f"unsupported image format: {fmt}")
        except Exception as e:
            raise ValueError(f"invalid image: {e}")
        return v
