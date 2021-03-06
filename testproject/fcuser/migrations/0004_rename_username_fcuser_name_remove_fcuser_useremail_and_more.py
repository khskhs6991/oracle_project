# Generated by Django 4.0.2 on 2022-02-09 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0003_fcuser_useremail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fcuser',
            old_name='username',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='fcuser',
            name='useremail',
        ),
        migrations.AddField(
            model_name='fcuser',
            name='phonenumber',
            field=models.IntegerField(default=0, verbose_name='사용자번호'),
            preserve_default=False,
        ),
    ]
