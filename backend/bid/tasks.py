import time
from django.core.mail import send_mail
from celery import shared_task
from django.conf import settings
from django.urls import reverse

@shared_task
def notify_owner_new_email(bidder, auction, bid_amount):
    full_link = f"http://localhost:8000{reverse('all_auctions')}"
    information_message = f"Hi, user {bidder} bids your {auction} with bid {bid_amount}"
    html_message = f"""Hi, user {bidder} bids your {auction} with bid {bid_amount}<p>View all bids here: <a href="{full_link}">{full_link}</a></p>"""
    time.sleep(10)
    try:
        send_mail(
            "New Bid Notification",
            information_message,
            settings.EMAIL_HOST_USER,
            [auction.user.email],
            html_message=html_message
        )
    except Exception as e:
        print(f"Failed to send email: {e}")