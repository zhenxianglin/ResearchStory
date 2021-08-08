from django.core.exceptions import ValidationError


def file_size(value):
    filesize = value.size

    if filesize > 104857600:
        raise ValidationError("maximum size is 100 mb")
