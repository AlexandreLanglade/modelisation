# Generated by Django 4.0.4 on 2022-04-25 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0073_journalentry_tags_custom_fields'),
        ('modelisation', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topologie',
            new_name='Topology',
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ('topology', 'name')},
        ),
        migrations.RenameField(
            model_name='member',
            old_name='topologie',
            new_name='topology',
        ),
    ]