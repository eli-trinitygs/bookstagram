""" Bookstagram views """
#Django
from django.http import HttpResponse
#Utilities
from datetime import datetime

#objeto request
def hello_world(request):
    """Return a greeting """
    return HttpResponse('Oh, hi ! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %h:%M hrs')
    ))

def hi(request):
    import pdb; pdb.set_trace()
# def hi(request):
#     """Hi."""
#     numbers = request.GET['numbers']
#     return HttpResponse(str(numbers))