# Generated by Django 4.1.7 on 2023-03-13 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import nftprod.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('cover', models.FileField(upload_to=nftprod.models.get_collection_media_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('symbol', models.CharField(max_length=10)),
                ('decimals', models.IntegerField(default=18)),
                ('contract', models.CharField(max_length=42, unique=True)),
                ('usd_value', models.DecimalField(decimal_places=2, default=1, max_digits=8)),
                ('eur_value', models.DecimalField(decimal_places=2, default=1, max_digits=8)),
                ('try_value', models.DecimalField(decimal_places=2, default=1, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('extension', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NFT',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('token_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('price_amount', models.DecimalField(decimal_places=16, max_digits=18)),
                ('latest_bid', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('metadata', models.JSONField(blank=True)),
                ('auction_date', models.DateTimeField(blank=True, null=True)),
                ('bit_count', models.PositiveIntegerField(default=0)),
                ('highest_bid', models.DecimalField(blank=True, decimal_places=16, max_digits=18, null=True)),
                ('level', models.CharField(default='beginner', max_length=20)),
                ('language', models.CharField(default='english', max_length=50)),
                ('rating', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SaleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owned_at', models.DateTimeField(auto_now_add=True)),
                ('price_amount', models.DecimalField(decimal_places=16, max_digits=18)),
                ('nft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ownerships', to='nftprod.nft')),
                ('price_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nftprod.currency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nft_ownership', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NFTMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_file', models.FileField(upload_to=nftprod.models.get_media_path)),
                ('url', models.URLField(blank=True, null=True)),
                ('media_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nftprod.mediatype')),
            ],
        ),
        migrations.AddField(
            model_name='nft',
            name='authors',
            field=models.ManyToManyField(related_name='authors_nft', through='nftprod.Ownership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='nft',
            name='categories',
            field=models.ManyToManyField(to='nftprod.category'),
        ),
        migrations.AddField(
            model_name='nft',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nftprod.collection'),
        ),
        migrations.AddField(
            model_name='nft',
            name='media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_nft', to='nftprod.nftmedia'),
        ),
        migrations.AddField(
            model_name='nft',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_nft', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='nft',
            name='price_currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nftprod.currency'),
        ),
        migrations.AddField(
            model_name='nft',
            name='properties',
            field=models.ManyToManyField(blank=True, to='nftprod.property'),
        ),
        migrations.AddField(
            model_name='nft',
            name='sale_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='saletype_nft', to='nftprod.saletype'),
        ),
        migrations.AddField(
            model_name='nft',
            name='tags',
            field=models.ManyToManyField(blank=True, to='nftprod.tag'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_date', models.DateTimeField(auto_now_add=True)),
                ('nft', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='like', to='nftprod.nft')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price_amount', models.DecimalField(decimal_places=16, max_digits=18)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('nft', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history', to='nftprod.nft')),
                ('price_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nftprod.currency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_amount', models.DecimalField(decimal_places=16, max_digits=18)),
                ('bid_date', models.DateTimeField(auto_now_add=True)),
                ('nft', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bid', to='nftprod.nft')),
                ('price_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nftprod.currency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids_ownership', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
