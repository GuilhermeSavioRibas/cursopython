# Generated by Django 4.0.4 on 2022-05-30 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_contato_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/'),
        ),
    ]