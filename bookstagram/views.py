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

def hi(request):
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