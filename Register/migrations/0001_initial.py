# Generated by Django 5.1 on 2024-12-27 16:18

import django.db.models.deletion
import register.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.CharField(default=register.models.generate_unique_id, editable=False, max_length=8, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=155)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=155)),
                ('college_name', models.CharField(max_length=255)),
                ('college_id', models.CharField(max_length=25)),
                ('course', models.CharField(blank=True, max_length=155, null=True)),
                ('event', models.CharField(choices=[('CyberShow', 'CyberShow'), ('CodeGolf', 'CodeGolf'), ('PromptMatrix', 'PromptMatrix'), ('FragFest', 'FragFest'), ('ExpoRenaissance', 'ExpoRenaissance'), ('ArtBurst', 'ArtBurst'), ('MemeIfy', 'MemeIfy')], max_length=50)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FragFestDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_member_details', models.JSONField()),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.participant')),
            ],
        ),
        migrations.CreateModel(
            name='ExpoDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=155)),
                ('number_of_members', models.IntegerField()),
                ('project_detail', models.TextField()),
                ('project_detail_file', models.FileField(upload_to='uploads/expo_projects/')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.participant')),
            ],
        ),
        migrations.CreateModel(
            name='CyberShowDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=155)),
                ('number_of_members', models.IntegerField()),
                ('skit_detail_file', models.FileField(upload_to='uploads/cybershow_skits/')),
                ('participant_names', models.JSONField()),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.participant')),
            ],
        ),
    ]
