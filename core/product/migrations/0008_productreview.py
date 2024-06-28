# Generated by Django 4.0.1 on 2022-01-27 03:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0007_vendorcategory_remove_product_subcategory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', 'Unsatisfied'), ('2', 'Below Average'), ('3', 'Average'), ('4', 'Above Average'), ('5', 'Excellent')], default='3', max_length=2)),
                ('comment', models.TextField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('verified', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productReviews', to='product.product')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productReviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
