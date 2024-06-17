from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.urls import reverse
from django.dispatch import receiver
from django.conf import settings
from .models import Bid


@receiver(post_save, sender=Bid)
def notify_owner_of_the_new_bid(sender, instance, created, **kwargs):
    if created:
        full_link = f"http://localhost:8000{reverse('all_auctions')}"
        auction_owner_email = instance.auction.user.email
        information_message = f"Hi, user {instance.bidder} bids your {instance.auction} with bid {instance.bid_amount}"
        html_message = f"""Hi, user {instance.bidder} bids your {instance.auction} with bid {instance.bid_amount}<p>View all bids here: <a href="{full_link}">{full_link}</a></p>
        """
        send_mail(
            "New Bid Notification",
            f"{information_message} ",
            settings.EMAIL_HOST_USER,
            [auction_owner_email],
            html_message=html_message
        )
