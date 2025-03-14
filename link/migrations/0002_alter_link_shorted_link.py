# Generated by Django 5.1.7 on 2025-03-14 10:49

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("link", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="link",
            name="shorted_link",
            field=autoslug.fields.AutoSlugField(
                editable=False, populate_from="user__username", unique=True
            ),
        ),
    ]
