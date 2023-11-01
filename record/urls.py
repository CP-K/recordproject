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

    #ユーザーの投稿一覧ページ
    #records/<ユーザーテーブルのid値>にマッチング
    #<int:user>は辞書{user: id値(int)}としてCatnameViewに渡される
    path('user_list/<int:user>',
        views.UserView.as_view(),
        name='user_list'
        ),

    #詳細ページ
    #record-detail/<Condition Recordsテーブルのid値>にマッチング
    #<int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('record_detail/<int:pk>',
        views.DetailView.as_view(),
        name='record_detail'
        ),

    #マイページ
    #mypage/へのアクセスはMypageViewを実行
    path('mypage/',
        views.MypageView.as_view(),
        name='mypage'
        ),
]
