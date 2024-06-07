import requests
from django.shortcuts import render
# Create your views here.
from datetime import date, datetime, timedelta


def main(request):
    # del request.session['appointments']
    try:
        print(request.session['appointments'])
    except:
        request.session['appointments'] = []
    if request.method == 'GET':
        today = datetime.today()
        date_ = str(datetime(today.year, today.month, today.day))
        date_ = date_[0:date_.find(' ')].split('-')
        all_weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        d1 = date(int(date_[0]), int(date_[1]), int(date_[2]))
        d2 = date(int(date_[0]) + 1, int(date_[1]), int(date_[2]))
        delta = d2 - d1  # returns timedelta
        final_data = {}
        data_dynamic = []
        for _ in range(today.weekday()):
            data_dynamic.append(f'  -{all_weeks[today.weekday()].split("-")[0]}')
        all_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                      'November', 'December']
        for i in range(delta.days + 1):
            day = d1 + timedelta(days=i)
            weekday = day.weekday()
            curr_day = str(day).split("-")[2]
            if curr_day == '01' and len(data_dynamic) > 1:
                month_year = f"{all_months[int(str(day).split('-')[1]) - 2]}-{str(d1 + timedelta(days=i - 1)).split('-')[0]}"
                final_data[month_year] = data_dynamic
                new_data = []
                for _ in range(len(data_dynamic) % 7):
                    new_data.append(f'  -{all_weeks[weekday].split("-")[0]}')
                data_dynamic = [i for i in new_data]
            else:
                pass
            data_dynamic.append(f'{curr_day}-{all_weeks[weekday].split("-")[0]}')

        return render(request, 'main/index.html',
                      {'final_data': final_data,
                       'all_weeks': all_weeks})
    else:
        return render(request, 'main/busy.html')


def appointments(request):
    try:
        print(request.session['appointments'])
    except:
        request.session['appointments'] = []
    appointments = request.session['appointments']
    return render(request, 'main/appointments.html', {'appointments': appointments})


def delete_appointment(request, appointment_id):
    Appointment.objects.get(id=appointment_id).delete()
    a = [request.session['appointments'].index(i) for i in request.session['appointments'] if i[0] == appointment_id]
    del request.session['appointments'][a[0]]
    appointments = request.session['appointments']
    return render(request, 'main/appointments.html', {'appointments': appointments})

