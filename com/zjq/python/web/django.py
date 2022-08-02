# Python Django 框架
# Django是高水准的Python编程语言驱动的一个开源模型．视图，控制器风格的Web应用程序框架，它起源于开源社区。使用这种架构，程序员可以方便、快捷地创建高品质、易维护、数据库驱动的应用程序。
# 这也正是OpenStack的Horizon组件采用这种架构进行设计的主要原因。另外，在Dj ango框架中，还包含许多功能强大的第三方插件，使得Django具有较强的可扩展性 。
# Django 项目源自一个在线新闻 Web 站点，于 2005 年以开源的形式被释放出来。Django 框架的核心组件有：
# 1. 用于创建模型的对象关系映射；
# 2. 为最终用户设计较好的管理界面；
# 3. URL 设计；
# 4. 设计者友好的模板语言；
# 5. 缓存系统。
# Django已经成为web开发者的首选框架，是一个遵循 MVC 设计模式的框架。MVC是Model、View、Controller三个单词的简写，分别代表模型、视图、控制器。Django其实也是一个MTV 的设计模式。
# MTV是Model、Template、View三个单词的简写，分别代表模型、模版、视图 [4]  。但是在Django中，控制器接受用户输入的部分由框架自行处理，
# 所以 Django 里更关注的是模型（Model）、模板(Template)和视图（Views），称为 MTV模式。
if __name__ == '__main__':

    # 在此添加创建django项目和初始化目录的命令
    create_django = 'django-admin startproject projectName'
    init_django = 'python manage.py startapp projectApp'

    installs = [
        "安装：pip install django",
        f"创建django项目命令：{create_django}",
        "进入目录：cd projectName",
        f"初始化django项目命令：{init_django}",
        "进一步查看教程：https://docs.djangoproject.com/zh-hans/3.2/"
    ]
    for step in installs:
        print(step)