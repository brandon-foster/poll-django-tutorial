from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from polls.models import Poll
# Create your views here.
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk = poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, question_id):
    return HttpResponse("You're looking at results from %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
