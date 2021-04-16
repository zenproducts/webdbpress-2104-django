# WEB+DB PRESS Vol.122 特集2「はじめてのDjango」

このリポジトリーはWEB+DB PRESS Vol.122の特集2「はじめてのDjango」で作ったプロジェクトです。
特集内で作った最終的な状態のWebアプリケーションを公開しています。

もしまだ本書をお持ちでない方はぜひ以下のURLからお買い求めください。

https://gihyo.jp/magazine/wdpress/archive/2021/vol122

## 利用方法

以下の手順で、手元にこのリポジトリーをクローンしてDjangoを起動できます。
**GitやPythonの環境は事前にご用意ください**。

リポジトリーとPython環境を準備します。
```bash
$ git clone git@github.com:zenproducts/webdbpress-2104-django.git 
$ cd webdbpress-2104-django
$ python3.9 -m venv venv
$ source venv/bin/activate
$ pip install Django
```

データベースとユーザーアカウントを準備します。

```bash
$ cd mysite
$ python manage.py migrate
$ python manage.py createsuperuser
```

サーバーを起動します。

```bash
$ python manage.py runserver
```

ここで http://127.0.0.1:8000/ にアクセスするとブログのトップページが表示されます。
記事を追加するには http://127.0.0.1:8000/admin/ にアクセスしてください。

詳しくは本特集に書かれていますので、ぜひお買い求めください。
PythonとDjangoを使ったWebアプリケーションの開発方法をステップバイステップで説明しています！

## 目次

特集2︰
新バージョン登場！ PythonによるWeb開発の基本
はじめてのDjango

* 第1章：DjangoでのWebアプリケーション開発の始め方
  （WebのしくみとPythonでの開発方法…… 清原 弘貴）
* 第2章：ブログ記事をモデルに保存しよう
  （データベース連携とDjango Adminによる管理サイト実装…… 清原 弘貴）
* 第3章：ブログの画面をビューで作ろう
  （テンプレートを使ったWebアプリケーションの基本UI…… 清原 弘貴）
* 第4章：ブログをCSSでデザインしよう
  （Bootstrapを組み込んでUIを使いやすくする…… 清原 弘貴）
* 第5章：さらに学んでいくために
  （最新のDjango 3.2について注目の機能を紹介…… 清原 弘貴）

https://gihyo.jp/magazine/wdpress/archive/2021/vol122
