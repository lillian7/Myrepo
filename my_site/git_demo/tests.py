from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from git_demo.forms import PersonForm, UserForm


class PersonFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(first_name='Li', last_name='Na', username='Li')

    def test_form_should_save_persons_age(self):
        fields = {
            'age': 23,
        }

        form = PersonForm(data=fields)
        form.is_valid()
        self.assertTrue(form.is_valid())
        personform = form.save(commit=False)
        personform.user = self.user
        personform.save()
        self.assertEqual(personform.age, fields['age'])

    def test_form_should_save_persons_first_name(self):
        fields = {
            'user_name':'lily',
            'first_name': 'Lily',
            'last_name': 'Nassie',
        }
        form = UserForm(data=fields)
        form.is_valid()


class PersonFormViewTest(TestCase):
    def test_person_form_view_should_render_person_forms(self):
        client = Client()
        response = client.get(reverse('git_demo:index'))
        self.assertTrue(200, response.status_code)
        self.assertTemplateUsed(response, template_name='person_form.html')