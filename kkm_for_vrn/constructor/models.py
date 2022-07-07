from unicodedata import name
from django.db import models

# Create your models here.
'''Примерная структура моделей:
1 Автостанция a. Наименование (строка)
b.Город (Строка)
c.Регион (Строка)
2Перевозчик
a.Наименование (строка)
b.ИНН
3 Маршрут
a.Наименование (Строка)
b.Номер маршрута (строка)
c.Станция отправления (FK на автостанцию)
d.Станция прибытия (FK на автостанцию)
4 Рейс
a. Дата отправления (Дата с временем)
b.Даты прибытия (Дата с временем)
c.Маршрут (FK на маршрут)
d.Платформа (число)
e. Перевозчик (FK на перевозчика)
5 Билет 
a.ФИО пассажира
b.Рейс (FK на рейс)
cНомер билета (строка)
d.Номер места (число)
e. Вид билета (перечисление – взрослый / детский)'''


class Autostation(models.Model):

    name = models.TextField()
    city = models.TextField()
    region = models.TextField()

    def __str__(self):
        return f'{self.name} ({self.city})'

class Carrier(models.Model):

    name = models.TextField()
    inn = models.PositiveBigIntegerField()
    #region = models.TextField()
    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.TextField()
    departure_number = models.PositiveIntegerField()
    autostation_from = models.ForeignKey("Autostation", on_delete=models.SET_NULL, null=True, related_name='autostation_from')
    autostation_to = models.ForeignKey("Autostation", on_delete=models.SET_NULL, null=True, related_name='autostation_to')
    def __str__(self):
        return self.name

class Flight(models.Model):

    departure_date = models.DateField()
    arrival_date = models.DateField()
    route = models.ForeignKey("Route", on_delete=models.SET_NULL, null=True)
    platform = models.PositiveIntegerField()
    carrier = models.ForeignKey("Carrier", on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.route} ({self.departure_date} - {self.arrival_date})'

class Ticket(models.Model): 
    ADULT = 'взрослый'
    CHILDREN = 'детский'
    TYPE_CHOICES = [
        (ADULT, 'взрослый'),
        (CHILDREN, 'детский')
    ]

        
    passenger_name = models.TextField()
    flight = models.ForeignKey("Flight", on_delete=models.SET_NULL, null=True)
    ticket_number = models.TextField()
    ticket_place = models.PositiveIntegerField()
    ticket_type = models.TextField(choices = TYPE_CHOICES, default = ADULT)
    def __str__(self):
        fio = '{"ФИО":"'+f'{self.passenger_name}'+'", '
        fly = '"Рейс":"'+f'{self.flight}'+'",'
        tn = '"Номер билета":"'+f'{self.ticket_number}'+'",'
        tp = '"Номер места":"'+f'{self.ticket_place}'+'",'
        tpl = '"Тип билета":"'+f'{self.ticket_type}'+'"}'
        out = fio+fly+tn+tp+tpl
        return out#f'ФИО пассажира: {self.passenger_name}; Рейс: ({self.flight}); Номер билета: {self.ticket_number}; Номер места: {self.ticket_place}; Тип билета: {self.ticket_type};'
