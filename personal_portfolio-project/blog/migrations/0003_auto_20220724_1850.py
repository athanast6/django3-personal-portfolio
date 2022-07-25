# Generated by Django 3.2.14 on 2022-07-24 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default=1, upload_to='blog/images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
