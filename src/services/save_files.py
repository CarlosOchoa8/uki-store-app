import mimetypes
import os

import slugify
from wtforms import MultipleFileField

from config2.statics import static


def save_files_to_static(category: str, upload_files: MultipleFileField) -> str:
    """Save images in their folders name and create if dond exists."""
    valid_image_types = [
        "image/jpeg",
        "image/jpg",
        "image/png",
        "image/svg+xml",
        "application/pdf"
    ]
    try:
        product_files = []
        for upload_file in upload_files:
            if upload_file:
                file_type = mimetypes.guess_type(upload_file.filename)[0]
                if file_type not in valid_image_types:
                    Exception("Exception")
                if not os.path.exists(f"{static}products/{category}"):
                    print("No existe")
                    os.makedirs(f"{static}products/{category}")
                directory_path = (
                    f"{static}/products/{category}/"
                    )
                content = upload_file.read()
                image_extension = os.path.splitext(upload_file.filename)[1]
                image_name = os.path.splitext(upload_file.filename)[0]
                slugified_filename = slugify.slugify(image_name)
                product_files.append(f"{slugified_filename}{image_extension}")
                with open(
                        f"{directory_path}{slugified_filename}{image_extension}", "wb"
                ) as f:
                    f.write(content)
        return product_files
        # return f"{slugified_filename}{image_extension}"
    except Exception as e:
        raise TypeError(f"Error: {str(e)}") from e
