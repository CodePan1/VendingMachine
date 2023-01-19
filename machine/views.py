from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
import json

# Create your views here.
from machine.forms import VendingMachineForm
from machine.models import VendingMachine


def vending_machine_create(request):
    if request.method == 'POST':
        form = VendingMachineForm(request.POST)
        if form.is_valid():
            vending_machine = form.save()
            vending_machine_data = {"pk": vending_machine.pk}
            return JsonResponse(vending_machine_data)
    else:
        form = VendingMachineForm()
    context = {'form': form}
    return JsonResponse(json.dumps(context), safe=False)


def vending_machine_edit(request, pk):
    vending_machine = get_object_or_404(VendingMachine, pk=pk)
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            name = data['name']
            location = data['location']
        except KeyError:
            return HttpResponseBadRequest("Invalid data")
        vending_machine.name = name
        vending_machine.location = location
        vending_machine.save()
        return JsonResponse({'pk': vending_machine.pk})
    else:
        return JsonResponse({'error': 'Invalid request method'})
