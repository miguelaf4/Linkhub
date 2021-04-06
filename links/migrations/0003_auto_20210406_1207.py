# Generated by Django 3.2 on 2021-04-06 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_auto_20210406_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('link', models.URLField()),
                ('image', models.ImageField(upload_to='links')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='LinkModel',
        ),
    ]