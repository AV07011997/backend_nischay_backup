# Generated by Django 4.1.4 on 2023-01-05 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_alter_upload_file_details_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='bureau_account_segment_tl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RECORD_ID', models.CharField(max_length=20)),
                ('BUREAU_ID', models.CharField(max_length=20)),
                ('CUSTOMER_ID', models.CharField(max_length=20)),
                ('ACCOUNT_HD_SEGMENT', models.CharField(max_length=20)),
                ('REPORTER_SHORT_NAME', models.CharField(max_length=20)),
                ('AC_RPT_MEMBER_NAME', models.CharField(default=' ', max_length=20, null=True)),
                ('ACCOUNT_NUMBER', models.CharField(max_length=20)),
                ('ACCOUNT_TYPE', models.CharField(max_length=20)),
                ('OWNERSHIP_INDICATOR', models.CharField(max_length=20)),
                ('DATE_AC_DISBURSED', models.DateField(max_length=20)),
                ('DATE_LAST_PAYMENT', models.DateField(null=True)),
                ('DATE_CLOSED', models.DateField(null=True)),
                ('DATE_REPORTED_CERTIFIED', models.CharField(max_length=20)),
                ('HIGH_CREDIT_AMOUNT', models.CharField(max_length=20)),
                ('CURRENT_BALANCE', models.CharField(max_length=20)),
                ('AMOUNT_OVER_DUE', models.CharField(max_length=20)),
                ('PAYMENT_HST_1', models.CharField(max_length=20, null=True)),
                ('PAYMENT_HST_2', models.CharField(max_length=20)),
                ('DATE_PAYMENT_HST_START', models.DateField()),
                ('DATE_PAYMENT_HST_END', models.DateField()),
                ('SUIT_FILED', models.CharField(max_length=20, null=True)),
                ('WRITTEN_OFF_STATUS', models.CharField(max_length=20, null=True)),
                ('TYPE_OF_COLLATERAL', models.CharField(max_length=20, null=True)),
                ('VALUE_OF_COLLATERAL', models.CharField(max_length=20, null=True)),
                ('CREDIT_LIMIT', models.CharField(max_length=20, null=True)),
                ('CASH_LIMIT', models.CharField(max_length=20, null=True)),
                ('RATE_OF_INTEREST', models.CharField(max_length=20, null=True)),
                ('REPAYMENT_TENURE', models.CharField(max_length=20, null=True)),
                ('EMI_AMMOUNT', models.CharField(max_length=20, null=True)),
                ('WRITEN_OFF_AMOUNT', models.CharField(max_length=20, null=True)),
                ('WRITTEN_OFF_AMOUNT_TOTAL', models.CharField(max_length=20, null=True)),
                ('WRITTEN_OFF_AMOUNT_PRINCIPAL', models.CharField(max_length=20, null=True)),
                ('SETTLEMENT_AMOUNT', models.CharField(max_length=20, null=True)),
                ('PAYMENT_FREQUENCY', models.CharField(max_length=20, null=True)),
                ('ACTUAL_AMOUNT_PAYMENT', models.CharField(max_length=20, null=True)),
                ('DATE_ENTRY_ERROR_CODE', models.CharField(max_length=20, null=True)),
                ('ERROR_CODE', models.CharField(max_length=20, null=True)),
                ('DATE_BUREAU_REMARK_CODE', models.CharField(max_length=20, null=True)),
                ('ACCOUNT_HEADER_COUNT', models.CharField(max_length=20, null=True)),
                ('source', models.CharField(max_length=20)),
                ('final_selected', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='customer_allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lid', models.CharField(max_length=20)),
                ('did', models.CharField(max_length=20)),
                ('cid', models.CharField(max_length=20)),
                ('identifier', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
