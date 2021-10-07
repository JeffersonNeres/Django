from django.shortcuts import render
from .models import FilmesFavorito

# create your views here
def homepage(request):
    return render(
                    request=request,
                    template_name="home.html",
                    context={"Filmes": FilmesFavorito.objects.all}
                )
