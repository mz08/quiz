# Generated by Django 4.1.5 on 2024-04-28 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_question_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correct',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]