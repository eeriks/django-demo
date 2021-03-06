# Generated by Django 2.2 on 2022-04-27 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RelatedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('some_field', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='ChildModel',
            fields=[
                ('parentmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.ParentModel')),
                ('some_field', models.CharField(max_length=12)),
            ],
            bases=('app.parentmodel',),
        ),
        migrations.AddField(
            model_name='parentmodel',
            name='one_to_one_relation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.RelatedModel'),
        ),
    ]
