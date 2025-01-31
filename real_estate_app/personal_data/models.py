from django.db import models


class PersonalData(models.Model):
    city_list = [
        ('Москва', 'Москва'),
        ('Московская область', 'Московская область'),
    ]

    target_list = [
        ('Для проживания', 'Для проживания'),
        ('Инвестирования', 'Инвестирования'),
        ('Под сдачу', 'Под сдачу'),
    ]

    type_horse_list = [
        ('Первичное ( Новостройки )', 'Первичное ( Новостройки )'),
        ('Вторичное', 'Вторичное'),
    ]

    payment_type_list = [
        ('Наличный расчет', 'Наличный расчет'),
        ('Ипотека', 'Ипотека'),
        ('Рассрочка', 'Рассрочка'),
    ]

    city = models.CharField(max_length=50 ,choices=city_list, verbose_name='Город')
    target = models.CharField(max_length=50, choices=target_list, verbose_name='Цели')
    type_of_housing = models.CharField(max_length=50,choices=type_horse_list, verbose_name='Тип жилья')
    payment_type = models.CharField(max_length=50,choices=payment_type_list, verbose_name='Тип жилья')
    full_name = models.CharField(max_length=50,verbose_name='ФИО')
    phone_number = models.CharField(max_length=50,verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкету'

    def __str__(self):
        return f'{self.city} {self.target}'
