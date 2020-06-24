from django.shortcuts import render
from hierarchical.models import Hierarchy


def hierarchical_data_view(request):
    # data
    data = Hierarchy.objects.all()
    return render(request, 'main.html', {"data": data})
