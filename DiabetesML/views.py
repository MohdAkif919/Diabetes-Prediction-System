from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request, 'home.html')

def result(request):
    model = joblib.load('Model.sav')

    # Define the keys for form data
    data_keys = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

    # Get form data and convert values to float
    data = [float(request.GET.get(key, 0)) for key in data_keys]

    try:
        # Make predictions
        prediction = model.predict([data])

        # Assuming your model returns a single prediction
        ans = prediction[0]

        # Pass the predicted value to the template
        return render(request, 'result.html', {'ans': ans})
    except Exception as e:
        # Handle any errors that might occur during prediction
        return HttpResponse(f"Error during prediction: {e}")
