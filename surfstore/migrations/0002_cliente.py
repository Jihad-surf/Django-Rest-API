# Generated by Django 4.2.7 on 2023-11-19 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surfstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('praia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='surfstore.praia')),
                ('prancha', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='surfstore.prancha')),
            ],
        ),
    ]