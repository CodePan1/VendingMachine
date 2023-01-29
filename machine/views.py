from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
import json
from django.views.decorators.http import require_safe
# Create your views here.
from machine.forms import VendingMachineForm, ProductForm
from machine.models import VendingMachine, Product


@require_safe
def vending_machine_create(request) -> JsonResponse:
    if request.method == 'POST':
        form = VendingMachineForm(request.POST)
        if form.is_valid():
            vending_machine = form.save()
            vending_machine_data = model_to_dict(vending_machine)
            return JsonResponse(vending_machine_data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@require_safe
def vending_machine_edit(request, vending_machine_pk: int) -> JsonResponse:
    vending_machine = get_object_or_404(VendingMachine, pk=vending_machine_pk)
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


@require_safe
def vending_machine_delete(request, vending_machine_pk: int) -> JsonResponse:
    vending_machine = get_object_or_404(VendingMachine, pk=vending_machine_pk)
    vending_machine.delete()
    return JsonResponse({'message': 'Vending Machine deleted'})


@require_safe
def product_create(request, vending_machine_pk: int) -> JsonResponse:
    vending_machine = get_object_or_404(VendingMachine, pk=vending_machine_pk)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.vending_machine = vending_machine
            product.save()
            product_data = {"pk": product.pk}
            return JsonResponse(product_data)
    else:
        form = ProductForm()
    context = {'form': form, 'vending_machine': vending_machine}
    return JsonResponse(json.dumps(context), safe=False)


@require_safe
def product_edit(request, vending_machine_pk: int, product_pk: int) -> JsonResponse:
    vending_machine = get_object_or_404(VendingMachine, pk=vending_machine_pk)
    product = get_object_or_404(Product, pk=product_pk, vending_machine=vending_machine)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            product_data = model_to_dict(product)
            return JsonResponse(product_data)
        else:
            return JsonResponse({'error': 'Invalid request method'}, status=400)


@require_safe
def product_delete(request, vending_machine_pk: int, product_pk: int) -> JsonResponse:
    vending_machine = get_object_or_404(VendingMachine, pk=vending_machine_pk)
    product = get_object_or_404(Product, vending_machine=vending_machine, pk=product_pk)
    product.delete()
    return JsonResponse({"message": "Product deleted successfully"})


@require_safe
def product_stock(request, vending_machine_pk: int) -> JsonResponse:
    if request.method == 'GET':
        vending_machine = get_object_or_404(VendingMachine, pk=vending_machine_pk)
        products = Product.objects.filter(vending_machine=vending_machine)
        products_list = []
        for product in products:
            products_list.append({'name': product.name, 'stock': product.stock, 'price': product.price})
        return JsonResponse({'products': products_list})
    else:
        return JsonResponse({'status': 'error'})
