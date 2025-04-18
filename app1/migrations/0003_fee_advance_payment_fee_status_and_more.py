# Generated by Django 5.0.7 on 2024-12-18 09:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_student_image_student_face_embedding'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='advance_payment',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='fee',
            name='status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Pending', 'Pending'), ('Partial', 'Partial')], default='Pending', max_length=10),
        ),
        migrations.AddField(
            model_name='feepayment',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('UPI', 'UPI'), ('Bank Transfer', 'Bank Transfer')], default='Cash', max_length=15),
        ),
        migrations.CreateModel(
            name='AdvancePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('fee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advance_payments', to='app1.fee')),
            ],
        ),
    ]
