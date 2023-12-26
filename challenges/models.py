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
    exercise = models.CharField(max_length=30, default='', validators=[exercise_regex])
    disription = models.TextField(default='')
    visible = models.BooleanField(default=False)
    
    category = models.CharField(
        max_length=30,
        choices = CATEGORIES,
        default='Misc'
    )
    
    reference_url = models.URLField(default="")
    explanation_url = models.URLField(default="")
    
    # 日時
    created_at = models.DateTimeField(auto_now_add=True) #データ挿入時
    updated_at = models.DateTimeField(auto_now=True) #データ更新時
    
    def __str__(self):
        return self.exercise
    
    class Meta:
        verbose_name = "Exercise"
    
# 課題クラス:多
class Challenge(models.Model):
    identifier = models.CharField(max_length=50, unique=True, validators=[RegexValidator(regex='^[0-9a-zA-Z]*$')])
    title_regex = RegexValidator(regex=r'^[0-9]{2}[.]{1}')
    title = models.CharField(max_length=30, default='', validators=[title_regex])
    exerciseName = models.ForeignKey(Exercise, on_delete=models.SET_DEFAULT, default='実戦問題')
    category = models.CharField(
        max_length=30,
        choices = CATEGORIES,
        default='Misc'
    )
    problem = models.TextField(default='')
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3000)], default=0)
    flag = models.CharField(max_length=100, default='')
    visible = models.BooleanField(default=False)
    
    #ヒント
    hint_one = models.CharField(max_length=100, blank=True, default="")
    hint_two = models.CharField(max_length=100, blank=True, default="")
    hint_three = models.CharField(max_length=100, blank=True, default="")
    
    # 日時
    created_at = models.DateTimeField(auto_now_add=True) #データ挿入時
    updated_at = models.DateTimeField(auto_now=True) #データ更新時
    
    # 正解数
    cleared_counts = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Challenges"
        
class Submit(models.Model):
    # 外部参照の理由：user削除時に点数が残ってしまうから。
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, to_field="username")
    
    # 外部参照しない理由：問題が削除されたときに、点数情報も変わってしまうため。
    identifier = models.CharField(max_length=50, validators=[RegexValidator(regex='^[0-9a-zA-Z]*$')],) 
    
    def __str__(self):
        submit_title = str(self.user) + ":" + str(self.identifier)
        return submit_title