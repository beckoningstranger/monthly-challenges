from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    # month is set in urls.py
    match month:
        case('january'):
            challenge_text = "Eat no meat for the entire month!"
        case('february'):
            challenge_text = "Walk for at least 20 minutes every day!"
        case('march'):
            challenge_text = "Learn Django for at least 20 minutes every day!"
        case _:
            challenge_text = "Month not implemented yet!"

    return HttpResponse(challenge_text)
