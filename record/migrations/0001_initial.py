# Generated by Django 4.2.4 on 2023-09-15 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CatName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='猫の名前')),
            ],
        ),
        migrations.CreateModel(
            name='ConditionRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField(max_length=8, verbose_name='記録日')),
                ('food_amount', models.IntegerField(max_length=20, verbose_name='ごはんの量')),
                ('snack_amount', models.IntegerField(max_length=20, verbose_name='おやつの量')),
                ('unit', models.CharField(choices=[('gram', 'g'), ('pack', '袋'), ('stick', '本'), ('piece', '個')], max_length=50, verbose_name='量の単位')),
                ('urine_amount', models.CharField(choices=[('more', 'すごく多い'), ('much', '多い'), ('usual', 'いつも通り'), ('little', '少ない'), ('less', 'すごく少ない')], max_length=50, verbose_name='尿の量')),
                ('stool_amount', models.CharField(choices=[('more', 'すごく多い'), ('much', '多い'), ('usual', 'いつも通り'), ('little', '少ない'), ('less', 'すごく少ない')], max_length=50, verbose_name='便の量')),
                ('stool_condition', models.CharField(choices=[('harder', 'カチコチ'), ('hard', 'カタ'), ('usual', 'いつも通り'), ('soft', 'ヤワ'), ('softer', 'シャバシャバ')], max_length=50, verbose_name='便の状態')),
                ('physical_condition', models.CharField(choices=[('best', 'すごく良い'), ('good', '良い'), ('usual', '変わらず'), ('bad', '悪い'), ('worst', 'すごく悪い')], max_length=50, verbose_name='元気度数')),
                ('damage', models.CharField(choices=[('best', 'すごく良い'), ('good', '良い'), ('usual', '変わらず'), ('bad', '悪い'), ('worst', 'すごく悪い')], max_length=50, verbose_name='傷の状態')),
                ('clinic', models.CharField(choices=[('go', '通院日'), ('didnotgo', '通院なし')], max_length=50, verbose_name='通院日')),
                ('cut_nail', models.CharField(choices=[('cut', '爪を切った'), ('donot', '爪切ってない')], max_length=50, verbose_name='爪切り')),
                ('weight', models.IntegerField(max_length=50, verbose_name='体重')),
                ('comment', models.TextField(max_length=200, verbose_name='その他')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='イメージ')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('catname', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='record.catname', verbose_name='猫の名前')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
    ]
