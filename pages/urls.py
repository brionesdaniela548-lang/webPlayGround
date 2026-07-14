from django.urls import path
from .views import PageListView, PageDetailView, CreatePageView, pageUpdate, pageDeleteView

app_name = 'pages'

urlpatterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('create/', CreatePageView.as_view(), name='create'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('update/<int:pk>/', pageUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', pageDeleteView.as_view(), name='delete'),
], 'pages')
