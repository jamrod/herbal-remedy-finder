# Generated by Django 3.0.3 on 2020-02-19 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbal_remedy_finder', '0002_auto_20200218_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(default='bottles.jpg', upload_to='gallery'),
        ),
    ]
