# Generated by Django 2.0.3 on 2019-11-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signuprecord', '0002_auto_20191029_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='partyname',
            name='telephone',
            field=models.CharField(default='123', max_length=11, verbose_name='手机号码'),
        ),
    ]