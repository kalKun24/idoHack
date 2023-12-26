from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator
from accounts.models import CustomUser

# カテゴリ
CATEGORIES = (('WebExploitation', 'WebExploitation'), 
              ('Cryptography', 'Cryptography'), 
              ('Reversing', 'Reversing'), 
              ('Pwnable', 'Pwnable'), 
              ('Forensics', 'Forensics'),
              ('Network', 'Network'),
              ('GenerallSkill', 'GenerallSkill'),
              ('Misc', 'Misc')
              )

# 演習クラス(課題の集合):1
class Exercise(models.Model):
    exercise_regex = RegexValidator(regex=r'^#[0-9]{2}')
    exercise = models.CharField(max_length=30, default='', validators=[exercise_regex], verbose_name="演習名")
    disription = models.TextField(default='', verbose_name="説明")
    visible = models.BooleanField(default=False, verbose_name="ユーザへの公開")
    
    category = models.CharField(
        max_length=30,
        choices = CATEGORIES,
        default='Misc',
        verbose_name="カテゴリー"
    )
    
    reference_url = models.URLField(default="", verbose_name="教科書URL")
    explanation_url = models.URLField(default="", verbose_name="解説URL")
    
    # 日時
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時") #データ挿入時
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時") #データ更新時
    
    def __str__(self):
        return self.exercise
    
    class Meta:
        verbose_name = "Exercise"
    
# 課題クラス:多
class Challenge(models.Model):
    identifier = models.CharField(max_length=50, unique=True, validators=[RegexValidator(regex='^[0-9a-zA-Z]*$')], verbose_name="識別子")
    title_regex = RegexValidator(regex=r'^[0-9]{2}[.]{1}')
    title = models.CharField(max_length=30, default='', validators=[title_regex], verbose_name="タイトル")
    exerciseName = models.ForeignKey(Exercise, on_delete=models.SET_DEFAULT, default='実戦問題', verbose_name="演習名")
    category = models.CharField(
        max_length=30,
        choices = CATEGORIES,
        default='Misc',
        verbose_name="カテゴリー"
    )
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3000)], default=0, verbose_name="配点")
    flag = models.CharField(max_length=100, default='', verbose_name="フラグ")
    visible = models.BooleanField(default=False, verbose_name="ユーザへの公開")
    
    problem = models.TextField(default='', verbose_name="問題文")
    
    #ヒント
    hint_one = models.CharField(max_length=100, blank=True, default="" , verbose_name="ヒント1")
    hint_two = models.CharField(max_length=100, blank=True, default="", verbose_name="ヒント2")
    hint_three = models.CharField(max_length=100, blank=True, default="", verbose_name="ヒント3")
    
    # 正解数
    cleared_counts = models.IntegerField(default=0, verbose_name="正解者数")
    
    # 日時
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時") #データ挿入時
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時") #データ更新時
    
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Challenges"
        
class Submit(models.Model):
    # 外部参照の理由：user削除時に点数が残ってしまうから。
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, to_field="username", verbose_name="ユーザ")
    
    # 外部参照しない理由：問題が削除されたときに、点数情報も変わってしまうため。
    identifier = models.CharField(max_length=50, validators=[RegexValidator(regex='^[0-9a-zA-Z]*$')], verbose_name="課題") 
    
    def __str__(self):
        submit_title = str(self.user) + ":" + str(self.identifier)
        return submit_title