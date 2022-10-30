from django.http import HttpResponse
from django.shortcuts import render


def page_not_found(request, exception=None):
    return HttpResponse('Error handler content', status=404)


def csrf_failure(request, reason=''):
    return render(request, 'core/403csrf.html')


def server_error(request):
    return render(request, 'core/500.html', status=500)
