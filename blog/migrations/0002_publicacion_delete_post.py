# Generated by Django 5.1.3 on 2024-11-22 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', models.TextField()),
                ('autor', models.CharField(default='Anónimo', max_length=50)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]