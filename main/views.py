from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245112',
        'name': 'Tristan Agra Yudhistira',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
