===============================================================================
Django Modelを使ってみよう
===============================================================================

Modelは、サイトを構成するデータソース（主にデータベース）へのアクセスを請け負います。
理解するにはデータベースの知識も必要になるため、Djangoの中でも特に難しい所です。

しかし、シンプルなCRUD：Create（生成）、Read（読み取り）、Update（更新）、Delete（削除）は、
幾つかのルールを覚えれば実現可能です。ジンプルなCRUDができれば、一般的なWebアプリケーションは開発できます。

苦手意識を持たず、理解を深めていきましょう。

基礎知識とModelクラス（理論）
===============================================================================

Modelを作るまえに、データベースにテーブルを作るDDLを思い返してみましょう。

::

   CREATE TABLE "テーブル名" (
      カラム1 データ型 {その他の制約},
      カラム2 データ型 {その他の制約},
   );

Modelクラスもデータベースを扱う以上、DDLと同じ情報を持ちます。
また、Modelクラスもクラスである以上、Pythonのclassの書き方から外れることはありません。

DDLとModelクラスがどのように紐づくかを表にしてみます。

:テーブル名: クラス名
:カラム名: クラス変数名
:データ型: クラス変数に代入するオブジェクト（Fieldクラスのインスタンス）
:その他: Fieldクラスのオプション

この情報を元に、Modelクラスの雛形を書いてみます。

::

   class テーブル名(Model):
       カラム名1 = データ型(その他の制約)
       カラム名2 = データ型(その他の制約)

基礎知識とModelクラス（実例）
===============================================================================

.. note::

   ここで出てくるコードはあくまで実例なので、実際に書く必要はありません。

テーブル定義からDDLとModelを書く例です。

テーブル定義
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
テーブル
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 1 1

   * - 論理名
     - 物理名
   * - 顧客テーブル
     - customer

-------------------------------------------------------------------------------
列
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 2 2 2 1 1 1 2 3

   * - 論理名
     - 物理名
     - データ型
     - 長さ
     - 必須
     - キー
     - 外部キー
     - 備考
   * - ID
     - id
     - INT
     -
     - YES
     - PK
     -
     - AUTO INCREMENT
   * - 姓
     - last_name
     - varchar
     - 20
     - YES
     -
     -
     -
   * - 名
     - first_name
     - varchar
     - 20
     - YES
     -
     -
     -
   * - Eメールアドレス
     - email_address
     - varchar
     - 255
     - YES
     - UK
     -
     -
   * - メモ
     - memo
     - text
     -
     -
     -
     -
     -

DDL
-------------------------------------------------------------------------------

.. code-block:: sql

   CREATE TABLE customer (
      id serial NOT NULL PRIMARY KEY,
      last_name varchar(20) NOT NULL,
      first_name varchar(20) NOT NULL,
      email_address varchar(255) NOT NULL UNIQUE,
      memo text
   );

Model
-------------------------------------------------------------------------------

Modelでは、幾つかの制約が暗黙的に定義されています。例えばFieldクラスのオプションに何も指定しなければ、NOT NULL制約がかかります。

また、PRIMARY KEYとなるクラス変数を定義しない場合、idが自動的に定義されます。

**hello/models.py**

.. code-block:: python

   from django.db import models


   class Customer(models.Model):
       # id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
       last_name = models.CharField(max_length=20)
       first_name = models.CharField(max_length=20)
       email_address = models.EmailField(max_length=255, unique=True)
       memo = models.TextField(null=True)

以上で実例は終わりです。

migrateを実行しよう
===============================================================================

Modelを作る前に、 **migrate** を実行しましょう。migrateとは、Modelクラスを定義したり、定義後のModelクラスに変更を加えたときに、
それらをデータベースのスキーマに反映するコマンドです。

migrateの履歴管理やDjangoの一部のモジュールでデータベースを使うので、自分でModelを定義する前にmigrateを実行しましょう。

.. note::

   通常は、settings.pyにDBの設定を行った直後にmigrateを実施しておくと良いでしょう。

   1. プロジェクトを作る（ djang-admin.py startproject XXXXXX ）
   2. settings.py にDBの設定を書く（DBAにsqlite3を使う場合は、この手順を省略する）
   3. migrateを実行する （ python mysite/manage.py migrate ）

.. code-block:: bash

   (venv)$ python mysite/manage.py migrate


次のようなメッセージが表示されれば成功です。

.. code-block:: bash

    Operations to perform:
      Synchronize unmigrated apps: staticfiles, messages
      Apply all migrations: contenttypes, admin, sessions, auth
    Synchronizing apps without migrations:
      Creating tables...
        Running deferred SQL...
      Installing custom SQL...
    Running migrations:
      Rendering model states... DONE
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying sessions.0001_initial... OK


Modelクラスを定義しよう
===============================================================================

それでは、実際にModelクラスをhello/models.pyに追加しましょう。

今回つくるModelクラスは **Djangoフォームを使ってみよう** で作ったHelloFormクラスを使い、
画面から投稿されたデータ検証し、検証結果に問題が無いデータをデータベースに保存するためのModelとします。

**hello/models.py**

.. code-block:: python

   from django.db import models


   class Hello(models.Model):
       your_name = models.CharField(max_length=10)

       def __str__(self):
           return "<{0}>".format(self.your_name)


Modelクラスをデータベースのスキーマに反映しよう
===============================================================================

Modelクラスをデータベースのスキーマに反映するには、2つの手順をふみます。

- データベースのスキーマとModelクラスの差を取り、変更処理が書かれているPythonファイルを生成する
- 変更処理が書かれているPythonファイルを使いデータベースのスキーマを変更する

それぞれ manage.py で実行できます。

.. code-block:: bash

   (venv)$ python mysite/manage.py makemigrations
   (venv)$ python mysite/manage.py migrate


それぞれのコマンドを打った結果、次のようなメッセージが表示されれば成功です。

.. code-block:: bash

    (venv)$ python mysite/manage.py makemigrations
    Migrations for 'hello':
      0001_initial.py:
        - Create model Hello

    (venv)$ python mysite/manage.py migrate
    Operations to perform:
      Synchronize unmigrated apps: staticfiles, messages
      Apply all migrations: contenttypes, admin, sessions, auth, hello
    Synchronizing apps without migrations:
      Creating tables...
        Running deferred SQL...
      Installing custom SQL...
    Running migrations:
      Rendering model states... DONE
      Applying hello.0001_initial... OK


Modelを使ってみよう
===============================================================================

ここでは、実際にModelをDjango shellからModelを操作してCRUDの基礎を学びます。

まず、Django shellからModelを操作してみましょう。 **Django shell** を起動してください。

.. code-block:: bash

   (venv)$ python mysite/manage.py shell
   >>>


.. note::

   **>>>** や **...** は、Shellで表示される $ と同じく、Django shellが

   表示するプロンプトです。実際に入力するとSyntax Errorが発生するので注意してください。

データを登録しよう
-------------------------------------------------------------------------------

Django shell からデータを登録します。

.. code-block:: python

   >>> from hello.models import Hello
   >>> kenji = Hello.objects.create(your_name='Kenji')
   >>> print("id:{0}, your_name:{1}".format(kenji.id, kenji.your_name))
   id:1, your_name:Kenji
   >>> takuya = Hello.objects.create(your_name='Takuya')
   >>> print("id:{0}, your_name:{1}".format(takuya.id, takuya.your_name))
   id:2, your_name:Takuya

データを検索しよう
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
全件取得する場合
-------------------------------------------------------------------------------

**Hello.objects.all()** で、無条件ですべてのデータを取得できます。

.. code-block:: python

    >>> Hello.objects.all()
    [<Hello: <Kenji>>, <Hello: <Takuya>>]
    >>> for h in Hello.objects.all(): print(h.your_name)
    ...
    Kenji
    Takuya

-------------------------------------------------------------------------------
1件しか取得できないデータを検索する場合
-------------------------------------------------------------------------------

idを指定して検索する場合など、必ず1件しかデータが取得できない場合は

**Hello.objects.get({パラメーター})** で検索します。

.. code-block:: python

   >>> h = Hello.objects.get(pk=1)
   >>> print(h.your_name)
   Kenji

なお、検索結果が0件だった場合は**hello.models.DoesNotExist** エラーが発生します。

-------------------------------------------------------------------------------
条件に一致するデータを検索する場合
-------------------------------------------------------------------------------

条件指定で検索したい、かつ条件に一致するデータが複数存在する可能性がある場合は、

**Hello.objects.filter({パラメーター})** で検索します。

.. code-block:: python

   >>> h_qs = Hello.objects.filter(id__in=[1,2])
   >>> for h in h_qs: print(h.your_name)
   ...
   Kenji
   Takuya
   >>> for h in h_qs.filter(your_name='Kenji'): print(h.your_name)
   ...
   Kenji

データを更新しよう
-------------------------------------------------------------------------------

データを更新する場合は、**インスタンス変数を上書きした後、XXX.save()** メソッドを呼び出します。

.. code-block:: python

   >>> h = Hello.objects.get(pk=1)
   >>> print(h.your_name)
   Kenji
   >>> h.your_name = 'Makoto'
   >>> h.save()
   >>> h = Hello.objects.get(pk=1)
   >>> print(h.your_name)
   Makoto

データを削除しよう
-------------------------------------------------------------------------------

データを更新する場合は、**インスタンス変数を上書きした後、XXX.delete()** メソッドを呼び出します。

.. code-block:: python

    >>> h = Hello.objects.get(pk=1)
    >>> h.delete()
    >>> h = Hello.objects.get(pk=1)
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
      File "/Users/eiry/PycharmProjects/practice/venv/lib/python3.4/site-packages/django/db/models/manager.py", line 127, in manager_method
        return getattr(self.get_queryset(), name)(*args, **kwargs)
      File "/Users/eiry/PycharmProjects/practice/venv/lib/python3.4/site-packages/django/db/models/query.py", line 334, in get
        self.model._meta.object_name
    hello.models.DoesNotExist: Hello matching query does not exist.


画面から入力されたデータをデータベースに保存しよう
===============================================================================

実際にプログラムを書く前に、**クロスサイトリクエスト・フォージェリ** と **PRGパターン** について説明をしなければなりません。

クロスサイトリクエスト・フォージェリ
-------------------------------------------------------------------------------

クロスサイトリクエスト・フォージェリとは、Webにおける攻撃手法の1つです。詳細はWikipediaのページをみてください。

`クロスサイトリクエスト・フォージェリ - Wikipedia <http://ja.wikipedia.org/wiki/クロスサイトリクエストフォージェリ>`_

Djangoは、この攻撃に対抗する手段としてPOST時に暗号論的擬似乱数値をHIDDENに埋め込む方法が採用されています。
テンプレートの中で **{% csrf_token %}** と言う記述が出てきますが、これがHIDDENに暗号論的擬似乱数値を埋め込んでいる所です。
これを忘れると、POST時にセキュリティーエラーが発生します。

PRGパターンは
-------------------------------------------------------------------------------

PRGパターンとは、 **Post Redirect Get** の頭文字をとったもので、POSTでデータを送り正常に処理できた場合は、そのままHTMLのレスポンスを返さずに別のURLへリダイレクトすると言うものです。

説明を見ると難しいかもしれませんが、掲示板を例にしてPRGパターンを使わなかった場合の問題をあげてみます。

1. ブラウザから投稿するする
2. 正常に投稿処理が行われ、HTMLのレスポンスが返される
3. ブラウザをリロードすると、同じ投稿がされてしまう

このような問題を回避する為に、PRGパターンを使います。ビュー関数の中で **redirect(....)**
と言う関数を呼び出していますが、これがPRGパターンのR（Redirect）に該当するところです。

画面から入力されたデータをデータベースに保存しよう
-------------------------------------------------------------------------------

それでは、画面から入力されたデータを、Modelを使ってデータベースに保存してみましょう。

**views.py** にビュー関数を追加します。

**hello/views.py**

.. code-block:: python

   from django.shortcuts import redirect
   from . import forms, models

   def hello_models(request):
       form = forms.HelloForm(request.POST or None)
       if form.is_valid():
           models.Hello.objects.create(**form.cleaned_data)
           return redirect('hello:hello_models')

       d = {
           'form': form,
           'hello_qs': models.Hello.objects.all().order_by('-id')
       }
       return render(request, 'models.html', d)

.. note::

   redirect関数の引数には、 :doc:`views_and_urls` で urlブロック: **{% url 'namespace:name' %}** に

   渡していた引数と同じく、 **namespace:name** と書くことでURLConfから必要なURLを逆引きしてくれます。

   ほかにも、URL：http://XXXXXX を直接書くこともできます。

**templates** フォルダーに **models.html** を追加し、次のように編集します。

**templates/models.html**

.. code-block:: html

    {% extends "base.html" %}

    {% block body %}
      <h1>your_nameを登録する</h1>
      <h2>登録</h2>
      <form method="post" action="">
        {{ form.errors.your_name }}
        <label>{{ form.your_name.label }} {{ form.your_name }}</label><br>
        <input type="submit" value="送信">
        {% csrf_token %}
      </form>
      <hr>
      <h2>一覧</h2>
      {% for h in hello_qs %}
        {{ h.your_name }}<br>
      {% endfor %}
    {% endblock %}

最後に、URLConfを書きましょう。

**hello/urls.py**

.. code-block:: python

    from django.conf.urls import url
    from . import views


    urlpatterns = [
        url(r'^$', views.hello_world, name='hello_world'),
        url(r'^template/$', views.hello_template, name='hello_template'),
        url(r'^if/$', views.hello_if, name='hello_if'),
        url(r'^for/$', views.hello_for, name='hello_for'),
        url(r'^get/$', views.hello_get_query, name='hello_get_query'),
        url(r'^forms/$', views.hello_forms, name='hello_forms'),
        url(r'^sample_forms/$', views.hello_sample_forms, name='hello_sample_forms'),
        url(r'^models/$', views.hello_models, name='hello_models'),  # 追加する
    ]

http://127.0.0.1:8000/hello/models/ にアクセスして動作確認をしましょう。

**動作確認のパターン**

.. list-table::
   :widths: 5 10
   :stub-columns: 1

   * - 画面を表示したとき
     - エラーが発生せず、画面が表示できることを確認します
   * - *名前* に何も入力しない場合
     - 「このフィールドは必須です。」と言うメッセージが表示されることを確認します
   * - *名前* に「テスト名」と入力した場合
     - 『一覧』の下に「テスト名」と表示されることを確認します

以上で、Djangoの基礎編は終わりです。