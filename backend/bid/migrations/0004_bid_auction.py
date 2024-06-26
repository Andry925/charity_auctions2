# Generated by Django 5.0.3 on 2024-04-26 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_remove_auction_bids_auction_current_bid'),
        ('bid', '0003_alter_bid_bidder'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='auction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.auction'),
        ),
    ]
