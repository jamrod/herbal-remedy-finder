# Generated by Django 3.0.3 on 2020-02-18 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbal_remedy_finder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.TextField(blank=True, default=''),
        ),
    ]
