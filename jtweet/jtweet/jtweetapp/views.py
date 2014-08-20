from django.shortcuts import render
from django.template import RequestContext

# Create your views here.

def index(request):
  return render_to_responser('jtweetapp/index.html',
      {},
      context_instance=RequestContext(request))
