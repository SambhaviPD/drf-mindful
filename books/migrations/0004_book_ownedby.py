# Generated by Django 4.0.5 on 2022-08-08 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_alter_author_name_remove_book_author_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ownedBy',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
