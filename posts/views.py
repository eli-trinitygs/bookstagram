"""Posts views """
#Django
from django.http import HttpResponse

#diccionario de datos


# Create your views here.
def list_posts(request):
    """list existing posts"""
    post = [1, 2, 4]
    return HttpResponse(str(post))
