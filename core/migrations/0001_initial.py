# Generated by Django 2.2.7 on 2019-11-05 23:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('expiry_date', models.DateTimeField()),
                ('purchase_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-expiry_date'],
            },
        ),
    ]
