# Generated by Django 4.0.1 on 2022-02-15 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0008_alter_vendorreview_vendor_alter_vendorreview_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='address1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address Line 1'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='address2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address Line 2'),
        ),
    ]
