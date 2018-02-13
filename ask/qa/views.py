from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from models import Question, Answer

from .forms import AskForm, AnswerForm

# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():
			form._user = request.user
			answer = form.save()
			return HttpResponseRedirect(reverse('detail', args=(question_id,)))
	else:
		form = AnswerForm(initial={'question': question_id})
	return render(request, 'qa/detail.html', {'question': question,
												'form': form})

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

def ask_question(request):
	if request.method == 'POST':
		form = AskForm(request.POST)
		if form.is_valid():
			form._user = request.user
			question = form.save()
			url = reverse('detail', args=(question.id,))
			return HttpResponseRedirect(url)
	else:
		form = AskForm()
	return render(request, 'qa/ask.html', {'form': form})
