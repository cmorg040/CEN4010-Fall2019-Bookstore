#from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader, RequestContext
#from .models import Question
# Create your views here.
#def index(request):
#    return HttpResponse('My first successful django')
'''
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('sp/index.html')
    context = RequestContext(request, {
        'latest_questions':latest_questions
    })
    #output=", ".join(q.question for q in latest_questions)
    #return HttpResponse(output)
    return HttpResponse(template.render(context))
'''
'''
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions': latest_questions}
    return render(request, 'sp/index.html', context)


def detail(request, question_id):
    return HttpResponse("Detail %s" % question_id)

def results(request, question_id):
    return HttpResponse("Results %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Vote %s" % question_id)
'''