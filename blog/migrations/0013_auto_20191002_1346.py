# Generated by Django 2.2.6 on 2019-10-02 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190625_0930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['add_time'], 'verbose_name': '1-文章分类', 'verbose_name_plural': '1-文章分类'},
        ),
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(default=0, help_text='越大越前', verbose_name='排序'),
        ),
    ]
