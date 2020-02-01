from datetime import datetime
from random import shuffle
from django.shortcuts import render
from core.forms import ContactUsForm


def landing_page_view(request):
    message = request.GET.get("message")

    people = ["Serhii", "Andrii", "Bogdan", "Ira", "Alex", "Roman"]
    shuffle(people)
    
    if message:
        pass

    return render(
        request,
        "landing_page.html",
        context={
            "name": "Vasyl and team",
            "now": datetime.now(),
            "message": message,
            "people": people,
        },
    )


def contact_us_view(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            print("HAPPY U! FORM IS VALID!")
            pass
    else:
        form = ContactUsForm()

    return render(request, "contact_us.html", context={
        "form": form
    })
