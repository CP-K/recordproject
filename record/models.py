from django.db import models
#accountアプリのmodelモジュールからCustomUserをインポート
from accounts.models import CustomUser
from decimal import Decimal

class CatName(models.Model):
    '''記録する猫の名前を管理するモデル
    '''
    #猫の名前のフィールド
    title=models.CharField(
        verbose_name='猫の名前',                      #フィールドのタイトル
        max_length=30)
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        Returns(str):猫の名前
        '''
        return self.title

class FoodCategory(models.Model):
    '''ごはんの種類を管理するモデル
    '''
    #ごはんの種類のフィールド
    title=models.CharField(
        verbose_name='ごはんの種類',                   #フィールドのタイトル
        max_length=50)
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        Returns(str):ごはんの種類
        '''
        return self.title

class SnackCategory(models.Model):
    '''おやつの種類を管理するモデル
    '''
    #おやつの種類のフィールド
    title=models.CharField(
        verbose_name='おやつの種類',                    #フィールドのタイトル
        max_length=50)
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        Returns(str):おやつの種類
        '''
        return self.title

class ConditionRecord(models.Model):
    '''記録されたデータを管理するモデル
    '''
    #CustomUserモデル(のuser_id)とConditionRecordモデルを
    #1対多の関係で結びつける
    #CustomUserが親でConditionRecordが子の関係となる
    user=models.ForeignKey(
        CustomUser,
        #フィールドのタイトル
        verbose_name='ユーザー',
        #ユーザーに関連づけられた記録データが存在する場合は
        #そのユーザーを削除できないようにする
        on_delete=models.PROTECT
        )
    #CatNameモデル(のtitle)とConditionRecordモデルを
    #1対多の関係で結びつける
    #CatNameが親でConditionRecordが子の関係となる
    catname=models.ForeignKey(
        CatName,
        #フィールドのタイトル
        verbose_name='猫の名前',
        #猫の名前に関連づけられた記録データが存在する場合は
        #その猫の名前を削除できないようにする
        on_delete=models.PROTECT
        )
    #量の単位
    UNIT=(('g','g'),
        ('袋', '袋'),
        ('本','本'),
        ('個','個'))
    #尿と便の量
    AMOUNT=(('すごく多い','すごく多い'),
        ('多い','多い'),
        ('いつも通り','いつも通り'),
        ('少ない','少ない'),
        ('すごく少ない','すごく少ない'))
    #便の状態
    SCONDITION=(('カチコチ','カチコチ'),
        ('カタ','カタ'),
        ('いつも通り','いつも通り'),
        ('ヤワ','ヤワ'),
        ('シャバシャバ','シャバシャバ'))
    #元気度数と傷の状態
    CONDITION=(('すごく良い','すごく良い'),
        ('良い','良い'),
        ('変わらず','変わらず'),
        ('悪い','悪い'),
        ('すごく悪い','すごく悪い'))
    #通院日
    CLINIC=(('通院日','通院日'),
            ('通院なし','通院なし'))
    #爪切り
    NAIL=(('爪を切った','爪を切った'),
        ('爪切ってない','爪切ってない'))
    #記録日用のフィールド
    date=models.IntegerField(
        verbose_name='記録日'                   #フィールドのタイトル
        )
    #ConditionRecordモデル(のtitle)とFoodCategoryモデルを
    #1対多の関係で結びつける
    #ConditionRecordが親でFoodCategoryが子の関係となる
    food_category_bf=models.ForeignKey(
        FoodCategory,
        #フィールドのタイトル
        verbose_name='朝ごはんの種類',
        #ごはんの種類に関連づけられた記録データが存在する場合は
        #そのごはんの種類を削除できないようにする
        on_delete=models.PROTECT,
        related_name='food_category_bf',
        blank=True,
        null=True
        )
    #ごはんの量用のフィールド
    food_amount_bf=models.DecimalField(
        verbose_name='朝ごはんの量',              #フィールドのタイトル
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
        )
    #量の単位のフィールド
    food_unit_bf=models.CharField(
        verbose_name='朝ごはんの量の単位',        #フィールドのタイトル
        max_length=50,                           #最大文字数は50文字
        choices=UNIT,                            #unitフィールドにはUNITの要素のみを登録
        blank=True,
        null=True
        )

    food_category_l=models.ForeignKey(
        FoodCategory,
        #フィールドのタイトル
        verbose_name='昼ごはんの種類',
        #ごはんの種類に関連づけられた記録データが存在する場合は
        #そのごはんの種類を削除できないようにする
        on_delete=models.PROTECT,
        related_name='food_category_l',
        blank=True,
        null=True
        )
    #ごはんの量用のフィールド
    food_amount_l=models.DecimalField(
        verbose_name='昼ごはんの量',              #フィールドのタイトル
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
        )
    #量の単位のフィールド
    food_unit_l=models.CharField(
        verbose_name='昼ごはんの量の単位',        #フィールドのタイトル
        max_length=50,                           #最大文字数は50文字
        choices=UNIT,                            #unitフィールドにはUNITの要素のみを登録
        blank=True,
        null=True
        )

    food_category_d=models.ForeignKey(
        FoodCategory,
        #フィールドのタイトル
        verbose_name='夕ごはんの種類',
        #ごはんの種類に関連づけられた記録データが存在する場合は
        #そのごはんの種類を削除できないようにする
        on_delete=models.PROTECT,
        related_name='food_category_d',
        blank=True,
        null=True
        )
    #ごはんの量用のフィールド
    food_amount_d=models.DecimalField(
        verbose_name='夕ごはんの量',              #フィールドのタイトル
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
        )
    #量の単位のフィールド
    food_unit_d=models.CharField(
        verbose_name='夕ごはんの量の単位',        #フィールドのタイトル
        max_length=50,                           #最大文字数は50文字
        choices=UNIT,                            #unitフィールドにはUNITの要素のみを登録
        blank=True,
        null=True,
        )

    #ConditionRecordモデル(のtitle)とSnackCategoryモデルを
    #1対多の関係で結びつける
    #ConditionRecordが親でSnackCategoryが子の関係となる
    snack_category_1=models.ForeignKey(
        SnackCategory,
        #フィールドのタイトル
        verbose_name='おやつ1の種類',
        #ごはんの種類に関連づけられた記録データが存在する場合は
        #そのごはんの種類を削除できないようにする
        on_delete=models.PROTECT,
        related_name='snack_category_1',
        blank=True,
        null=True
        )
    #おやつの量用のフィールド
    snack_amount_1=models.DecimalField(
        verbose_name='おやつ1の量',              #フィールドのタイトル
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
        )
    #量の単位のフィールド
    snack_unit_1=models.CharField(
        verbose_name='おやつ1の量の単位',        #フィールドのタイトル
        max_length=50,                          #最大文字数は50文字
        choices=UNIT,                           #unitフィールドにはUNITの要素のみを登録
        blank=True,
        null=True
        )

    snack_category_2=models.ForeignKey(
        SnackCategory,
        #フィールドのタイトル
        verbose_name='おやつ2の種類',
        #ごはんの種類に関連づけられた記録データが存在する場合は
        #そのごはんの種類を削除できないようにする
        on_delete=models.PROTECT,
        related_name='snack_category_2',
        blank=True,
        null=True
        )
    #おやつの量用のフィールド
    snack_amount_2=models.DecimalField(
        verbose_name='おやつ2の量',      #フィールドのタイトル
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
        )
    #量の単位のフィールド
    snack_unit_2=models.CharField(
        verbose_name='おやつ2の量の単位',        #フィールドのタイトル
        max_length=50,                          #最大文字数は50文字
        choices=UNIT,                           #unitフィールドにはUNITの要素のみを登録
        blank=True,
        null=True
        )

    snack_category_3=models.ForeignKey(
        SnackCategory,
        #フィールドのタイトル
        verbose_name='おやつ3の種類',
        #ごはんの種類に関連づけられた記録データが存在する場合は
        #そのごはんの種類を削除できないようにする
        on_delete=models.PROTECT,
        related_name='snack_category_3',
        blank=True,
        null=True
        )
    #おやつの量用のフィールド
    snack_amount_3=models.DecimalField(
        verbose_name='おやつ3の量',      #フィールドのタイトル
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
        )
    #量の単位のフィールド
    snack_unit_3=models.CharField(
        verbose_name='おやつ3の量の単位',        #フィールドのタイトル
        max_length=50,                          #最大文字数は50文字
        choices=UNIT,                           #unitフィールドにはUNITの要素のみを登録
        blank=True,
        null=True
        )
    #尿の量のフィールド
    urine_amount=models.CharField(
        verbose_name='尿の量',           #フィールドのタイトル
        max_length=50,                   #最大文字数は50文字
        choices=AMOUNT                   #urine_amountフィールドにはAMOUNTの要素のみを登録
        )
    #便の量のフィールド
    stool_amount=models.CharField(
        verbose_name='便の量',          #フィールドのタイトル
        max_length=50,                  #最大文字数は50文字
        choices=AMOUNT                  #stool_amountフィールドにはAMOUNTの要素のみを登録
        )
    #便の状態のフィールド
    stool_condition=models.CharField(
        verbose_name='便の状態',       #フィールドのタイトル
        max_length=50,                 #最大文字数は50文字
        choices=SCONDITION             #stool_conditionフィールドにはSCONDITIONの要素のみを登録
        )
    #元気度数のフィールド
    physical_condition=models.CharField(
        verbose_name='元気度数',       #フィールドのタイトル
        max_length=50,                 #最大文字数は50文字
        choices=CONDITION              #physical_conditionフィールドにはCONDITIONの要素のみを登録
        )
    #傷の状態のフィールド
    damage=models.CharField(
        verbose_name='傷の状態',       #フィールドのタイトル
        max_length=50,                 #最大文字数は50文字
        choices=CONDITION              #damageフィールドにはCONDITIONの要素のみを登録
        )
    #通院日のフィールド
    clinic=models.CharField(
        verbose_name='通院日',         #フィールドのタイトル
        max_length=50,                 #最大文字数は50文字
        choices=CLINIC                 #clinicフィールドにはCLINICの要素のみを登録
        )
    #爪切りのフィールド
    cut_nail=models.CharField(
        verbose_name='爪切り',         #フィールドのタイトル
        max_length=50,                 #最大文字数は50文字
        choices=NAIL                   #cut_nailフィールドにはNAILの要素のみを登録
        )
    #体重のフィールド
    weight=models.DecimalField(
        verbose_name='体重',            #フィールドのタイトル
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
        )
    #その他のコメントフィールド
    comment=models.TextField(
        verbose_name='その他',
        max_length=200,
        blank=True,
        null=True
        )
    #イメージのフィールド
    image=models.ImageField(
        verbose_name='イメージ',
        upload_to='photos'
        )
    #投稿日時のフィールド
    posted_at=models.DateTimeField(
        verbose_name='投稿日時',         #フィールドのタイトル
        auto_now_add=True                #日時を自動追加
        )
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        Returns(str):記録日
        '''
        return str(self.date)



