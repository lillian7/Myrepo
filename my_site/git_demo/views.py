from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from git_demo.forms import PersonForm, UserForm

class Home(FormView):
    template_name = 'person_form.html'
    form_class = PersonForm

    def post(self, request, *args, **kwargs):
        return super(Home, self).post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        user_form = UserForm()
        return render(request, self.template_name, {'form': form, 'user_form': user_form})
