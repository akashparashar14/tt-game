# Generated by Django 4.0.6 on 2022-07-11 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament_reg_rel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ManyToManyField(to='user_auth.profile')),
            ],
        ),
    ]
