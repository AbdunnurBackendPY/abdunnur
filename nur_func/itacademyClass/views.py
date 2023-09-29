from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import SingleObjectTemplateResponseMixin, SingleObjectMixin

from .models import Cat

@login_required
def index(request):
    shablon= Cat.objects.all()
    return render(request, "shablon.html",{"shablon":shablon})


class MyDetailView(SingleObjectMixin, SingleObjectTemplateResponseMixin, TemplateView):
    model = Cat
    def get_template_names(self):
        if self.request.user.is_superuser:
            return ['my_detail_admin.html']
        else:
            return ['my_detail.html']


