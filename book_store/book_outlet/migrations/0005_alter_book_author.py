# Generated by Django 4.1.1 on 2022-09-15 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0004_author_alter_book_slug_alter_book_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="books",
                to="book_outlet.author",
            ),
        ),
    ]