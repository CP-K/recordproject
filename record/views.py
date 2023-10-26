from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
#django.views.genericからTemplateviewをインポート
from django.views.generic import TemplateView, ListView
#django.views.genericからCreateViewをインポート
from django.views.generic import CreateView
#django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
#formsモジュールからConditionRecordFormをインポート
from .forms import ConditionRecordForm
#method_decoratorをインポート
from django.utils.decorators import method_decorator
#login_requiredをインポート
from django.contrib.auth.decorators import login_required
#modelsモジュールからモデルConditionRecordをインポート
from .models import ConditionRecord
#django.views.genericからDetailViewをインポート
from django.views.generic import DetailView

class IndexView(ListView):
    '''トップページのビュー
    '''
    #index.htmlをレンダリングする
    template_name='index.html'
    #モデルConditionRecordのオブジェクトにorder_by()を適用して
    #投稿日時の降順で並び替える
    queryset=ConditionRecord.objects.order_by('-posted_at')
    #1ページに表示するレコードの件数
    paginate_by=7

#デコレーターにより、CreateRecordViewへのアクセスはログインユーザーに限定される
#ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')
class CreateRecordView(CreateView):
    '''記録投稿ページのビュー
    ConditionRecordFormで定義されてるモデルとフィールドと連携して
    投稿データをデータベースに登録する
    
    Attributes:
        form_class: モデルとフィールドが登録されたフォームクラス
        Template_name: レンダリングするテンプレート
        success_url: データベースへの登録完了後のリダイレクト先
        '''
    #forms.pyのConditionRecordをフォームクラスとして登録
    form_class=ConditionRecordForm
    #レンダリングするテンプレート
    template_name="post_record.html"
    #フォームデータ登録完了後のリダイレクト先
    success_url=reverse_lazy('record:post_done')

    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド
        
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う
        
        parameters:
            form(django.forms.Form):
                form_classに格納されているConditionRecordFormオブジェクト
        Return:
            HttpResponseRedirectオブジェクト:
                スーパークラスのform_valid()の戻り値を返すことで、
                success_urlで設定されているURLにリダイレクトさせる
        '''
        #commit=-FalseにしてPOSTされたデータを取得
        postdata=form.save(commit=False)
        #投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user=self.request.user
        #投稿データをデータベースに登録
        postdata.save()
        #戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    '''投稿完了ページのビュー
    
    Attributes:
        template_name: レンダリングするテンプレート
    '''
    #index.htmlをレンダリングする
    template_name='post_success.html'

class CatnameView(ListView):
    '''猫の名前ページのビュー
    
    Attributes:
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''
    #index.htmlをレンダリングする
    template_name='index.html'
    #1ページに表示するレコードの件数
    paginate_by=7

    def get_queryset(self):
        '''クエリを実行する
        
        self.kwargsの取得が必要なため、クラス変数querysetではなく。
        get_queryset()のオーバーライドによりクエリを実行する
        
        Returns:
            クエリによって取得されたレコード
        '''
        #self.kwargsでキーワードの辞書を取得し、
        #catnameキーの値(Catnamesテーブルのid)を取得
        catname_id=self.kwargs['catname']
        #filter(フィールド名=id)で絞り込む
        catnames=ConditionRecord.objects.filter(catname=catname_id).order_by('-posted_at')
        #クエリによって取得されたレコードを返す
        return catnames

class UserView(ListView):
    '''ユーザーの投稿一覧ページのビュー
    Attributes:
    template_name: レンダリングするテンプレート
    paginate_by: 1ページに表示するレコードの件数
    '''
    #index.htmlをレンダリングする
    template_name='index.html'
    #1ページに表示するレコードの件数
    paginate_by=9

    def get_queryset(self):
        '''クエリを実行する
        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する

        Returns:クエリによって取得されたレコード
        '''
        #self.kwargsでキーワードの辞書を取得し、
        #userキーの値(ユーザーテーブルのid)を取得
        user_id=self.kwargs['user']
        #filter(フィールド名=id)で絞り込む
        user_list=ConditionRecord.objects.filter(user=user_id).order_by('-posted_at')
        #クエリによって取得されたレコードを返す
        return user_list

class DetailView(DetailView):
    '''詳細ページのビュー
    
    投稿記事の詳細を表示するためDetailViewを継承する
    Attributes:
        template_name: レンダリングするテンプレート
        model: モデルのクラス
    '''
    #post.htmlをレンダリングする
    template_name='detail.html'
    #クラス変数modelにモデルConditionRecordを設定
    model=ConditionRecord