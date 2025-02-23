from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import notes
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from . forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

# Create your views here.
class NotesDeleteView(LoginRequiredMixin,DeleteView):
    model=notes
    success_url='/smart/Notes/'
    template_name='Notes/Notes_delete.html'

    login_url="/login"

    def query_set(self):
        return self.request.user.notes.all()

class NotesUpdateView(LoginRequiredMixin,UpdateView):
    model=notes
    success_url='/smart/Notes/'
    form_class=NotesForm

    login_url="/login"

    def query_set(self):
        return self.request.user.notes.all()

class NotesCreateView(LoginRequiredMixin,CreateView):
    model=notes
    success_url='/smart/Notes/'
    form_class=NotesForm

    login_url="/login"

    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin,ListView):
    model=notes
    context_object_name="Notes"
    login_url="/login"

    def query_set(self):
        return self.request.user.notes.all()


class NotesDetailView(LoginRequiredMixin,DetailView):
    model= notes 
    context_object_name='Note'
    login_url="/login"

    def query_set(self):
        return self.request.user.notes.all()


