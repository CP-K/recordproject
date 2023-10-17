from django.contrib import admin

from .models import CatName, ConditionRecord, FoodCategory, SnackCategory

class CatNameAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    '''
    #レコード一覧にidとtitleを表示
    list_display=('id','title')
    #表示するカラムにリンクを設定
    list_display_links=('id','title')

class ConditionRecordAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    '''
    #レコード一覧にidとdateを表示
    list_display=('id','date')
    #表示するカラムにリンクを設定
    list_display_links=('id','date')

class FoodCategoryAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    '''
    #レコード一覧にidとtitleを表示
    list_display=('id','title')
    #表示するカラムにリンクを設定
    list_display_links=('id','title')

class SnackCategoryAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    '''
    #レコード一覧にidとtitleを表示
    list_display=('id','title')
    #表示するカラムにリンクを設定
    list_display_links=('id','title')

#Django管理サイトにCatName、CatNameAdminを登録する
admin.site.register(CatName, CatNameAdmin)

#Django管理サイトにConditionRecord、ConditionRecordAdminを登録する
admin.site.register(ConditionRecord, ConditionRecordAdmin)

#Django管理サイトにFoodCategory、FoodCategoryAdminを登録する
admin.site.register(FoodCategory, FoodCategoryAdmin)

#Django管理サイトにSnackCategory、SnackCategoryAdminを登録する
admin.site.register(SnackCategory, SnackCategoryAdmin)