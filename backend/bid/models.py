from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Bid(models.Model):
    bidder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bids')
    bid_amount = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[
            MinValueValidator(0.1)])
    bid_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.bid_amount}'
