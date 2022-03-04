# Generated by Django 3.1.5 on 2021-01-24 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Body_Parts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(verbose_name='Position:')),
                ('image', models.ImageField(upload_to='images/Body_Parts', verbose_name='Image')),
                ('title', models.CharField(max_length=5000, verbose_name='Title:')),
                ('text', models.TextField(max_length=5000, verbose_name='Description:')),
                ('button', models.CharField(max_length=5000, verbose_name='Button Text:')),
                ('slug', models.SlugField(max_length=5000, unique=True, verbose_name='Slug:')),
                ('status', models.BooleanField(default=False, verbose_name='Enable')),
            ],
            options={
                'verbose_name': 'Body Part',
                'verbose_name_plural': 'Body Parts',
            },
        ),
        migrations.CreateModel(
            name='Footer_Copyright',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000, verbose_name='Copyright:')),
                ('status', models.BooleanField(default=False, verbose_name='Enable')),
            ],
            options={
                'verbose_name': 'Footer Copyright',
                'verbose_name_plural': 'Footer Copyrights',
            },
        ),
        migrations.CreateModel(
            name='Footer_Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000, verbose_name='Description:')),
                ('status', models.BooleanField(default=False, verbose_name='Enable')),
            ],
            options={
                'verbose_name': 'Footer Description',
                'verbose_name_plural': 'Footer Descriptions',
            },
        ),
        migrations.CreateModel(
            name='Footer_Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/Footer_Logo', verbose_name='Image')),
                ('status', models.BooleanField(default=False, verbose_name='Enable')),
            ],
            options={
                'verbose_name': 'Footer Logo',
                'verbose_name_plural': 'Footer Logos',
            },
        ),
        migrations.CreateModel(
            name='Footer_Logo_Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000, verbose_name='Text:')),
                ('status', models.BooleanField(default=False, verbose_name='Enable')),
            ],
            options={
                'verbose_name': 'Footer Logo Text',
                'verbose_name_plural': 'Footer Logo Texts',
            },
        ),
        migrations.CreateModel(
            name='Footer_Social_Icons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(verbose_name='Position:')),
                ('name', models.CharField(max_length=5000, verbose_name='Name:')),
                ('link', models.CharField(max_length=5000, verbose_name='Page Link:')),
                ('status', models.BooleanField(default=False, verbose_name='Enable')),
            ],
            options={
                'verbose_name': 'Footer Social Icon',
                'verbose_name_plural': 'Footer Social Icons',
            },
        ),
        migrations.CreateModel(
            name='Header_Items_Left',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(verbose_name='Position:')),
                ('title', models.CharField(max_length=5000, verbose_name='Title:')),
                ('slug', models.CharField(max_length=5000, unique=True, verbose_name='Slug:')),
                ('status', models.BooleanField(default=False, verbose_name='Enable')),
            ],
            options={
                'verbose_name': 'Header Item Left',
                'verbose_name_plural': 'Header Items Left',
            },
        ),
        migrations.CreateModel(
            name='Header_Items_Right',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(verbose_name='Position:')),
                ('title', models.CharField(max_length=5000, verbose_name='Title:')),
                ('slug', models.CharField(max_length=5000, unique=True, verbose_name='Slug:')),
                ('status', models.BooleanField(default=False, verbose_name='Enable')),
            ],
            options={
                'verbose_name': 'Header Item Right',
                'verbose_name_plural': 'Header Items Right',
            },
        ),
        migrations.CreateModel(
            name='Header_Logo_Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_one', models.CharField(max_length=5000, verbose_name='Part One:')),
                ('part_two', models.CharField(max_length=5000, verbose_name='Part Two:')),
                ('slug', models.CharField(max_length=5000, unique=True, verbose_name='Slug:')),
                ('status', models.BooleanField(default=False, verbose_name='Enable')),
            ],
            options={
                'verbose_name': 'Header Logo Text',
                'verbose_name_plural': 'Header Logo Texts',
            },
        ),
        migrations.CreateModel(
            name='Footer_Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(verbose_name='Position:')),
                ('title', models.CharField(max_length=5000, verbose_name='Title:')),
                ('slug', models.SlugField(max_length=5000, unique=True, verbose_name='Slug:')),
                ('status', models.BooleanField(default=True, verbose_name='Enable')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='Home.footer_categories', verbose_name='Parent:')),
            ],
            options={
                'verbose_name': 'Footer Category',
                'verbose_name_plural': 'Footer Categories',
            },
        ),
    ]
