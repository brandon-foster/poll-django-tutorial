from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Poll
# Create your views here.
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.question for p in latest_poll_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    return HttpResponse("You're looking at results from %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
