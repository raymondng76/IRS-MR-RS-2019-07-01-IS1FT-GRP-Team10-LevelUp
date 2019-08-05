from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic import View, CreateView, TemplateView, ListView, DetailView, FormView
from Level_Up_App.forms import NewUserForm, QuestionaireForm
from Level_Up_App.models import User, Questionaire
# Create your views here.

class IndexView(FormView):
    template_name = 'Level_Up_App/user_form.html'
    success_url = '/questionaire/'
    form_class = NewUserForm

    def form_valid(self, form):
        return super(IndexView, self).form_valid(form)


class QuestionaireView(FormView):
    context_object_name = 'questionaire_form'
    template_name = 'Level_Up_App/questionaire_form.html'
    success_url = 'Level_Up_App/user_form.html'
    form_class = QuestionaireForm

    def form_valid(self, form):
        return super(QuestionaireView, self).form_valid(form)

# class ResultView(ListView):
#     model
