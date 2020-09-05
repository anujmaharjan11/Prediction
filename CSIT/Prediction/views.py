import pickle
import sklearn
import joblib
from django.shortcuts import render, redirect


def predict(request):
    if request.method == "POST":
        Id = request.POST['s_id']
        assignment = request.POST['assignment']
        attendance = request.POST['attendance']
        first = request.POST['third']
        gender = request.POST['first']
        second = request.POST['second']
        third = request.POST['gender']

        fields = [Id, gender, assignment, attendance, first, second, third]

        if not None in fields:
            # Datapreprocessing Convert the values to float, int
            Id = int(Id)
            assignment = int(assignment)
            attendance = int(attendance)
            first = float(first)
            second = float(second)
            third = float(third)
            gender = int(gender)

            result = [Id, assignment, attendance, first, second, third, gender]

            path = './MLmodel/11chemistry.pkl'
            model = pickle.load(open(path, 'rb'))

            final = model.predict([result])[0]
            # print(final)
            #
            # PredResults.objects.create(s_id=Id, gender=gender, assignment=assignment,
            #                            attendance=attendance, first=first, second=second,
            #                            third=third, final=final)

            context = {'final': final}
            return render(request, 'Prediction/predict.html', context)

    return render(request, 'Prediction/predict.html')


def result(request):
    return render(request, "Prediction/result.html")
