# Generated by Django 2.0 on 2017-12-04 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_auto_20171204_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.CharField(default='Luxx', max_length=100),
            preserve_default=False,
        ),
    ]
