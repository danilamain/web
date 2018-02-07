from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from models import Question, Answer

# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'qa/detail.html', {'question': question})

def home(request, current=''):
	if current == 'popular':	
		new_questions = Question.objects.popular()
		name = 'popular'
	else:
		new_questions = Question.objects.new()
		name = 'home'
	paginator = Paginator(new_questions, 10)
	
	page = request.GET.get('page', 1)
	try:	
		questions = paginator.page(page)
		return render(request, 'qa/home.html', {'questions': questions})
	except PageNotAnInteger:
		page = 1
	except EmptyPage:
		page = paginator.num_pages
	return HttpResponseRedirect("%s?page=%s" % (reverse(name), page))
