# Generated by Django 4.2.18 on 2025-01-31 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='city',
            field=models.CharField(blank=True, choices=[('Москва', 'Москва'), ('Московская область', 'Московская область')], max_length=50, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='payment_type',
            field=models.CharField(blank=True, choices=[('Наличный расчет', 'Наличный расчет'), ('Ипотека', 'Ипотека'), ('Рассрочка', 'Рассрочка')], max_length=50, null=True, verbose_name='Тип жилья'),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='target',
            field=models.CharField(blank=True, choices=[('Для проживания', 'Для проживания'), ('Инвестирования', 'Инвестирования'), ('Под сдачу', 'Под сдачу')], max_length=50, null=True, verbose_name='Цели'),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='type_of_housing',
            field=models.CharField(blank=True, choices=[('Первичное ( Новостройки )', 'Первичное ( Новостройки )'), ('Вторичное', 'Вторичное')], max_length=50, null=True, verbose_name='Тип жилья'),
        ),
    ]
