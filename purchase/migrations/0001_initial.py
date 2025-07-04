# Generated by Django 4.2.19 on 2025-05-01 13:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='order_time')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_payment_done', models.BooleanField(default=False)),
                ('price', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'verbose_name': 'purchase',
                'verbose_name_plural': 'purchases',
                'db_table': 'purchase',
            },
        ),
    ]
