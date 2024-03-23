# Generated by Django 4.1.2 on 2024-03-22 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.TextField(max_length=225)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='about')),
            ],
            options={
                'verbose_name': 'about-me',
                'verbose_name_plural': 'about-me',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='client-name')),
                ('description', models.TextField(verbose_name='client-description')),
                ('image', models.ImageField(default='default.png', upload_to='clients')),
            ],
        ),
        migrations.CreateModel(
            name='RecentWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Work-title')),
                ('image', models.ImageField(upload_to='works')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='service-name')),
                ('description', models.TextField(verbose_name='about-service')),
            ],
        ),
    ]