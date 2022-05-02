from django.urls import path
from . import views

urlpatterns = [
    path('', views.family, name='family-tree'),
    path('prof-input/', views.fam_input, name='family-input'),
    # path('fam-edit/', views.fam_edit, name='family-edit'),
    # path('fam-delete/', views.fam_delete, name='family-delete'),
    path('prof-search/', views.search, name='fam-search'),
    path('prof-results/', views.search, name='fam-results'),
]
