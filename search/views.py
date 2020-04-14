from django.http import HttpResponse


def show_time(request):
    return HttpResponse(f'Request time is: {request.current_time}')


def show_exception(request):
    raise Exception('Django middleware')

