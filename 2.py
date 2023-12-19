# docString  : not ignore and you can print it """ text """ use in function - class - module 
# هدف نشان دادن این است که تابع چی هست برای کاربر اگر خارج از تابع و کلاس ها تعریف کنیم مفسر به عنوان کامنت در نظر می گیرد
#
# comments : ignore to run
# توضیحات برای برنامه نویسی

def prin(name):
    """" that function for print input function """
    print(name)

prin("mohsen" ); print(prin.__doc__)