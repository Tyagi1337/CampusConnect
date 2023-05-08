from django.shortcuts import render


def admin_home(request):
    return render(request, 'hod_template/base_template.html')
