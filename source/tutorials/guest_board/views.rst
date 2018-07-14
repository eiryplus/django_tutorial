===============================================================================
|view_method| を作ろう
===============================================================================

|view_method| で必要な機能を整理しよう
===============================================================================

今回作る |view_method| で必要な機能を整理します。

1. 過去に投稿されたメッセージを表示する

   - 一度に表示する件数を5件にする
   - ページ送りボタンが押下された時は、指定されたページが開かれるようにする。

2. 投稿ボタンが押下された時に適切に振る舞う

   - 投稿内容に誤りがあれば、投稿内容にエラーがあったことをユーザーに通知し、入力フォーム毎にエラーメッセージを表示する
   - 投稿内容に誤りがなければ、投稿を受け付けた事をユーザーに通知し、画面を再表示する

これらの機能を実現するために、2つのモジュールを紹介します。

-------------------------------------------------------
ページネーターとは
-------------------------------------------------------

長い文章や大量のデータを表示するときに複数のページに分割して表示する機能をページネーターと言います。ショッピングサイトなどで馴染みがある機能だと思います。

Django には、これを実現する為の ページネータークラス（ `django.core.paginator` ）が予め組み込まれています。

-------------------------------------------------------
メッセージフレームワークとは
-------------------------------------------------------

投稿ボタンが押下されたとき、正常に登録されたか、投稿内容にエラーがあったかを一度だけメッセージ表示（フラッシュメッセージ）を行いたいことがあります。

Django には、これを実現する為の メッセージフレームワーク（ `django.contrib.messages` ） が予め組み込まれています。

|view_method| を作ろう
===============================================================================

実際に |view_method| を作りましょう。 :doc:`../tutorial/index` で登場しなかった3つの機能

- ModelForm
- ページネーター
- メッセージフレームワーク

を使いますので、それぞれの機能がどのように使われるか、注意してみてください。

**guestboard/views.py**

.. code-block:: python

    # ページネーター
    from django.core.paginator import (
        Paginator,  # ページネーター本体のクラス
        EmptyPage,  # ページ番号が範囲外だった場合に発生する例外クラス
        PageNotAnInteger  # ページ番号が数字でなかった場合に発生する例外クラス
    )
    from django.shortcuts import (
        render,
        redirect,
    )
    from .models import Posting
    from .forms import PostingForm


    def _get_page(list_, page_no, count=5):
        """ページネーターを使い、表示するページ情報を取得する"""
        paginator = Paginator(list_, count)
        try:
            page = paginator.page(page_no)
        except (EmptyPage, PageNotAnInteger):
            # page_noが指定されていない場合、数値で無い場合、範囲外の場合は
            # 先頭のページを表示する
            page = paginator.page(1)
        return page


    def index(request):
        """表示・投稿を処理する"""
        # ModelFormもFormもインスタンスを作るタイミングでの使い方は同じ
        form = PostingForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                # save()メソッドを呼ぶだけでModelを使ってDBに登録される。
                form.save()
                # メッセージフレームワークを使い、処理が成功したことをユーザーに通知する
                messages.success(request, '投稿を受付ました。')
                return redirect('guestboard:index')
            else:
                # メッセージフレームワークを使い、処理が失敗したことをユーザーに通知する
                messages.error(request, '入力内容に誤りがあります。')
        page = _get_page(
            Posting.objects.order_by('-id'),  # 投稿を新しい順に並び替えて取得する
            request.GET.get('page')  # GETクエリからページ番号を取得する
        )
        contexts = {
            'form': form,
            'page': page,
        }
        return render(request, 'guestboard/index.html', contexts)


|url_dispatcher| を書こう
===============================================================================

:doc:`../tutorial/views_and_urls` を参考に |url_dispatcher| を書きましょう。

**guestboard/urls.py**

.. code-block:: python

    from django.conf.urls import url
    from . import views


    urlpatterns = [
        url(r'^$', views.index, name='index'),
    ]

**mysite/urls.py**

.. code-block:: python

    from django.conf.urls import include, url


    urlpatterns = [
        url(r'^hello/', include('hello.urls', namespace='hello')),
        url(r'^crud/', include('crud.urls', namespace='crud')),
        url(r'^guestboard/', include('guestboard.urls', namespace='guestboard')),  # 追加する
    ]

