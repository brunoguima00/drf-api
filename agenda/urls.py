from django.urls import path
from agenda.views import agendamento_detail,agendamento_list

urlpatterns = [
    path('agendamento/<int:id>/', agendamento_detail),
    path('agendamentos/', agendamento_list)
]
