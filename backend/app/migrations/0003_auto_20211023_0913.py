# Generated by Django 3.2.8 on 2021-10-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_stack'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stack',
            options={'verbose_name': 'Stack', 'verbose_name_plural': 'stacks'},
        ),
        migrations.RemoveField(
            model_name='stack',
            name='intern',
        ),
        migrations.RemoveField(
            model_name='intern',
            name='stack',
        ),
        migrations.AddField(
            model_name='intern',
            name='stack',
            field=models.ManyToManyField(blank=True, related_name='intern_stack', to='app.Stack'),
        ),
    ]
