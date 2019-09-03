# Generated by Django 2.1.5 on 2019-09-02 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190902_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='myapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('tag', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=120)),
            ],
        ),
        migrations.DeleteModel(
            name='blog_posts',
        ),
    ]
