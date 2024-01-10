from django.http import HttpResponse
from django.shortcuts import render, redirect
import joblib

loeaded_rf_model = joblib.load("ref_model.joblib")

def index(request):
    if request.method == 'POST':
        alcohol_content = request.POST.get('acohol_content','default')
        malic_acid = request.POST.get('malic_acid', 'default')
        Ash = request.POST.get('Ash', 'default')
        alc_ash = request.POST.get('alc_ash', 'default')
        Magnesium = request.POST.get('Magnesium', 'default')
        Phenols = request.POST.get('Phenols', 'default')
        Flavanoid = request.POST.get('Flavanoid', 'default')
        NFPhelons = request.POST.get('NFPhelons', 'default')
        Cyacnins=request.POST.get('Cyacnins','default')
        Intensity=request.POST.get('Intensity','default')
        Hue=request.POST.get('Hue','default')
        OD280=request.POST.get('OD280','default')
        Proline=request.POST.get('Proline','default')

        labels = [[float(alcohol_content),
                   float(malic_acid),
                   float(Ash),
                   float(alc_ash),
                   float(Magnesium),
                   float(Phenols),
                   float(Flavanoid),
                   float(NFPhelons),
                   float(Cyacnins),
                   float(Intensity),
                   float(Hue),
                   float(OD280),
                   float(Proline),
        ]]

        our_labels = loeaded_rf_model.predict(labels)

        if our_labels[0]<= 400:
            wine_quality = "A Poor Quality Wine"
        if 400 < our_labels[0]<= 800:
            wine_quality = "A Average Quality Wine"
        if 800 < our_labels[0]<= 1200:
            wine_quality = "A Good Quality Wine"
        if 1200 < our_labels[0]<= 1500:
            wine_quality = "A Exclusive Wine"
        if our_labels[0] > 1500:
            wine_quality = "A Premium & Fresh Wine"
        
        details = {
            "answer": our_labels[0],
            "wine_quality": wine_quality,
        }

        return render(request, "results.html", details)
    
    return render(request, "index.html")