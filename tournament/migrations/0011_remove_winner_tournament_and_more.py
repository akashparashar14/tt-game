# Generated by Django 4.0.6 on 2022-07-11 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0010_alter_tournament_reg_rel_tournament_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='winner',
            name='tournament',
        ),
        migrations.RemoveField(
            model_name='winner',
            name='tournament_winner',
        ),
        migrations.DeleteModel(
            name='Tournament_reg_rel',
        ),
        migrations.DeleteModel(
            name='winner',
        ),
    ]
