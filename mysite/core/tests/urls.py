from django import forms
from django.http import HttpResponse
from django.template import engines
from django.views.decorators.cache import never_cache
from django.views.generic.edit import FormView
from django.urls import path

from core.views import MessageMixin


TEMPLATE = """{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>
        {{ message }}
    </li>
    {% endfor %}
</ul>
{% endif %}
"""


@never_cache
def show(request):
    template = engines['django'].from_string(TEMPLATE)
    return HttpResponse(template.render(request=request))


class DummyForm(forms.Form):
    name = forms.CharField(required=True)


class DummyFormViewWithMsg(MessageMixin, FormView):
    form_class = DummyForm
    success_url = show
    error_message = "Name was invalid"
    template_name = "core/tests/error.html"


urlpatterns = [
    path('add/msg/', DummyFormViewWithMsg.as_view(), name='add_error_msg'),
]
