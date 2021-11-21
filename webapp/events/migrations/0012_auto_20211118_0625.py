# Generated by Django 3.2 on 2021-11-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20211117_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='body',
            field=models.CharField(blank=True, help_text='Enter valid GitHub markdown.\n            Upload event images at the bottom of the page, and tag them\n            in markdown like so:\n            <pre>\n             ![alt text](img1)    # img1 will be replaced with the real URI\n             ...\n             ![alt text](img2) </pre>\n             ', max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='external',
            field=models.URLField(blank=True, help_text='Link to external content. Users will be directed here instead of the post page, so use instead of body.', null=True),
        ),
    ]
