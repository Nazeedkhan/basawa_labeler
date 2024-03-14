from django.db import models

# Create your models here.
class First_qr_code_table(models.Model):
    qrcode=models.CharField(max_length=200)
    field1=models.CharField(max_length=200)
    value1=models.CharField(max_length=200)
    field2=models.CharField(max_length=200)
    value2=models.CharField(max_length=200)
    field3=models.CharField(max_length=200)
    value3=models.CharField(max_length=200)

    class Meta:
        db_table = 'first_qr_code_table'

class Second_qr_code_table(models.Model):
    qrcode=models.CharField(max_length=200)
    field1=models.CharField(max_length=200)
    value1=models.CharField(max_length=200)
    field2=models.CharField(max_length=200)
    value2=models.CharField(max_length=200)
    field3=models.CharField(max_length=200)
    value3=models.CharField(max_length=200)

    class Meta:
        db_table = 'second_qr_code_table'

class First_bar_code_table(models.Model):
    qrcode=models.CharField(max_length=200)
    field1=models.CharField(max_length=200)
    value1=models.CharField(max_length=200)
    field2=models.CharField(max_length=200)
    value2=models.CharField(max_length=200)
    field3=models.CharField(max_length=200)
    value3=models.CharField(max_length=200)

    class Meta:
        db_table = 'first_bar_code_table'

class Second_bar_code_table(models.Model):
    qrcode=models.CharField(max_length=200)
    field1=models.CharField(max_length=200)
    value1=models.CharField(max_length=200)
    field2=models.CharField(max_length=200)
    value2=models.CharField(max_length=200)
    field3=models.CharField(max_length=200)
    value3=models.CharField(max_length=200)

    class Meta:
        db_table = 'second_bar_code_table'

class First_no_code_table(models.Model):
    qrcode=models.CharField(max_length=200)
    field1=models.CharField(max_length=200)
    value1=models.CharField(max_length=200)
    field2=models.CharField(max_length=200)
    value2=models.CharField(max_length=200)
    field3=models.CharField(max_length=200)
    value3=models.CharField(max_length=200)
    field4=models.CharField(max_length=200)
    value4=models.CharField(max_length=200)

    class Meta:
        db_table = 'first_no_code_table'

class Second_no_code_table(models.Model):
    qrcode=models.CharField(max_length=200)
    field1=models.CharField(max_length=200)
    value1=models.CharField(max_length=200)
    field2=models.CharField(max_length=200)
    value2=models.CharField(max_length=200)
    field3=models.CharField(max_length=200)
    value3=models.CharField(max_length=200)

    class Meta:
        db_table = 'second_no_code_table'