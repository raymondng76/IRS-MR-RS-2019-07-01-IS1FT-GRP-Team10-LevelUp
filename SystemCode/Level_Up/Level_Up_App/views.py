from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View, CreateView, TemplateView, ListView, DetailView, FormView
from Level_Up_App.forms import NewUserForm, QuestionaireForm
from Level_Up_App.models import User, Questionaire
# Create your views here.

class IndexView(FormView):
    template_name = 'Level_Up_App/user_form.html'
    success_url = 'questionaire'
    context_object_name = 'user'
    form_class = NewUserForm
    # pk = None

    # def post(self, request):
    #     form=NewUserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         request.session['username'] = form.cleaned_data['name']
    #         return HttpResponseRedirect(self.success_url)

    def form_valid(self, form):
        # form.instance.user = self.request.user
        form.save()
        return super(IndexView, self).form_valid(form)
    # def get_success_url(self):
    #     return reverse('questionaire', kwargs={'pk': self.pk})

class QuestionaireView(FormView):
    context_object_name = 'questionaire_form'
    template_name = 'Level_Up_App/questionaire_form.html'
    success_url = 'Level_Up_App/user_form.html'
    form_class = QuestionaireForm

    # def get(self, request):
    #     user = request.session['username']
    #     form_class = self.form_class
    #     return render(request, self.template_name, {'user': user})

    def form_valid(self, form):
        form.save()
        return super(QuestionaireView, self).form_valid(form)

# class ResultView(ListView):
#     model
