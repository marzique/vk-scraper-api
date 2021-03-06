# Generated by Django 3.1.1 on 2020-09-08 22:14

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=django.db.models.fields.DateTimeField)),
                ('content', models.TextField(blank=True)),
                ('posted', models.BooleanField(default=False)),
            ],
        ),
    ]
