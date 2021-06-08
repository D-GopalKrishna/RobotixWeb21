# Generated by Django 3.2 on 2021-05-31 16:22

from django.db import migrations, models
import extras.models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0006_auto_20210530_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diy_fyi',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=extras.models.PathAndRename2('extras/diy_fyi/img')),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='photo',
            field=models.ImageField(upload_to=extras.models.PathAndRename2('extras/gallery')),
        ),
        migrations.AlterField(
            model_name='web',
            name='img',
            field=models.ImageField(default='', upload_to=extras.models.PathAndRename('extras/webteam')),
        ),
    ]
