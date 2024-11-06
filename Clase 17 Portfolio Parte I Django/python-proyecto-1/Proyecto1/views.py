from django.http import HttpResponse
from datetime import date
# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context


def otra_vista(request):
    return HttpResponse("<h1>¡Esto es un título!</h1><p>Y este es un párrafo.</p>")

def saludo(request):
    return HttpResponse("Chanchito Feliz")

def segunda_vista(request):
    return HttpResponse("Segunda vista actualizada")


def dia_de_hoy(request):
    hoy = date.today()
    return HttpResponse(f"Hoy es {hoy}")

def muestra_nombre(self, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a Curso")


def probando_template(request):

    # Abrimos el archivo html
    mi_html = open('./Proyecto1/plantillas/index.html')

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    mi_contexto = Context()

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)