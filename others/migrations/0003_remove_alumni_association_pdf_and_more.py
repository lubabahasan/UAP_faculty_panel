# Generated by Django 5.2 on 2025-04-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0002_alumni_association'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumni_association',
            name='pdf',
        ),
        migrations.AddField(
            model_name='alumni_association',
            name='file',
            field=models.FileField(default='pdfs/Alumni_page.pdf', upload_to='pdfs/'),
        ),
    ]
