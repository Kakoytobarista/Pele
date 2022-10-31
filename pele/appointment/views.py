from django.shortcuts import render, redirect
from rest_framework.reverse import reverse

from appointment.utils import send_mail_custom
from users.models import User


def index(request):
    template = 'appointment/index.html'
    if request.method == "POST" or None:
        request.session["name"] = request.POST["name"]
        request.session["email"] = request.POST["email"]
        request.session["time"] = request.POST["time"]
        request.session["date"] = request.POST["date"]
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
    template = 'appointment/success_appointment.html'
    name, date, time, email = request.session["name"], request.session["date"], request.session["time"], request.session["email"]
    send_mail_custom(name, date, time, email)
    return render(request=request,
                  template_name=template)
