# Generated by Django 3.1 on 2020-09-20 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_read'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pk']},
        ),
    ]
