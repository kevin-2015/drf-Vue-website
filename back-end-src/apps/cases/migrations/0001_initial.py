# Generated by Django 2.0 on 2017-12-06 11:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='暂无标题', max_length=50, verbose_name='标题')),
                ('hyperlink', models.CharField(default='/index', max_length=200, verbose_name='超链接地址')),
                ('image', models.ImageField(upload_to='banner', verbose_name='轮播图片')),
                ('index', models.IntegerField(default=0, verbose_name='轮播顺序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '首页轮播图',
                'verbose_name_plural': '首页轮播图',
            },
        ),
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='案例名')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('fav_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('reply_num', models.IntegerField(default=0, verbose_name='回复数')),
                ('cases_brief', models.TextField(max_length=500, verbose_name='案例简短描述')),
                ('cases_desc', models.TextField(max_length=50000, verbose_name='案例正文内容')),
                ('cases_front_image', models.CharField(default='/static/image/fail.jpg', max_length=200, verbose_name='封面图URL')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '案例',
                'verbose_name_plural': '案例',
            },
        ),
        migrations.CreateModel(
            name='CasesCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='类别名', max_length=30, verbose_name='类别名')),
                ('code', models.CharField(default='', help_text='类别code', max_length=30, verbose_name='类别code')),
                ('desc', models.TextField(default='', help_text='类别描述', verbose_name='类别描述')),
                ('category_type', models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目')], help_text='类目级别', verbose_name='类目级别')),
                ('is_tab', models.BooleanField(default=False, help_text='是否导航', verbose_name='是否导航')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('parent_category', models.ForeignKey(blank=True, help_text='父目录', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_cat', to='cases.CasesCategory', verbose_name='父类目级别')),
            ],
            options={
                'verbose_name': '案例类别',
                'verbose_name_plural': '案例类别',
            },
        ),
        migrations.CreateModel(
            name='CasesImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('cases', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='cases.Cases', verbose_name='案例')),
            ],
            options={
                'verbose_name': '案例图片',
                'verbose_name_plural': '案例图片',
            },
        ),
        migrations.CreateModel(
            name='HotSearchWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(default='', max_length=20, verbose_name='热搜词')),
                ('index', models.IntegerField(default=0, verbose_name='排序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '热搜词',
                'verbose_name_plural': '热搜词',
            },
        ),
        migrations.AddField(
            model_name='cases',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.CasesCategory', verbose_name='案例类目'),
        ),
    ]