import random
import string
from django.conf import settings

SHORTENER_MIN = getattr(settings, "SHORTENER_MIN", 6)


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortener(instance, size=SHORTENER_MIN):
    new_code = code_generator(size=size)
    URLAppShortener = instance.__class__
    query_set_exists = URLAppShortener.objects.filter(
        shortener=new_code).exists()
    if query_set_exists:
        return create_shortener(size=size)
    return new_code
