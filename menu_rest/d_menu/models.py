from django.db import models


# Модель для категорий блюд (например, закуски, основные блюда, десерты)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название категории (например, закуски)

    def __str__(self):
        return self.name


# Модель для блюд
class Dish(models.Model):
    name = models.CharField(max_length=200)  # Название блюда
    description = models.TextField()  # Описание блюда
    ingredients = models.TextField()  # Ингредиенты
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Цена блюда
    image = models.ImageField(upload_to='dishes/', blank=True, null=True)  # Фото блюда
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Категория блюда

    def __str__(self):
        return self.name
