# Generated by Django 4.0.5 on 2022-07-07 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0006_alter_blog_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=1000)),
            ],
        ),
    ]