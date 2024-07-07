from django.shortcuts import render, HttpResponse
import pickle
import numpy as np
from django.conf import settings
import os
file_path = os.path.join(settings.BASE_DIR,'model', 'heart_predict.pkl')
with open(file_path, 'rb') as file:
    model1 = pickle.load(file)

# Create your views here.
def index (request):
    return render(request,'index.html')



    
def heart_predict(request):
    # Assuming your pickle file is located at 'path/to/your/model.pkl'
   
    # Now you can use your model object, for example, to make predictions
    # model.predict(...)
    return render(request, 'heart_predict.html')



def heart_result(request):
    
    if request.method == 'POST':    
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        cp = int(request.POST.get('cp'))
        trestbps = int(request.POST.get('trestbps'))
        chol = int(request.POST.get('chol'))
        fbs = int(request.POST.get('fbs'))
        restecg = int(request.POST.get('restecg'))
        thalach = int(request.POST.get('thalach'))
        exang = int(request.POST.get('exang'))
        oldpeak = float(request.POST.get('oldpeak'))
        slope = int(request.POST.get('slope'))
        ca = int(request.POST.get('ca'))
        thal = int(request.POST.get('thal'))
       
        heart_result = model1.predict(np.asarray([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]).reshape(1,-1))
        print("Raw prediction:", heart_result[0])
        if heart_result[0] == 1: 
            prediction = "The patient seems to have heart disease:("
        else:
            prediction = "The patient seems to be Normal:)"

        return render(request, 'heart_result.html', {'prediction1':prediction})
    else:
        # If not a POST request, you might want to show the form again or redirect
        return HttpResponse("This URL expects a POST request.")


def login(request):
    return render(request,'login.html')
