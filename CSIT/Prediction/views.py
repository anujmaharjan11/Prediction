import pickle
import sklearn
import joblib
from django.shortcuts import render, redirect


def predict(request):
    if request.method == 'POST':
        Id = request.POST['s_id']
        print('my id: ', Id)
        assignment = request.POST['assignment']
        attendance = request.POST['attendance']
        first = request.POST['first']
        gender = request.POST['gender']
        second = request.POST['second']
        third = request.POST['third']

        fields = [Id, gender, assignment, attendance, first, second, third]

        if not None in fields:
            # Data preprocessing Convert the values to float, int
            Id = int(Id)
            assignment = int(assignment)
            attendance = int(attendance)
            first = float(first)
            second = float(second)
            third = float(third)
            gender = int(gender)

        results = [Id, assignment, attendance, first, second, third, gender]
        # path = './MLmodel/11chemistry.pkl'
        # model = pickle.load(open(path, 'rb'))

        with open('./Prediction/11biology.pkl', 'rb') as file:
            model = pickle.load(file)

        final = model.predict([results])[0]

        context = {'final': final}
        return render(request, 'Prediction/predict.html', context)

    return render(request, 'Prediction/predict.html')


def result(request):
    return render(request, "Prediction/result.html")
