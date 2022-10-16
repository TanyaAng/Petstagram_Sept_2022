from django.core.exceptions import ValidationError


def convert_MB_to_binary_bytes(value):
    return value*1024*1024

def max_file_size_validator_to_5MB(file):
    limit = 5
    if file.size > convert_MB_to_binary_bytes(limit):
        raise ValidationError('The maximum file size that can be uploaded is 5MB.')
