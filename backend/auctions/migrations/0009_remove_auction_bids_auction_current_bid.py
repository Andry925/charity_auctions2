# Generated by Django 5.0.3 on 2024-04-26 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auction_is_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='bids',
        ),
        migrations.AddField(
            model_name='auction',
            name='current_bid',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]