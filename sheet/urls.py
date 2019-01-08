from django.urls import path
from .views import SheetListView, SheetDetailView, SheetCreateView, SheetUpdateView, SheetDeleteView


urlpatterns = [
    path('',SheetListView.as_view(),name = 'sheet-home'),
    path('<int:pk>/',SheetDetailView.as_view(), name = 'sheet-detail'),
    path('create/', SheetCreateView.as_view(), name = 'sheet-create'),
    path('<int:pk>/update/',SheetUpdateView.as_view(), name = 'sheet-update'),
    path('<int:pk>/delete/', SheetDeleteView.as_view(), name = 'sheet-delete')
]
