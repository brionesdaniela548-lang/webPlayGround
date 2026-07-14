from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Page


class PageListView(ListView):
    model = Page
    template_name = 'pages/pages_list.html'


class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'


class CreatePageView(LoginRequiredMixin,CreateView):
    model = Page
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')
    template_name = 'pages/create_page.html'
    login_url = 'login'

class pageUpdate(LoginRequiredMixin,UpdateView):
    model = Page
    fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('pages:update',args=[self.object.id]) + '?ok'

class pageDeleteView(LoginRequiredMixin,DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")
    login_url = 'login'
