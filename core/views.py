from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
    produtos = Product.objects.all()
    html = """
    <html>
      <body>
        <h1>Sejam bem vindos!!!</h1>
      </body>
    </html>
    """
    return HttpResponse(html)
