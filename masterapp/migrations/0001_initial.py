# Generated by Django 5.0.7 on 2024-07-25 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(null=True, upload_to=None)),
                ('under_parrent', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('agent_id', models.CharField(max_length=50, null=True)),
                ('branch_name', models.CharField(max_length=50, null=True)),
                ('aria_name', models.CharField(max_length=50, null=True)),
                ('representive', models.CharField(max_length=50, null=True)),
                ('supervisor', models.CharField(max_length=50, null=True)),
                ('group', models.CharField(max_length=255)),
                ('terms', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('address', models.TextField()),
                ('pan', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('linkid', models.CharField(max_length=255)),
                ('customer_type', models.CharField(max_length=255)),
                ('account_no', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='customer_group_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_under_group', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_group_id', models.CharField(max_length=50)),
                ('customer_group_name', models.CharField(max_length=50)),
                ('customer_account_id', models.CharField(max_length=50)),
                ('customer_parrent', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='item_group_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_under_group', models.CharField(max_length=50)),
                ('groupid', models.CharField(max_length=50)),
                ('item_group_name', models.CharField(max_length=50)),
                ('item_nature', models.CharField(max_length=50)),
                ('undergroup', models.CharField(blank=True, default='primary', max_length=100, null=True)),
                ('group_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='item_setup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iteam_image', models.ImageField(null=True, upload_to=None)),
                ('select_group', models.CharField(max_length=50, null=True)),
                ('unit_choice', models.CharField(max_length=50, null=True)),
                ('alt_unit', models.CharField(max_length=50, null=True)),
                ('item_name', models.CharField(max_length=50, null=True)),
                ('barcode', models.CharField(max_length=50, null=True)),
                ('item_code', models.CharField(max_length=50, null=True)),
                ('hs_code', models.CharField(max_length=50, null=True)),
                ('cost_price', models.CharField(max_length=50, null=True)),
                ('sales_rate', models.CharField(max_length=50, null=True)),
                ('enable_non_tax', models.BooleanField(null=True, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='ledger_setup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(blank=True, max_length=100, null=True)),
                ('nature', models.CharField(max_length=100)),
                ('account_name', models.CharField(blank=True, max_length=100, null=True)),
                ('account_number', models.CharField(blank=True, max_length=100, null=True)),
                ('branch', models.CharField(blank=True, max_length=100, null=True)),
                ('cheque_no', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(blank=True, null=True, upload_to='')),
                ('group', models.CharField(blank=True, max_length=50, null=True)),
                ('terms_condition', models.TextField(blank=True, null=True)),
                ('supplier_category', models.CharField(blank=True, max_length=255, null=True)),
                ('supplier_type', models.CharField(blank=True, max_length=255, null=True)),
                ('under_parent', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('pan', models.CharField(blank=True, max_length=255, null=True)),
                ('account_number', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('link_account_id', models.CharField(blank=True, max_length=255, null=True)),
                ('link_agent_id', models.CharField(blank=True, max_length=255, null=True)),
                ('branch_name', models.CharField(blank=True, max_length=255, null=True)),
                ('aria_name', models.CharField(blank=True, max_length=255, null=True)),
                ('representative', models.CharField(blank=True, max_length=255, null=True)),
                ('supervisor', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_under_group', models.CharField(blank=True, max_length=50, null=True)),
                ('supplier_group_id', models.CharField(blank=True, max_length=50, null=True)),
                ('supplier_group_name', models.CharField(blank=True, max_length=50, null=True)),
                ('supplier_account_id', models.CharField(blank=True, max_length=50, null=True)),
                ('supplier_parrent', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='unit_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=50)),
                ('unit_symbol', models.CharField(max_length=50)),
                ('unit_extra', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userroles', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('allowWebAccess', models.CharField(max_length=50)),
            ],
        ),
    ]