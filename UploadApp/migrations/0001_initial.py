# Generated by Django 3.1.7 on 2021-03-29 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(blank=True, max_length=255)),
                ('docfile', models.FileField(null=True, upload_to='documents/%Y/%m/%d')),
            ],
        ),
    ]
