# Generated by Django 2.0.2 on 2019-06-22 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190623_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text_body',
            field=models.TextField(max_length=20000),
        ),
    ]
