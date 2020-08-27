# Generated by Django 3.0.6 on 2020-08-02 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20200801_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_id',
        ),
        migrations.AlterField(
            model_name='bid',
            name='item_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Item'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='user_detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.User'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.User'),
        ),
        migrations.AlterField(
            model_name='message',
            name='to_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.User'),
        ),
        migrations.AlterField(
            model_name='sold_item',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
