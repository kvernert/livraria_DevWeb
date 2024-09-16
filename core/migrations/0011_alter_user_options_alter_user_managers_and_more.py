# Generated by Django 5.0.2 on 2024-09-16 14:01

import core.models.user
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_rename_autor_livro_autores"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "Usuário", "verbose_name_plural": "Usuários"},
        ),
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", core.models.user.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="passage_id",
            field=models.CharField(
                default=uuid.UUID("1bad1322-a398-4efb-8dbc-06987e7de56f"),
                help_text="Passage ID",
                max_length=255,
                unique=True,
                verbose_name="passage_id",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(help_text="Email", max_length=255, unique=True, verbose_name="email"),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True, help_text="Indica que este usuário está ativo.", verbose_name="Usuário está ativo"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Indica que este usuário pode acessar o Admin.",
                verbose_name="Usuário é da equipe",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(blank=True, help_text="Username", max_length=255, null=True, verbose_name="name"),
        ),
    ]
