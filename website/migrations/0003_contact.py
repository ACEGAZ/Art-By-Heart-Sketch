# Generated by Django 3.2.14 on 2022-07-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_add_art_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254,)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]