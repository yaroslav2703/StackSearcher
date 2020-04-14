from django.http import HttpResponse


def showtime(request):
    raise Exception('Django middleware')
    #return HttpResponse(f'Request time is: {request.current_time}')
