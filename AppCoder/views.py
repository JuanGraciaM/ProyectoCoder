from django.shortcuts import render
from AppCoder.models import Familia, Comentario

# Create your views here.
def entrega(request):
    flia= Familia.objects.all()
    if request.method == "POST":
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        mensaje = request.POST["mensaje"]
        obj = Comentario(nombre=nombre, apellido=apellido, comentario=mensaje)
        obj.save()
        mensaje="Gracias por tu comentario"
        return render(request, "index.html",{"familia":flia, "mensaje":mensaje})
    return render(request, "index.html", {"familia":flia})