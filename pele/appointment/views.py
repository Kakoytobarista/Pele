import json
import uuid

import logging

from django.shortcuts import render, redirect
from rest_framework.reverse import reverse

from appointment.utils import send_mail_custom
from users.models import User


def index(request):
    template = 'appointment/index.html'
    if request.method == "POST" or None:
        name, date, time, email = request.POST["name"], \
                                  request.POST["date"], \
                                  request.POST["time"], \
                                  request.POST["email"]
        uuid_ = str(uuid.uuid4())
        request.session["name"] = request.POST["name"]
        request.session["token"] = json.dumps(uuid_)
        send_mail_custom(name, date, time, email)
        return redirect(reverse("appointment:success_appointment"))

    if request.user.is_authenticated:
        user_data = User.objects.filter(id=request.session["_auth_user_id"])
        name = f"{user_data[0].first_name} {user_data[0].first_name}"
        email = user_data[0].email
        phone = user_data[0].phone
        context = {
            "name": name,
            "email": email,
            "phone": phone,
        }
        return render(request=request,
                      template_name=template,
                      context=context)
    return render(request=request,
                  template_name=template)


def success_appointment(request):
    if request.session.get('token'):
        template = 'appointment/success_appointment.html'
        request.session["token"] = None
        return render(request=request,
                      template_name=template)
    template = 'core/404.html'
    return render(request=request,
                  template_name=template)
