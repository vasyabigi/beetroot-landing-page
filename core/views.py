from datetime import datetime

from django.shortcuts import render
from core.forms import ContactUsForm


def landing_page_view(request):
    message = request.GET.get("message")

    if message:
        pass

    return render(
        request,
        "landing_page.html",
        context={
            "name": "Vasyl and team",
            "now": datetime.now(),
            "message": message,
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


def privat_page_view(request):
    return render(request, "privat.html")
