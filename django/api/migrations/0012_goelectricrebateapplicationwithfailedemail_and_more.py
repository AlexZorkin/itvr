# Generated by Django 4.0.1 on 2022-09-06 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_goelectricrebateapplication_approval_email_sent'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoElectricRebateApplicationWithFailedEmail',
            fields=[
            ],
            options={
                'ordering': ['-created'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('api.goelectricrebateapplication',),
        ),
        migrations.RemoveField(
            model_name='goelectricrebateapplication',
            name='approval_email_sent',
        ),
        migrations.AddField(
            model_name='goelectricrebateapplication',
            name='confirmation_email_success',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='goelectricrebateapplication',
            name='spouse_email_success',
            field=models.BooleanField(null=True),
        ),
    ]