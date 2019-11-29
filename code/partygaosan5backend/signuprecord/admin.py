from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(PartyName)
class MsgAdmin(admin.ModelAdmin):
    # 显示数据库里面order出来的数据
    list_display = ('name','telephone')
    # 每页记录数
    list_per_page = 25
    pass

    class Meta:
        verbose_name = '报名记录'      # 重定义 MsgAdmin 的名字
        verbose_name_plural = verbose_name



'''
class NameAdmin(admin.ModelAdmin):
    # 列表显示字段 name
    list_display = ('name')
    # 每页记录数
    list_per_page = 25
    # 查询字段
    search_fields = ('name')
'''

'''


class NameAdmin(admin.ModelAdmin):
    list_display = ('name', 'article_count')

    def article_count(self, obj):
        return PartyName.objects.filter(tag=obj).count()

admin.site.register(PartyName, NameAdmin)
'''