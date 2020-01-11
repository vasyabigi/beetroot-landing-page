from random import shuffle
from datetime import datetime

from django.shortcuts import render


def landing_page_view(request):
    message = request.GET.get("message")

    if message:
        pass

    students = ["Serhii", "Andrii", "Bogdan", "Ira", "Alex", "Roman"]
    shuffle(students)

    return render(
        request,
        "landing_page.html",
        context={
            "name": "Vasyl",
            "now": datetime.now(),
            "students": students,
            "message": message,
        },
    )
