# Generated by Django 5.2 on 2025-04-27 21:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0014_faculty_linkedin_url_faculty_orcid_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
