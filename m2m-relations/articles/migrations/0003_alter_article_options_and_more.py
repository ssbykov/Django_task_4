# Generated by Django 4.0.5 on 2022-06-11 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_scope_articlescope'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterUniqueTogether(
            name='articlescope',
            unique_together={('article', 'tag')},
        ),
    ]
