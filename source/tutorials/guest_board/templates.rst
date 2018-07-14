===============================================================================
|template_file| を作ろう
===============================================================================

共通パーツを作ろう
===============================================================================

まず、ページネーターで使うパーツを作ります。このパーツは本アプリ以外でも使えるので、独立したファイルに作っておきましょう。

**templates/pagination.html** を作成します。

.. code-block:: html

    {# ページネーター #}
    <nav class="col-sm-8">
      <ul class="pager">
        {# ページ送りボタン(1) - 新しい投稿を表示する #}
        {% if page.has_previous %}
          <li class="previous">
            <a href="?page={{ page.previous_page_number }}"><span aria-hidden="true">&larr;</span> Newer</a>
          </li>
        {% else %}
          <li class="previous disabled">
            <a href="#"><span aria-hidden="true">&larr;</span> Newer</a>
          </li>
        {% endif %}

        {# ページ情報 #}
        <li>Page {{ page.number }} of {{ page.paginator.num_pages }}.</li>

        {# ページ送りボタン(2) - 古い投稿を表示する #}
        {% if page.has_next %}
          <li class="next">
            <a href="?page={{ page.next_page_number }}">Older <span aria-hidden="true">&rarr;</span></a>
          </li>
        {% else %}
          <li class="next disabled">
            <a href="#">Older <span aria-hidden="true">&rarr;</span></a>
          </li>
        {% endif %}
      </ul>
    </nav>

続いて **templates/guestboard/base.html**  を作成します。

.. code-block:: html

    <!doctype html>
    <html>
    {% load staticfiles %}
    <head lang="ja">
      <meta charset="UTF-8">
      <title>{% block title %}{% endblock %}</title>
      {% block css %}
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
        <link rel="stylesheet" href="{% static 'css/common.css' %}" >
      {% endblock %}
    </head>
    <body>
      <div class="container">
        {% if messages %}
          <ul class="messages">
            {% for message in messages %}
              <li class="{{ message.tags }}">{{ message }}</li>
            {% endfor %}
          </ul>
        {% endif %}
        {% block body %}
        {% endblock %}
      </div>
      {% block js %}
        <script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
        <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
      {% endblock %}
    </body>
    </html>

この中で見慣れないURLが3つ登場しています。

- `//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css`
- `//code.jquery.com/jquery-1.11.3.min.js`
- `//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js`

これらのファイルは、CDN （ コンテンツ・デリバリー・ネットワーク ）から **bootstrap** と **jQuery** を読み込んでいます。

.. note::

    通常、CDNはファイルを配信するサーバーを分散させることを目的として使いますが、

    今回はファイルをダウンロードする手間を省略する為に使っています。

    これらのファイルをダウンロードして、静的ファイルを格納するフォルダーに配置しても問題ありません。

ゲストボード用のテンプレートファイルを作ろう
===============================================================================

最後に **templates/guestboard/index.html** を作成します。

この中で **{% include "pagination.html" %}** と言うブロックが存在します。
これは別のファイルを読み込むブロックになります。今回はページネーター用のパーツを読み込んでいます。

.. code-block:: html

    {% extends "guestboard/base.html" %}
    {% block title %}Guest Board{% endblock %}
    {% block body %}
      <div class="page-header">
        <h1>Guest Board</h1>
      </div>
      {# 画面上段 - 入力フォームを定義する #}
      <form action="{% url 'guestboard:index' %}" method="post">
        <div class="row">
          {% for field in form %}
            <div class="form-group">
              {% if field.errors %}
                <div class="col-sm-10">
                  <span class="col-sm-10">{{ field.errors }}</span>
                </div>
              {% endif %}
              <div class="col-sm-10">
                <label class="col-sm-3 control-label">{{ field.label_tag }}</label>
                <label class="label col-sm-7">{{ field }}</label>
              </div>
            </div>
          {% endfor %}
          <div class="col-sm-10">
            <div class="form-group">
              <label class="col-sm-2 control-label"><input type="submit" class="btn btn-primary" value="登録"></label>
              {% csrf_token %}
            </div>
          </div>
        </div>
      </form>
      <hr>
      {# 画面下段 - 投稿内容とページネーター用のパーツを表示する #}
      {% include "pagination.html" %}{# ページネーター用のパーツ #}
      <div class="container">
        <div class="row">
          <div class="col-sm-8">
            {% for posting in page %}
              <div class="panel panel-primary">
                <div class="panel-heading">
                  <h3 class="panel-title">{{ posting.name }} <label class="small">投稿日時：{{ posting.created_at }}</label></h3>
                </div>
                <div class="panel-body">
                  {{ posting.message }}
                </div>
              </div>
            {% endfor %}
          </div>
        </div>
      </div>
      {% include "pagination.html" %}{# ページネーター用のパーツ #}

    {% endblock %}
