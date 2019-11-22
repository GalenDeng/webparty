# python 知识积累 （2019.11.20）

1. `class Meta`
```
class Main(models.Model):
    img = models.CharField(max_length=200) # 图片
    name = models.CharField(max_length=100) # 名称
    trackid = models.CharField(max_length=16) # 通用id
 
    class Meta:
                db_table = 'name'   # 指定这个类在数据库中表单的名字
                ordering = ['order_date'] # 按升序排列
                abstract = True        #抽象类
```
2. `question to resolve`
```
You are trying to add a non-nullable field 'name' to contact without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 


解决方法：
先给'name'任意初始值：name = models.CharField(max_length=50, default='abc')
然后执行：python manage.py makemirations
再执行：python manage.py migrate
```
3. `operation`
```
*  killall -9 uwsgi
*  uwsgi -x djangochina_socket.xml
```