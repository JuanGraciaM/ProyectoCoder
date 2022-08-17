from django.shortcuts import render
from AppCoder.models import Familia

# Create your views here.
def entrega(request):
    flia= Familia.objects.all()
    return render(request, "index.html", {"familia":flia})