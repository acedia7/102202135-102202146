# Generated by Django 4.2.16 on 2024-10-08 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_is_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_id',
            field=models.CharField(max_length=10),
        ),
    ]
