from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cats.models import Cat, Breed


class CatList(LoginRequiredMixin, View):
    def get(self, request):
        cat = Cat.objects.all()
        brd = Breed.objects.all()
        brd_count = Breed.objects.all().count()
        context = {'cat_list': cat, 'breed_list': brd, 'breed_count': brd_count}
        return render(request, 'cats/cat_list.html', context)


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        brd = Breed.objects.all()
        context = {'breed_list': brd}
        return render(request, 'cats/breed_list.html', context)


class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')



