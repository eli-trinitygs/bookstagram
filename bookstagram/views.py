""" Bookstagram views """
#Django
from django.http import HttpResponse
#Utilities
from datetime import datetime
import json
#objeto request
def hello_world(request):
    """Return a greeting """
    return HttpResponse('Oh, hi ! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %h:%M hrs')
    ))

# def hi(request):
#     import pdb; pdb.set_trace()
#     return HttpResponse('Hola ke aze!')

def sort_integers(request):
    """Hi."""
    # numbers = request.GET['numbers']
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    #crar diccionario
    data = {
        'status': 'ok',
        'numbers': 'sorte_ints',
        'message': 'Integers sorted successfully!'
    }
    # import pdb; pdb.set_trace()
    # return HttpResponse(str(numbers), content_type = 'application/json')
    #implementando metodo json.dumps para traducir un diccionario a json
    return HttpResponse(json.dumps(data,indent=4), 
    content_type = 'application/json'
    )

def say_hi(request, name, age):
    #return a greeting
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}!!! Welcome to Bookstagram :)'.format(name)
    return HttpResponse(message) 

