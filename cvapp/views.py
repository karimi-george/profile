from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf 
from .models import Feedback
from django.conf import settings
class GeneratePdf(View):
    def get(seFGlf, request, *args, **kwargs):
        pdf = render_to_pdf('invoice.html')
        return HttpResponse(pdf, content_type='application/pdf')
def index(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        feedback=Feedback(name=name,email=email,message=message)
        feedback.save()
    return render(request, 'index.html')