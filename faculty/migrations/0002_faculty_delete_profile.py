# Generated by Django 5.2 on 2025-04-25 05:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='First Name', max_length=50)),
                ('last_name', models.CharField(default='Last Name', max_length=50)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=11)),
                ('bio', models.TextField(max_length=200)),
                ('about', models.TextField(max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
