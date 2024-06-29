from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from django.conf import settings
from .models import Auction


@receiver(post_save, sender=Auction)
def clear_cache_after_auction_creation(instance, created, **kwargs):
    if created:
        cache.delete(settings.AUCTION_CACHE_NAME)
