from django.shortcuts import render

from .serializers import SchemaSerializer

from .models import SchemaItem

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from rest_framework import generics, authentication, permissions

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class SchemaList(ListView):
    model = SchemaItem
    template_name = 'schemas/schema.html'
    context_object_name = 'schema_list'


class SchemaDetail(DetailView):
    model = SchemaItem
    template_name = 'schemas/detail.html'
    context_object_name = 'schema'

class SchemaCreate(CreateView):
    model = SchemaItem
    fields = ['schemaname', 'changelog', 'schemafile']
    template_name = 'schemas/itemform.html'
    success_url = reverse_lazy('schema')

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)





class SchemaUpdate(UpdateView):
    model = SchemaItem
    fields = ['user','schemaname', 'changelog', 'schemafile']
    template_name = 'schemas/itemform.html'
    success_url = reverse_lazy('schemas')


class SchemaDelete(DeleteView):
    model = SchemaItem
    context_object_name = 'schema'
    success_url = reverse_lazy('schemas')
    





