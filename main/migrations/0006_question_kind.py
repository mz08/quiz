# Generated by Django 4.1.5 on 2024-04-23 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_quizresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='kind',
            field=models.CharField(choices=[('WV', 'С вариантами ответа'), ('TF', 'Поле ввода')], default='WV', max_length=2),
        ),
    ]