# Generated by Django 3.2.5 on 2021-07-08 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_showdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='showdata',
            name='age',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
