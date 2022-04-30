# Generated by Django 3.2.13 on 2022-04-30 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '书籍管理'},
        ),
        migrations.AddField(
            model_name='book',
            name='commentcount',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='pub_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='readcount',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterModelTable(
            name='book',
            table='Bookinfo',
        ),
    ]
