from django.shortcuts import render


def home(request):
    c = ""
    value = {}
    if request.method == 'POST':
        n = eval(request.POST.get('num1'))
        if n % 2 == 0:
            c = 'Juft Son'
        else:
            c = 'Toq Son'
        value = {
            'n': n,
            'c': c
        }
    print(c)
    return render(request, 'home.html', value)