from django.urls import path
from . import views

urlpatterns = [
    # if path can be converted to an integer, call one function, if not, another
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge)
]
