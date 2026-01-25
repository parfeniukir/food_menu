from django.urls import path

from menu import views

urlpatterns = [
    path("", views.MenuItemListView.as_view(), name="home"),
    path("item/<int:pk>/", views.MenuItemDetailView.as_view(), name="menu_item")
]
