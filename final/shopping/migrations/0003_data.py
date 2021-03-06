# Generated by Django 2.0.7 on 2018-08-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20180808_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=5, default='', max_digits=50)),
                ('img', models.ImageField(blank=True, upload_to='cart_image')),
            ],
        ),
    ]
