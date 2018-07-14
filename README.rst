===============================================================================
django_tutorial
===============================================================================

DjangoによるWebアプリケーション開発入門を書く為のプロジェクトです。

フォルダー構成
===============================================================================

:mysite: チュートリアルで作っているDjangoプロジェクト
:source: sphinxでビルドする為のrstや、イメージファイル


仮想環境
===============================================================================

仮想環境を2つ使います。

:venv: Python3.6、Django環境。チュートリアル用のコードの動作確認に使います。
:venv2: Python3.6、Sphinx、sphinx-autobuild環境。

venv
----

.. code-block:: bash

   $ python3.6 -m venv venv
   $ source venv/bin/activate
   (venv)$ pip install -r requirements.txt
   (venv)$ python mysite/manage.py runserver

venv2
-----

.. code-block:: bash

   $ python3.6 -m venv venv2
   $ source venv2/bin/activate
   (venv2)$ pip install -r requirements2.txt
   (venv2)$ sphinx-autobuild -p 8080 source ../eiry.bitbucket.org/
