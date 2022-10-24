from django.shortcuts import render


def index(request):
    template = 'appointment/index.html'
    return render(request=request,
                  template_name=template)
