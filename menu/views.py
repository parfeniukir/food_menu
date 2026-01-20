from django.views import generic

from .models import MenuItem


class MenuItemListView(generic.ListView):
    queryset = MenuItem.objects.order_by("-date_created")
    template_name = "menu_item_list.html"

    def get_context_data(self):
        context = {"meal": "Sandwich", "drink": "Juice"}
        return context


class MenuItemDetailView(generic.DeleteView):
    model = MenuItem
    template_name = "menu_item_detail.html"
