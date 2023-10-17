from django.forms import ModelForm
from .models import ConditionRecord

class ConditionRecordForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        
        Attributes:
            model:モデルのクラス
            fields:フォームで使用するモデルのフィールドを指定
        '''
        model=ConditionRecord
        fields=['catname','date',
                'food_category_bf','food_amount_bf','food_unit_bf',
                'food_category_l','food_amount_l','food_unit_l',
                'food_category_d','food_amount_d','food_unit_d',
                'snack_category_1','snack_amount_1','snack_unit_1',
                'snack_category_2','snack_amount_2','snack_unit_2',
                'snack_category_3','snack_amount_3','snack_unit_3',
                'urine_amount','stool_amount','stool_condition',
                'physical_condition','damage','clinic','cut_nail','weight',
                'comment','image'
                ]