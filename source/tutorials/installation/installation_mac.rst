===============================================================================
環境を構築しよう
===============================================================================

事前にPython3.6をインストールしpathを通しておいてください。

それぞれpathが通っているかは *which* コマンドで確認できます。

.. code-block:: bash

    $ which python3.6
    /Library/Frameworks/Python.framework/Versions/3.6/bin/python3

Pythonの仮想環境を作ろう
===============================================================================

.. note::

   仮想環境を作るメリットは、複数のシステムを開発する時に、各システム専用の環境を手軽に用意出来る事です。

   例えばシステムAではDjango1.6を、システムBではDjango1.8を使っているような場合、仮想環境がなければ
   どちらか一方のバージョンしかインストールすることができず、PC自体を分けて開発するか、
   その都度使うバージョンのDjangoをインストールしなければいけません。

   個人で1つのアプリケーションしか作らない場合、仮想環境を作るメリットはほぼ無いのですが、
   仮想環境の作り方を知っておけば追々役立ちますので、ぜひ覚えて下さい。

   どうしても仮想環境を作るのが面倒な方は、 **practiceフォルダ** を作った後、
   **Djangoをインストールしよう** まで読み飛ばして下さい。

   また、チュートリアルを進める中で仮想環境を有効にするコマンド

   $ source venv/bin/activate

   は無視してください。

まずvenvを使いPythonの仮想環境を作ります。

開発をPyCharmで行うので、ホームディレクトリ以下にPycharmProjectsフォルダーを作ります。

その下に、学習用のDjangoプロジェクトと仮想環境を配置するためのpracticeフォルダを作ります。

.. code-block:: bash

   $ mkdir -p ~/PycharmProjects/practice

practiceフォルダの下に仮想環境を作ります。

.. code-block:: bash

   $ cd ~/PycharmProjects/practice/
   $ python3.6 -m venv venv

Pythonの仮想環境を有効にしよう
===============================================================================

作った仮想環境を有効にしましょう。

.. code-block:: bash

   $ cd ~/PycharmProjects/practice/
   $ source venv/bin/activate
   (venv)$

成功すると、プロンプトに仮想環境のフォルダー名が丸括弧で囲われ表示されるようになります。

Djangoをインストールしよう
===============================================================================

仮想環境にDjangoをインストールします。DjangoはPyPIに登録されているので、 **pip install** コマンドでインストールします。

.. code-block:: bash

   (venv)$ pip install django

正しくインストールされたか、 **pip freeze** コマンドで確認しましょう。**Django==1.11.X** と表示されていれば成功です。

.. code-block:: bash

   (venv)$ pip freeze
   Django==1.11.3
   pytz==2017.2

.. note::

   pytzはDjangoが依存しているモジュールなので、Djangoをインストールする際、一緒にインストールされます。

以上で、環境構築についての説明はおしまいです。
