# Generated by Django 3.0.8 on 2020-08-21 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_auto_20200820_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ques', to='mainpage.Question'),
        ),
    ]