from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('view/<int:id>',views.view),
]
