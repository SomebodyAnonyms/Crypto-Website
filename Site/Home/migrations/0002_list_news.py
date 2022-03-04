# Generated by Django 3.1.5 on 2021-01-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='List_News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(verbose_name='Position:')),
                ('image', models.ImageField(upload_to='images/List_News', verbose_name='Image')),
                ('title', models.CharField(max_length=5000, verbose_name='Title:')),
                ('text', models.TextField(max_length=5000, verbose_name='Description:')),
                ('slug', models.SlugField(max_length=5000, unique=True, verbose_name='Slug:')),
                ('status', models.BooleanField(default=False, verbose_name='Enable')),
            ],
            options={
                'verbose_name': 'List News',
                'verbose_name_plural': 'List News',
            },
        ),
    ]
