from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Exercise, Challenge, Submit
from accounts.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin


class ListExcerciseView(LoginRequiredMixin, ListView):
    template_name = 'challenges/exercises.html'
    model = Exercise
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['exercise_list'] = Exercise.objects.filter(visible=True).order_by('-category', 'exercise')
        return context 
    
class DetailExcerciseView(LoginRequiredMixin, DetailView):
    template_name = 'challenges/exercises_try.html'
    model = Exercise
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        product = Exercise.objects.get(pk=self.kwargs['pk'])
        challenge = Challenge.objects.filter(exerciseName=product, visible=True).order_by('title')
        context['challenge_list'] = challenge
        context['pks'] = self.kwargs['pk']
        return context
    
class ChallengeView(LoginRequiredMixin, ListView):
    template_name = 'challenges/challenge.html'
    model = Challenge
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['challenge'] = Challenge.objects.filter(identifier=self.kwargs['identifier'])
        context['pkz'] = self.kwargs['pks']
        return context
    
    def post(self, request, *args, **kwargs):
        submit = request.POST['submitFlag']
        flag = Challenge.objects.values_list('flag', flat=True).get(identifier=self.kwargs['identifier'])
        challenge = Challenge.objects.filter(identifier=self.kwargs['identifier'])
        score = Challenge.objects.values_list('score', flat=True).get(identifier=self.kwargs['identifier'])
        
        ctx = {'user': self.request.user}
        answered = Submit.objects.filter(user=ctx['user'], identifier=self.kwargs['identifier']).exists()
        
        if submit == flag:
            if answered == False:
                user = CustomUser.objects.get(username=ctx['user'])
                user.total_score += score
                user.save()
                
                ch = Challenge.objects.get(identifier=self.kwargs['identifier'])
                ch.cleared_counts += 1
                ch.save()
                
                print(user.total_score)
                
                Submit.objects.create(user=ctx['user'], identifier=self.kwargs['identifier'])
                
        return render(request, 'challenges/challenge.html', {'isCorrect': (submit == flag), 'challenge': challenge, 'answered': answered, 'pkz': self.kwargs['pks']}, )



