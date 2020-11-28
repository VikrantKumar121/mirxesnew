# Generated by Django 3.0.6 on 2020-09-09 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GnC', '0007_auto_20200817_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competencies',
            name='board_comments',
            field=models.TextField(default='NIL', max_length=2000),
        ),
        migrations.AlterField(
            model_name='competencies',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='competencies',
            name='manager_comments',
            field=models.TextField(default='NIL', max_length=2000),
        ),
        migrations.AlterField(
            model_name='competencies',
            name='summary',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='competencies',
            name='user_comments',
            field=models.TextField(default='NIL', max_length=2000),
        ),
        migrations.AlterField(
            model_name='competency_category',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='competency_comment',
            name='comments',
            field=models.TextField(max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='departmental_competencies',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='departmental_competencies',
            name='summary',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='departmental_competencies_comment',
            name='comments',
            field=models.TextField(max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='departmental_goal_comment',
            name='comments',
            field=models.TextField(max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='departmental_goals',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='departmental_goals',
            name='summary',
            field=models.TextField(max_length=70),
        ),
        migrations.AlterField(
            model_name='goal_comment',
            name='comments',
            field=models.TextField(max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='goals',
            name='MID_manager_comments',
            field=models.TextField(default='NIL', max_length=2000),
        ),
        migrations.AlterField(
            model_name='goals',
            name='MID_user_comments',
            field=models.TextField(default='NIL', max_length=2000),
        ),
        migrations.AlterField(
            model_name='goals',
            name='board_comments',
            field=models.TextField(default='NIL', max_length=2000),
        ),
        migrations.AlterField(
            model_name='goals',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='goals',
            name='manager_comments',
            field=models.TextField(default='NIL', max_length=2000),
        ),
        migrations.AlterField(
            model_name='goals',
            name='metrics_Used',
            field=models.TextField(default='NIL', max_length=100),
        ),
        migrations.AlterField(
            model_name='goals',
            name='summary',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='goals',
            name='tracking_status',
            field=models.TextField(choices=[('null', 'null'), ('On Track', 'On Track'), ('Not On Track', 'Not On Track')], default='null', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='goals',
            name='user_comments',
            field=models.TextField(default='NIL', max_length=2000),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='progress',
            field=models.CharField(choices=[('Working', 'Working'), ('Completed', 'Completed')], default='Working', max_length=50),
        ),
    ]