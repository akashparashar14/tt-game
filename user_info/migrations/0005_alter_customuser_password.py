# Generated by Django 4.0.6 on 2022-07-12 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0004_alter_customuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.IntegerField(),
        ),
    ]
