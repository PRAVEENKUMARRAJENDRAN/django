from django.urls import path
from . import views


urlpatterns = [
    path("", views.challenges_list),
    path("<int:month>", views.monthy_challenges_number),
    path("<str:month>", views.monthy_challenges, name= "monthly-challenges")
]