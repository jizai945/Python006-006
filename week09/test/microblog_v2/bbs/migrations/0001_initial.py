# Generated by Django 2.2.12 on 2020-12-07 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleid', models.CharField(default='', max_length=30, verbose_name='文章id')),
                ('title', models.CharField(default='', max_length=30, verbose_name='文章标题')),
                ('article', models.CharField(default='', max_length=30, verbose_name='文章内容')),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['createtime'],
            },
        ),
    ]
