from django.contrib.auth.models import User
from django.db import models


MEAL_CATEGORY = (
    ("breakfast", "Сніданки"),
    ("main_course", "Основні страви"),
    ("salad", "Салати"),
    ("dessert", "Десерти"),
    ("beverage", "Напої"),
)

STATUS_CHOISES = (
    (True, "Доступний"),
    (False, "Недоступний"),
)

# class Categoty(models.Model):
#     name = models.CharField(max_length=30, unique=True)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name


class MenuItem(models.Model):
    meal_name = models.CharField(max_length=1000, unique=True)
    meal_description = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    meal_category = models.CharField(max_length=30, choices=MEAL_CATEGORY)
    # meal_category_id = models.ForeignKey(Categoty, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True, choices=STATUS_CHOISES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal_name

# ZZ94jQyJsknLH