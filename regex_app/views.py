from django.shortcuts import render 

import re

def index(request):

    return render(request, "regex_app/index.html")

def confirm(request):

    # 全てのデータを取得
    name = request.POST.get("name")
    age = request.POST.get("age")
    zip_code = request.POST.get("zip_code")
    tel = request.POST.get("tel")

    # 入力されたが値をチェック
    checkname = re.sub("\s", "", name)
    checkage = re.match("[0-9]{1,3}", age)
    checkzip_code = re.match("([0-9]{3}-?[0-9]{4})", zip_code)
    checktel=re.match("([0-9]{3}-?[0-9]{4}-?[0-9]{4})" ,tel)

    #以下 全ての値がマッチしたらconfirm.htmlへ遷移
    if checkage and checkzip_code and checktel is not None:
        
        context = {
           "name": checkname,
           "age": checkage.group(),
           "zip_code": checkzip_code.group(),
           "tel": checktel.group(),
        }
        
        return render(request, "regex_app/confirm.html", context)  

    #以下 それぞれマッチした値だけを保存、マッチしなかった場合はエラーメッセージを表示
    elif checkage and checkzip_code is not None:
            tel = ""

            context = {
                "name": checkname,
                "age": age,
                "zip_code": zip_code,
                'tel': "",
            }

            return render(request, "regex_app/index.html", context)
    

    elif  checkage and checktel is not None:
            zip_code = ""

            context = {
                "name": checkname,
                "age": age,
                'zip_code': "",
                "tel": tel,
            }

            return render(request, "regex_app/index.html", context)
    

    elif checkzip_code and checktel is not None:
            age = ""

            context = {
                "name": checkname,
                'age': "",
                "zip_code": zip_code,
                "tel": tel,
            }

            return render(request, "regex_app/index.html", context)
    
    elif  checkage is not None:
            zip_code = ""
            tel = ""

            context = {
                "name": checkname,
                "age": age,
                'zip_code': "",
                'tel': "",
            }

            return render(request, "regex_app/index.html", context)
    

    elif checkzip_code is not None:
            age = ""
            tel = ""

            context = {
                "name": checkname,
                "age" : "",
                "zip_code": zip_code,
                "tel" : "",
            }

            return render(request, "regex_app/index.html", context)
    
    

    elif  checktel is not None:
            age = ""
            zip_code = ""

            context = {
                "name": checkname,
                "age" : "",
                "zip_code" : "",
                "tel": tel,
            }

            return render(request, "regex_app/index.html", context)
    

    else:
        
        context = {
            "name": checkname,
            "age":"",
            "zip_code":"",
            "tel":"",
        }
            
        return render(request, "regex_app/index.html", context)