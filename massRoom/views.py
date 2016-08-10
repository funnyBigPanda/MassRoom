from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from massRoom.models import Staff, Service, Record
import smtplib
from email.mime.text import MIMEText
import configparser

# Create your views here.
def home(request):
    return render(request, 'massRoom/index.html')


def about(request):
    staffs = Staff.objects.all()
    context = {
        'staffs': staffs
    }
    return render(request, 'massRoom/about.html', context)

def services(request):
    all_services = Service.objects.all()
    rows = int(len(all_services)/3)
    if rows*3 != len(all_services):
        rows += 1
    services = []
    for row in range(rows):
        services_3 = []
        for i in range(3):
            if len(all_services) > row*3+i:
                services_3.append(all_services[row*3+i])
        services.append(services_3)
    context = {
        'services' : services
    }

    return render(request, 'massRoom/services.html', context)

def show_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    context = {
        'service': service
    }
    return render(request, 'massRoom/service.html', context)

def works(request):

    return render(request, 'massRoom/works.html')

def add_record(request, service_id):
    config = configparser.ConfigParser()
    config.read('massRoom/email.ini')
    user_name = config['DEFAULT']['user_name']
    password = config['DEFAULT']['password']
    admin_email = config['DEFAULT']['admin_email']
    smtp_server = config['DEFAULT']['smtp_server']
    port = config['DEFAULT']['port']

    service = get_object_or_404(Service, id=service_id)
    a = Record()
    a.name = request.POST['name']
    a.phone = request.POST['phone']
    a.massage = service.name
    a.comment = request.POST['comment']
    a.save()

    msg = MIMEText('Ім\'я: ' + a.name + "\nТелефон: " + a.phone + "\nВид масажу: " + a.massage + "\nКоментар: " + a.comment)
    msg['Subject'] = 'Новий запис на сеанс масажу! ' + a.name
    msg['From'] = user_name
    msg['To'] = admin_email
    smtpObj = smtplib.SMTP(smtp_server, port)
    smtpObj.starttls()
    smtpObj.login(user_name, password)
    smtpObj.sendmail(user_name, [admin_email, user_name], msg.as_string())
    smtpObj.quit()

    url = reverse('service', kwargs={'service_id': service_id})
    return HttpResponseRedirect(url)