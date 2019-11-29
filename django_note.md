# django-study (2019.11.27)

1. `当 python3 manage.py makemigrations 出现错误的时候的解决方式`
```
* python3 manage.py makemigrations your_app_label // will make a new initial migration for your app
*  python3 manage.py migrate --fake-initial // detect that you have an initial migration and that the tables it wants to create already exist, and will mark the migration as already applied
```

2. `有可能遇到 auth_user table not to find 的 solve way`
```
把 from django.contrib.auth.xxx 相关内容屏蔽掉，再执行
* python3 manage.py makemigrations your_app_label
* python3 manage.py migrate --fake-initial
```
3. `使用simpleui美化 django-admin 界面`
```
* pip3 install django-simpleui
* pip3 list 查看是否 install successful
* 新建一个 static 目录，和项目app 在同一级目录
* 项目setting.py add
   * INSTALLED_APPS 中在 admin上面添加 'simpleui'
   * STATIC_URL = '/static/'
   * STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    ]

   * 然后 python3 manage.py collectstatic // 收集 staticfile 到目录 static中
   * STATIC_ROOT = os.path.join(BASE_DIR, 'static')
* urls.py add
   * from django.conf.urls.static import static
   * from django.conf import settings
   * urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  // 这个操作为了当我们使用 uwsgi + nginx 能正常访问 static 目录
*  uwsgi -x djangochina_socket.xml  // 即可正常访问 
```
* [uwsgi部署django项目找不到static目录的解决方法](https://blog.csdn.net/mikyz/article/details/75348530)

