from django.shortcuts import render
from rest_framework import viewsets
from .serializer import RequestSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RequestForm
from .models import Request

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

def add_request(request):
    template_name = 'requests/add_request.html'
    context = {}
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('requests:list_requests')
    form = RequestForm()
    context['form'] = form
    return render(request, template_name, context)

def list_requests(request):
    template_name = 'requests/list_requests.html'
    pending_requests = Request.objects.filter(status='P')
    finished_requests = Request.objects.filter(status__in=['A', 'R'])
    context = {
        'pending_requests': pending_requests,
        'finished_requests': finished_requests
    }
    return render(request, template_name, context)

def edit_request(request, id_request):
    template_name = 'requests/add_request.html'
    context ={}
    request = get_object_or_404(Request, id=id_request)
    if request.method == 'POST':
        form = RequestForm(request.POST, instance=request)
        if form.is_valid():
            form.save()
            return redirect('requests:list_requests')
    form = RequestForm(instance=request)
    context['form'] = form
    return render(request, template_name, context)

def delete_request(request, id_request):
    request = Request.objects.get(id=id_request)
    request.delete()
    return redirect('requests:list_requests')

def accept_request(request, request_id):
    request_instance = Request.objects.get(pk=request_id)

    request_instance.status = 'A'
    request_instance.save()

    animal_instance = request_instance.animal
    animal_instance.is_adopted = True
    animal_instance.save()

    return redirect('requests:list_requests')

def decline_request(request, request_id):
    request_instance = Request.objects.get(pk=request_id)

    request_instance.status = 'R'
    request_instance.save()

    return redirect('requests:list_requests')