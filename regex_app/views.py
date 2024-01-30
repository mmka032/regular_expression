from django.shortcuts import render

import re

def index(request):

    
    return render(request, 'regex_app/index.html')

def confirm(request):

    # 全てのデータを取得
    name=request.POST.get("name")
    age = request.POST.get("age")
    zip_code=request.POST.get("zip_code")
    tel=request.POST.get("tel")

    # 入力されたが値をチェック
    checkname =re.sub(" ","",name)
    checkage=re.match("[0-9]{1,3}",age)
    checkzip_code=re.match("([0-9]{3}-?[0-9]{4})",zip_code)
    checktel=re.match("([0-9]{3}-?[0-9]{4}-?[0-9]{4})",tel)

    #以下 それぞれマッチした値だけを保存
    if checkage and checkzip_code and checktel is not None:
        context = {
           "name":checkname,
           "age": checkage.group(),
           "zip_code":checkzip_code.group(),
           "tel":checktel.group(),
        }
        return render(request,"regex_app/confirm.html", context)  
    

    elif checkage and checkzip_code is not None:
            tel=""
            context = {
                "name":name,
                "age":age,
                "zip_code":zip_code,
            }
            return render(request,"regex_app:index.html",context)
    

    elif  checkage and checktel is not None:
            zip_code=""
            context={
                "name":name,
                "age":age,
                "tel":tel,
            }
            return render(request,"regex_app/index.html",context)
    

    elif checkzip_code and checktel is not None:
            age=""
            context={
                "name":name,
                "zip_code":zip_code,
                "tel":tel,
            }
            return render(request,"regex_app/index.html",context)
    

    elif  checkage is not None:
            zip_code = ""
            tel=""
            context = {
                "name":name,
                "age":age,
            }
            return render(request,"regex_app/index.html",context)
    

    elif checkzip_code is not None:
            age=""
            tel=""
            context = {
                "name":name,
                "zip_code":zip_code
            }
            return render(request,"regex_app/index.html",context)
    

    elif  checktel is not None:
            age=""
            zip_code=""
            context = {
                "name":name,
                "tel":tel,
            }
            return render(request,"regex_app/index.html",context)
    
    else:
            context={
                "name":name,
            }
            return render(request,"regex_app/index.html",context)
    
