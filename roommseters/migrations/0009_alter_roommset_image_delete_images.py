# Generated by Django 4.1.7 on 2023-03-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roommseters', '0008_alter_roommset_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommset',
            name='image',
            field=models.ImageField(upload_to='propery/'),
        ),
        migrations.DeleteModel(
            name='images',
        ),
    ]
