# Generated by Django 3.1.7 on 2021-09-06 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'cash'), ('bkash', 'bkash'), ('nagad', 'nagad'), ('upay', 'upay'), ('card', 'card'), ('others', 'others')], default='cash', max_length=100),
        ),
    ]