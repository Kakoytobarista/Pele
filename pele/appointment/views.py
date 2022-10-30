from django.shortcuts import render, redirect
from rest_framework.reverse import reverse

from appointment.utils import send_mail_custom


def index(request):
    template = 'appointment/index.html'
    if request.method == "POST" or None:
        request.session["time"] = request.POST["time"]
        return redirect(reverse("appointment:success_appointment"))
    return render(request=request,
                  template_name=template)


def success_appointment(request):
    template = 'appointment/success_appointment.html'
    send_mail_custom(request, request.session)
    return render(request=request,
                  template_name=template)
