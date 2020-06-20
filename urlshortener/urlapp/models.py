from django.db import models
from django.utils import timezone
from .utils import code_generator, create_shortener


class URLAppManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(URLAppManager, self).all(*args, **kwargs)
        # we can also update this default or we can create specific filter
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortener(self):
        qs = URLAppShortener.objects.filter(
            id__gte=1)  # this is literly every items
        new_codes = 0
        for q in qs:
            q.shortener = create_shortener(q)
            print(q.shortener)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)


class URLAppShortener(models.Model):
    url = models.CharField(max_length=250, )
    shortener = models.CharField(max_length=15, unique=True, blank=True)
    # everytime the model is saved
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(
        default=timezone.now)  # when the model was created
    active = models.BooleanField(default=True)

    objects = URLAppManager()
    # some_random = URLAppManager()

    def save(self, *args, **kwargs):
        if self.shortener is None or self.shortener == "":
            self.shortener = create_shortener(self)
        super(URLAppShortener, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
