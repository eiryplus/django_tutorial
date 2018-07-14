===============================================================================
|django_application| を作ろう
===============================================================================

Django基礎編で作ったプロジェクトに、ゲストボード用の |django_application| を追加しましょう。

.. note::

   Django基礎編で作ったクラスやメソッドは利用しないので、新しく |django_project| を作っても問題ありません。

|django_application| を作ろう
===============================================================================

**startapp** コマンドを使い、 **guestboard** アプリケーションを作りましょう。

**Mac環境**

.. code-block:: bash

    $ cd ~/PycharmProjects/practice/
    $ source venv/bin/activate
    (venv)$ python mysite/manage.py startapp guestboard

**Windows環境**

.. code-block:: bash

    > cd "C:\PycharmProjects\practice"
    > venv\Scripts\Activate.ps1
    (venv)> python mysite\manage.py startapp guestboard


設定ファイルを編集しよう
===============================================================================

**設定ファイル** を編集し、 **guestboard** アプリケーションを **INSTALLED_APPS** に追加しましょう。

**mysite/settings.py**

.. code-block:: python

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'hello',
        'crud',
        'guestboard',  # 追加する
    )

また、アプリケーションの追加とは別に、CSSやJSファイルなどの **静的ファイル** を扱えるようにします。

以下のように **STATICFILES_DIRS** 変数を追加して下さい。

.. code-block:: python

    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )
