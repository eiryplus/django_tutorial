from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class MessageMixin(SuccessMessageMixin):
    error_message = ''

    def form_invalid(self, form):
        response = super().form_invalid(form)
        error_message = self.get_error_message()
        if error_message:
            messages.error(self.request, error_message)
        return response

    def get_error_message(self):
        return self.error_message
