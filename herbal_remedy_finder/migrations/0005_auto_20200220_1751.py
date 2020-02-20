# Generated by Django 3.0.3 on 2020-02-20 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbal_remedy_finder', '0004_auto_20200220_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('info', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='info',
        ),
    ]
