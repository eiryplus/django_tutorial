from .models import Posting
from .forms import PostingForm
from django.urls import reverse_lazy
from django.views import generic
from core.views import MessageMixin


class ListView(generic.ListView):
    paginate_by = 2
    model = Posting
    ordering = "-id"
    template_name = "guestboard/index.html"


class CreateView(MessageMixin, generic.CreateView):
    model = Posting
    form_class = PostingForm
    template_name = "guestboard/create.html"
    success_url = reverse_lazy("guestboard:index")
    success_message = "投稿が完了しました"
    error_message = "投稿内容に誤りがあります"


index_ = ListView.as_view()
create = CreateView.as_view()

# def index(request):
#     form = PostingForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             messages.success(request, "投稿を受付ました。")
#             return redirect("guestboard:index")
#         else:
#             messages.error(request, "入力内容に誤りがあります。")
#     page = _get_page(
#         Posting.objects.order_by("-id"),
#         request.GET.get("page")
#     )
#     contexts = {
#         "form": form,
#         "page": page,
#     }
#     return render(request, "guestboard/index.html", contexts)
