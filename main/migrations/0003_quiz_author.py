# Generated by Django 4.1.2 on 2022-11-18 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.user'),
            preserve_default=False,
        ),
    ]
