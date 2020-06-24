from django.shortcuts import render
from hierarchical.models import Hierarchy


def hierarchical_data_view(request):
    # data is everything from the Hierarchy model
    # so I'm going to extract
    data = Hierarchy.objects.all()
    return render(request, 'main.html', {"data": data})
