# Generated by Django 5.0.1 on 2024-02-01 09:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClothApp', '0005_contact'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('postcode', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=250)),
                ('amount', models.CharField(max_length=250)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
