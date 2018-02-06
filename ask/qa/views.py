from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, InvalidPage
from django.http import HttpResponse
from models import Question, Answer

# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'qa/detail.html', {'question': question})

def home(request):
	new_questions = Question.objects.new()
	paginator = Paginator(new_questions, 10)
	
	page = request.GET.get('page')
	try:	
		questions = paginator.page(page)
	except InvalidPage:
		questions = paginator.page(paginator.num_pages)
	
	return render(request, 'qa/home.html', {'questions': questions})