from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Bid
from .tasks import notify_owner_new_email


@receiver(post_save, sender=Bid)
def notify_owner_of_the_new_bid(sender, instance, created, **kwargs):
    if created:
        notify_owner_new_email.delay(str(instance.bidder), str(instance.auction), instance.bid_amount)

