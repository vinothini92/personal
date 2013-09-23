# Create your views here.
#from django.http import HttpResponse
#from django.template import Context
#from django.template.loader import get_template
from django.shortcuts import render_to_response
from blog.models import BlogPost
from django.template import RequestContext

def home(request):
	{#content = {
	'Title':"First post",
	'date':"20/09/2013",
	'author':"vinothini",
	'body':"Django application to create Blog written by beginner program"
	} #}
	contents = BlogPost.objects.all();
	return render_to_response('index.html',{'posts':contents},context_instance=RequestContext(request))
	#t = get_template('index.html')
	#html = t.render(Context({'Welcome_msg':"Welcome to my Blog"}))
	#return HttpResponse(html)
