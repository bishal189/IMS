# Generated by Django 5.0.7 on 2024-07-25 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bank_payment_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_p_voucher_number', models.CharField(max_length=50)),
                ('b_p_ledger_name', models.CharField(max_length=50)),
                ('b_p_voucher_date', models.CharField(max_length=50)),
                ('b_p_voucher_miti', models.CharField(max_length=50)),
                ('b_p_toprow_amount', models.CharField(max_length=50)),
                ('b_p_collectedby', models.CharField(max_length=50)),
                ('b_p_drcr', models.CharField(max_length=50)),
                ('b_p_remarks', models.CharField(max_length=50)),
                ('b_p_particular', models.CharField(max_length=50)),
                ('b_table_drcr', models.CharField(max_length=50)),
                ('b_p_table_amount', models.CharField(max_length=50)),
                ('b_p_cheque_no', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='payment_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_voucher_number', models.CharField(max_length=50, null=True)),
                ('p_bankacc', models.CharField(max_length=50, null=True)),
                ('p_voucher_date', models.DateField(null=True)),
                ('p_amount_top', models.CharField(max_length=50, null=True)),
                ('p_voucher_miti', models.CharField(max_length=50, null=True)),
                ('p_drcr', models.CharField(max_length=50, null=True)),
                ('p_remarks', models.CharField(max_length=50, null=True)),
                ('p_particular', models.CharField(max_length=50, null=True)),
                ('p_total', models.CharField(max_length=50, null=True)),
                ('p_collected_by', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
