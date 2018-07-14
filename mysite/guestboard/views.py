from django.contrib import messages
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
from django.shortcuts import (
    render,
    redirect,
)
from .models import Posting
from .forms import PostingForm


def _get_page(list_, page_no, count=5):
    paginator = Paginator(list_, count)
    try:
        page = paginator.page(page_no)
    except (EmptyPage, PageNotAnInteger):
        # page_noが指定されていない，数値で無い，範囲外の場合，
        # 先頭のページを表示する
        page = paginator.page(1)
    return page


def index(request):
    form = PostingForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "投稿を受付ました。")
            return redirect("guestboard:index")
        else:
            messages.error(request, "入力内容に誤りがあります。")
    page = _get_page(
        Posting.objects.order_by("-id"),
        request.GET.get("page")
    )
    contexts = {
        "form": form,
        "page": page,
    }
    return render(request, "guestboard/index.html", contexts)
