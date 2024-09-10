from django.shortcuts import render

def show_main(request):
    context = {
        'application_name': 'Nakama Collective',
        'class': 'PBD KKI',
        'name': 'Serafina Nala Putri Setiawan',
    }
    return render(request, "main.html", context)
