# Generated by Django 4.0.6 on 2022-07-11 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_tournament_reg_rel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament_reg_rel',
            name='user',
        ),
    ]
