# Generated by Django 4.1.7 on 2023-03-14 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nftprod', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nft',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
