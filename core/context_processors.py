from random import shuffle


def student_names(request):
    people = ["Serhii", "Andrii", "Bogdan", "Ira", "Alex", "Roman"]
    shuffle(people)
    return {"people": people}
