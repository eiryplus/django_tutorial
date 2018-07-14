===============================================================================
静的ファイル を作ろう
===============================================================================

メッセージフレームワークや、formのエラーメッセージで使用する為のCSSファイルを作りましょう。

**static/css/common.css** を作成します。

.. code-block:: css

    @charset "UTF-8";

    .errorlist {
        color: red;
        margin-left: 0;
        padding-left: 0;
    }

    .errorlist li {
        list-style-type: none;
    }

    .messages {
        margin: 0;
        padding: 0;
    }

    .messages li {
        list-style-type: none;
        padding: 15px;
    }

    .messages li.success {
        color: #00f;
        background-color: #ddf;
    }

    .messages li.error {
        color: #F00;
        background-color: #fdd;
    }

`errorlist` や `messages` 等 は |django_form| が付加するclass属性です。

CSSの詳細については、ここでは説明を省略します。他の技術書や解説サイトを参考にしてください。
