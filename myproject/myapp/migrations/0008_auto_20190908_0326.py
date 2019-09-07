# Generated by Django 2.1.5 on 2019-09-08 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20190907_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_db',
            name='c_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myapp.Board_DB'),
        ),
        migrations.AlterField(
            model_name='comment_db',
            name='c_writer',
            field=models.CharField(default='익명', max_length=10),
        ),
    ]
