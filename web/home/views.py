from django.shortcuts import render
from django.views.generic import TemplateView

from home.helper import profile_picture


class HomePage(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        image = profile_picture(user) if not user.is_anonymous else None
        return render(request, self.template_name, {'image': image})
