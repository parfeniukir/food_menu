from django.views import generic

from .models import MEAL_CATEGORY, MenuItem


class MenuItemListView(generic.ListView):
    queryset = MenuItem.objects.order_by("-date_created")
    template_name = "menu_item_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(
            **kwargs
        )  # {"menuitem_list": [{"meal_name": "Омлет", "meal_category": "breakfast"...}, {"meal_name": "Борщ"...}]}
        context["meals"] = MEAL_CATEGORY
        return context


class MenuItemDetailView(generic.DeleteView):
    model = MenuItem
    template_name = "menu_item_detail.html"
