from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


monthly_challenges = {
    "january" : "Want to do something",
    "feburary" : "Not doing becuase of hoping for something to happening",
    "march"   : "Crying over things that didn't happen",
    "april"   : "Started Progressing and upgrading myself daily efficiently",
    "may"     : "Not yet Started",
    "june"     : "Not yet Started",
    "july"     : "Not yet Started",
    "august"     : "Not yet Started",
    "september"     : "Not yet Started",
    "october"     : "Not yet Started",
    "november"     : "Not yet Started",
    "december"     : "Not yet Started",

}


def monthy_challenges_number(request, month):
    month_list = list(monthly_challenges.keys())
    if month > len(month_list):
        return HttpResponseNotFound("Not Found")
    
    else:
        redirect_month = month_list[month - 1]
        redirect_path = reverse("monthly-challenges", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)



def monthy_challenges(request, month):
    challenges_month = monthly_challenges[month]

    try:
        response_data = f"<h1>{challenges_month}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("Not Found")
    

def challenges_list(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly-challenges", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)







