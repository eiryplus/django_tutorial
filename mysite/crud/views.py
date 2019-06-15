from django.urls import reverse_lazy
from django.views import generic
from .models import Message
from .forms import MessageForm


class ListView(generic.ListView):
    model = Message
    template_name = "crud/index.html"


class CreateView(generic.CreateView):
    template_name = "crud/edit.html"
    form_class = MessageForm
    success_url = reverse_lazy("crud:list")


class UpdateView(generic.UpdateView):
    pk_url_kwarg = "pk"   # 定義しない場合は "pk" が使われるので、今回は省略可
    template_name = "crud/edit.html"
    form_class = MessageForm
    queryset = Message.objects
    success_url = reverse_lazy("crud:list")


class DeleteView(generic.DeleteView):
    pk_url_kwarg = "pk"   # 定義しない場合は "pk" が使われるので、今回は省略可
    template_name = "crud/edit.html"
    form_class = MessageForm
    queryset = Message.objects
    success_url = reverse_lazy("crud:list")


list_ = ListView.as_view()
create = CreateView.as_view()
update = UpdateView.as_view()
delete_ = DeleteView.as_view()
