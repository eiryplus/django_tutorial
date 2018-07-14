===============================================================================
|django_model| 、 |django_model_form| を作ろう
===============================================================================

|django_model| を作ろう
===============================================================================

:doc:`design` で作ったテーブル設計を元に |django_model| を定義しましょう。

**guestboard/models.py**

.. code-block:: python

   from django.db import models


    class Posting(models.Model):
        name = models.CharField(
            max_length=64,
            verbose_name='名前',
            help_text='あなたの名前を入力してください',
        )
        message = models.CharField(
            max_length=255,
            verbose_name='メッセージ',
            help_text='メッセージを入力してください',
        )
        created_at = models.DateTimeField(
            auto_now_add=True,
            verbose_name='登録日時',
        )

基本的には今までのチュートリで書いた通りのModelになりますが、 **verbose_name** と言うパラメーターが増えています。
この後つくるModelFormで使われるパラメーターになるので、忘れずに書いて下さい。

.. note::

   Modelを定義したり変更した時は、忘れずにマイグレーションを行いましょう

   (venv)$ python mysite/manage.py makemigrations

   (venv)$ python mysite/manage.py migrate


|django_model_form| を作ろう
===============================================================================

:doc:`../tutorial/forms` では **django.forms.Form** クラスを親クラスとしていましたが、Djangoには **django.forms.ModelForm** と言う
Modelクラスを元にFieldを自動的に生成してくれるクラスが存在します。登録や更新処理ではModelFormクラスを使う方が良いでしょう。

.. note::

   FormとModelFormの使い分けは？と言う疑問が出ると思いますが、私は検索で使う入力項目はFormを、

   登録・更新で使う入力項目はModelFormを使うようにしています。

   今回のケースではあまりModelFormクラスのメリットを感じ無いと思いますが、ModelFormは

   validationを行う時にユニーク制約のチェックも行う為、複雑なModelになるほどModelFormが便利になります。

**guestboard/forms.py** を追加して、ModelFormを定義します。

.. code-block:: python

    from django import forms
    from .models import Posting


    class PostingForm(forms.ModelForm):

        class Meta:
            model = Posting
            fields = ('name', 'message')
            widgets = {
                'name': forms.TextInput(attrs={'size': 40}),
                'message': forms.Textarea(attrs={'cols': 80, 'rows': 20})
            }

**Metaクラス** に定義されている変数の意味は以下の表を参考にしてください。

.. list-table::
   :header-rows: 1
   :widths: 1 8

   * - 変数名
     - 意味
   * - model
     - 紐付けるModelクラスを指定します
   * - fields
     - | Modelから入力フォームを生成する対象のフィールドをタプル形式で指定します。
       | 使わないフィールドを定義する **excludes** と言う変数も存在します。
       | excludesを使う場合は **fieldsを削除して** 、 **excludes=('created_at',)** と書くことが出来ます。
   * - widgets
     - 画面表示に使用するウィジェットを指定します。未指定の場合、デフォルトで設定されているウィジェットが使われます。
