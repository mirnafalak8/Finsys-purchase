# Generated by Django 4.2.1 on 2023-10-04 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_vendor_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='comments',
        ),
    ]
