from django.views import generic

from .models import MEAL_CATEGORY, MenuItem


class MenuItemListView(generic.ListView):
    """
    MenuItemListView - клас-представлення для відображення списку елементів меню.

    - Наслідується від generic.ListView, що дозволяє автоматично обробляти запити на отримання списку об'єктів.
    - queryset: визначає набір даних, який буде відображатися, впорядкований за датою створення у спадному порядку.
    - template_name: вказує на шаблон, який використовується для рендерингу сторінки зі списком елементів меню.

    Методи:
        get_context_data(self, **kwargs):
            - Перевизначає стандартний метод для додавання додаткових даних у контекст шаблону.
            - Додає до контексту список категорій страв (MEAL_CATEGORY) під ключем "meals".
            - Повертає розширений контекст для використання у шаблоні.

    Призначення:
        Даний клас використовується для відображення сторінки зі списком страв меню, а також для передачі додаткової інформації про категорії страв у шаблон.
    """
    queryset = MenuItem.objects.order_by("-date_created")
    template_name = "menu_item_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(
            **kwargs
        )  # {"menuitem_list": [{"meal_name": "Омлет", "meal_category": "breakfast"...}, {"meal_name": "Борщ"...}]}
        context["meals"] = MEAL_CATEGORY
        return context


class MenuItemDetailView(generic.DetailView):
    model = MenuItem
    template_name = "menu_item_detail.html"
