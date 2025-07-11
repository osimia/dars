from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Lesson
import io, sys, json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/index.html', {'lessons': lessons})

def lesson_detail(request, id):
    lesson = get_object_or_404(Lesson, id=id)
    return JsonResponse({
        'title': lesson.title,
        'content': lesson.content,
        'code_example': lesson.code_example,
    })

@csrf_exempt
def run_code(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data.get('code', '')
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        try:
            exec(code, {})
            result = buffer.getvalue()
        except Exception as e:
            result = str(e)
        finally:
            sys.stdout = old_stdout
        return JsonResponse({'result': result})
