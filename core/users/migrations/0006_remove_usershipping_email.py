# Generated by Django 4.0.1 on 2022-02-03 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_created_profile_date_updated_usershipping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usershipping',
            name='email',
        ),
    ]
