from collections import Counter
from django.http import HttpResponseNotFound
from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    ab_test = request.GET.get('from-landing', None)
    if ab_test == 'original':
        counter_click.update(['original'])
        return render(request, 'index.html')
    elif ab_test == 'test':
        counter_click.update(['test'])
        return render(request, 'index.html')
    else:
        return render(request, f"index.html")
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    ab_test = request.GET.get('ab-test-arg', None)
    if ab_test == 'original':
        counter_show.update(['original'])
        return render(request, 'landing.html')
    elif ab_test == 'test':
        counter_show.update(['test'])
        return render(request, 'landing_alternate.html')
    else:
        return HttpResponseNotFound(f"<h1>ОШИБКА! Вы перешли на не существующую страницу! Kод ошибки: 404 </h1> <br>"
                                    f"<h2>Параметры должны быть original или test</h2>")


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    return render(request, 'stats.html', context={
        'test_conversion': f"{counter_show['test']}/{counter_click['test']}",
        'original_conversion': f"{counter_show['original']}/{counter_click['original']}",
    })
