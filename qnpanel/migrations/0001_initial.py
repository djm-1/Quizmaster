# Generated by Django 3.0.6 on 2020-05-20 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(default='')),
                ('option_1', models.CharField(default='', max_length=300)),
                ('option_2', models.CharField(default='', max_length=300)),
                ('option_3', models.CharField(default='', max_length=300)),
                ('option_4', models.CharField(default='', max_length=300)),
                ('answer', models.CharField(default='', max_length=300)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]