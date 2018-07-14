===============================================================================
Django アプリケーションを作ろう
===============================================================================

Djangoを使って、 **「Hello World!」** をブラウザに表示するプログラムを作ってみましょう。

アプリケーションを作ろう
===============================================================================

Djangoは複数のアプリケーションを1つのプロジェクトの中にまとめて、1つのWebサイトを開発していきます。

manage.pyを使い、**mysiteプロジェクト** の中に **helloアプリケーション** を作ってみましょう。

**Mac環境**

.. code-block:: bash

   $ cd ~/PycharmProjects/practice/
   $ source venv/bin/activate
   (venv)$ python mysite/manage.py startapp hello

**Windows環境**

.. code-block:: bash

   > cd "C:\PycharmProjects\practice"
   > venv\Scripts\Activate.ps1
   (venv)> python mysite\manage.py startapp hello

mysiteフォルダーの中にhelloフォルダーが作られます。

.. code-block:: bash

    hello/
        migrations/
        __init__.py
        admin.py
        models.py
        tests.py
        views.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    manage.py

Django プロジェクトにアプリケーションを組み込もう
===============================================================================

アプリケーションを作ったら、プロジェクトにアプリケーションを組み込まなくては使えません。
アプリケーションを組み込むためには、プロジェクトの設定ファイルの **INSTALLED_APPS** という変数に追加します。

**mysite/settings.py**

.. code-block:: python

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'hello', # 追加する
    )
