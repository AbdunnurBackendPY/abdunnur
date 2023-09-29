from django.shortcuts import render, redirect


def homepage(request):
    visit_count = request.COOKIES.get('visit_count', '0')
    visit_count = int(visit_count) + 1
    response = render(request, 'coco.html', {'visit_count': visit_count})
    response.set_cookie('visit_count', visit_count)
    return response


def delete_cookies(request):
    response = redirect('home')
    response = delete_cookies('visit_count')
    return response


