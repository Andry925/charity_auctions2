from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Auction(models.Model):
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=5, decimal_places=2)
    auction_duration = models.PositiveIntegerField(
        default=0, validators=[
            MinValueValidator(1), MaxValueValidator(20)])
    image_url = models.ImageField(upload_to=upload_to, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    auto_now_add = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(default=None, null=True, blank=True)