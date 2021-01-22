from django.urls import path
from . import views


urlpatterns = [
    # language
    path('', views.LanguageListView.as_view(), name='language-list'),
    path('new/', views.LanguageCreateView.as_view(), name='language-create'),
    path('<int:pk>/', views.LanguageDetailView.as_view(), name='language-detail'),
    path('<int:pk>/histories/', views.language_histories, name='language-histories'),
    path('<int:pk>/update', views.LanguageUpdateView.as_view(), name='language-update'),

    # dialect
    path('<int:pk>/dialects/', views.dialect_list_view, name='dialect-list'),
    path('<int:language_pk>/dialect/<int:dialect_pk>/new/', views.dialect_create_view, name='dialect-create'),
    # path('<int:pk1>/dialect/<int:pk2>/detail', views.dialectDetailView, name='dialect-detail'),
    # path('<int:pk1>/dialect/<int:pk2>/update', views.dialectUpdateView, name='dialect-update'),
    # path('<int:pk1>/dialect/<int:pk2>/new/', views.dialectCreateView, name='dialect-create'),

]