#from django.shortcuts import render_to_response
from django.shortcuts import render
#from django.template import RequestContext
from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse('Custom index message')
  # return render_to_response('jtweetapp/index.html',
  # {},
  # context_instance=RequestContext(request))
