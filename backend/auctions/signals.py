from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Auction

@receiver(post_save, sender=Auction)
@receiver(post_delete, sender=Auction)
def clear_cache_after_auction_change(instance, **kwargs):
    cache.clear()