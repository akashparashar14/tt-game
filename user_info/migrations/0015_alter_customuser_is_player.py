# Generated by Django 4.0.6 on 2022-07-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0014_alter_customuser_is_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_player',
            field=models.CharField(choices=[('is_palyer', 'Is Player'), ('is_not_player', 'Is Not Player')], default='is_player', max_length=20),
        ),
    ]
