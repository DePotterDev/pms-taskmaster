# Generated by Django 3.0.8 on 2020-09-07 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200902_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('desc', models.CharField(blank=True, default='', max_length=300)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Project')),
            ],
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='task_group',
        ),
        migrations.RemoveField(
            model_name='task',
            name='date_due',
        ),
        migrations.RemoveField(
            model_name='task',
            name='tasks',
        ),
        migrations.AlterField(
            model_name='task',
            name='comments',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(0, 'Critical'), (1, 'Important'), (2, 'Normal'), (3, 'Low')], default=2),
        ),
        migrations.AlterField(
            model_name='task',
            name='text',
            field=models.TextField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='TaskGroup',
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='task_section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.TaskSection'),
        ),
    ]
