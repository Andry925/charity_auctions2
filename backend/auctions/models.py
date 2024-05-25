from django.db import models
from datetime import datetime, timedelta
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Auction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='auctions')
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=5, decimal_places=2)
    auction_duration = models.PositiveIntegerField(
        default=0, validators=[
            MinValueValidator(1), MaxValueValidator(20)])
    current_bid = models.IntegerField(default=0, null=True, blank=True)
    image_url = models.ImageField(
        upload_to=upload_to,
        null=True,
        blank=True,
        max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(default=None, null=True, blank=True)
    is_finished = models.BooleanField(default=False, blank=True)

    def save(self, *args, **kwargs):
        self.expires_at = self.calculate_expired_at()
        super().save(*args, **kwargs)

    def calculate_expired_at(self):
        self.created_at = datetime.now()
        expire_data = self.created_at +\
            timedelta(days=self.auction_duration)
        return expire_data

    def __str__(self):
        return self.description
