# Generated by Django 5.1.4 on 2024-12-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(default=' ', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Motive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('logo', models.ImageField(upload_to='')),
                ('motive_type', models.CharField(choices=[('Social Cause', 'Social Cause'), ('Environmental', 'Environmental'), ('Educational', 'Educational'), ('Medical', 'Medical'), ('Charity', 'Charity'), ('Other', 'Other')], default='Social Cause', max_length=50)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]