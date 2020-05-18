# Generated by Django 3.0.3 on 2020-04-18 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200418_1310'),
    ]

    def insert_role(apps, schema_editor):
        Role = apps.get_model('app', 'Role')
        roles = ['admin', 'mentee', 'mentor']
        for role in roles:
            role = Role(role=role)
            role.save()

    operations = [
        migrations.RunPython(insert_role),
    ]
