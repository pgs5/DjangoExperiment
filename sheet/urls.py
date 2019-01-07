from django.urls import path
from .views import SheetListView, SheetDetailView


urlpatterns = [
    path('',SheetListView.as_view(),name = 'sheet-home'),
    path('<int:pk>/',SheetDetailView.as_view(), name = 'sheet-detail')

]
