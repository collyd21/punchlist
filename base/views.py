from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PunchForm 

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Punch, PunchImage

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('punches')

class PunchList(LoginRequiredMixin, ListView):
    model = Punch
    context_object_name = 'punches'

class PunchDetail(LoginRequiredMixin, DetailView):
    model = Punch
    context_object_name = 'punch'

class PunchCreate(LoginRequiredMixin, CreateView):
    model = Punch
    form_class = PunchForm  # Use the PunchForm you defined
    success_url = reverse_lazy('punches')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.save()  # Save the Punch instance first

        # Handle uploaded images
        images = self.request.FILES.getlist('images')
        for image_data in images:
            punch_image = PunchImage(punch=form.instance)
            punch_image.image.save(image_data.name, image_data, save=True)

        return super(PunchCreate, self).form_valid(form)

from .models import Punch, PunchImage

class PunchUpdate(LoginRequiredMixin, UpdateView):
    model = Punch
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('punches')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Punch
    context_object_name = 'punch'
    success_url = reverse_lazy('punches')
