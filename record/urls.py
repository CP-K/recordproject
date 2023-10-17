from django.urls import path
from . import views

#URLパターンを逆引きできるように名前を付ける
app_name='record'

#URLパターンを登録する変数
urlpatterns = [
    #recordアプリへのアクセスはviewsモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),

    #記録投稿ページへのアクセスはviewsモジュールのCreateRecordViewを実行
    path('post/', views.CreateRecordView.as_view(), name='post'),

    #投稿完了ページへのアクセスはviewsモジュールのPostSuccessViewを実行
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),

    #猫の名前一覧ページ
    #records/<Catnamesテーブルのid値>にマッチング
    #<int:catname>は辞書{catname: id値(int)}としてCatnameViewに渡される
    path('records/<int:catname>',
        views.CatnameView.as_view(),
        name='records_catname'),
]
