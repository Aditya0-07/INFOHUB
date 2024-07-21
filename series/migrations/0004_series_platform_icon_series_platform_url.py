# Generated by Django 5.0.6 on 2024-07-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0003_alter_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='platform_icon',
            field=models.ImageField(default='allinall/static/images/Bad Boys Poster.jpeg', upload_to='icons/'),
        ),
        migrations.AddField(
            model_name='series',
            name='platform_url',
            field=models.URLField(default='soohan.uni'),
        ),
    ]