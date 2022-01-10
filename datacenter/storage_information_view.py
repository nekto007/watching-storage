from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Visit
from .models import format_duration


def storage_information_view(request):
    non_closed_visits = [
        {
            'who_entered': visit.passcard,
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(visit.get_duration())
        } for visit in Visit.objects.all().filter(leaved_at=None)
    ]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
