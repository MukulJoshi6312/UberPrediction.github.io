from django.shortcuts import render
import os
import pickle

# Create your views here.
def index(request):
    return render(request,"index.html")

def test(request):
    ppw = int(request.POST['ppw'])
    pn = int(request.POST['pn'])
    mi = int(request.POST['mi'])
    appm = int(request.POST['appm'])
    path = os.path.dirname(__file__)
    model = pickle.load(open(os.path.join(path,'taxi.pkl'),'rb'))
    result = str(model.predict([[ppw,pn,mi,appm]])[0].round(2))
    return  render(request,"index.html",{'result':result})