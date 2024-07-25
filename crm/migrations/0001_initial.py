# Generated by Django 4.2.7 on 2023-11-29 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('website', models.URLField()),
                ('designation', models.CharField(max_length=100)),
                ('task', models.TextField()),
                ('priority', models.IntegerField(default=1, help_text='Priority on a scale of 1 to 10')),
                ('handled_by', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('New', 'New'), ('Qualified', 'Qualified'), ('On Progress', 'On Progress'), ('Done', 'Done'), ('Decline', 'Decline')], max_length=20)),
            ],
        ),
    ]
