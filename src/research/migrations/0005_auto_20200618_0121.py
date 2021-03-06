# Generated by Django 3.0.7 on 2020-06-18 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0004_law_lawcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='law',
            options={'ordering': ['title'], 'verbose_name': 'Law', 'verbose_name_plural': 'Laws'},
        ),
        migrations.RemoveField(
            model_name='law',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='law',
            name='description',
        ),
        migrations.RemoveField(
            model_name='law',
            name='file',
        ),
        migrations.AddField(
            model_name='law',
            name='category',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, related_name='Law', to='research.LawCategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='law',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at'),
        ),
        migrations.AddField(
            model_name='law',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='pdf_file', verbose_name='Pdf file'),
        ),
        migrations.AddField(
            model_name='law',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AddField(
            model_name='law',
            name='views',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='law',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Title'),
        ),
    ]
