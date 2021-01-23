from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Members
# Create your views here.
def login(req):
    print(dir(req))
    if req.method== 'GET':
        return render(req, 'login.html')
    elif req.method == 'POST':
        username = req.POST.get('username', None)
        useremail = req.POST.get('useremail', None)
        err = {}
        if not (useremail and username) :
            err['err'] = '유효성이 잘못되었습니다.'
            return render(req, 'login.html', err)

        else:
            member = Members.objects.get(username=username)

            if useremail == member.useremail :
                req.session['user'] = member.id
                return redirect('/members')

            return HttpResponse(f"<h1>{member.useremail}</h1>")
        # username = req.POST.get('username', None)
        # email = req.POST.get('password', None)

        # err = {}
        # if not(username and email) : 
        #     err['err'] ='비밀번호 오류'
        #     return  render(req, 'login.html', err)
        # else :
            ## db read
            ## session 만들기
        return redirect('/')
		
def index(req):
    #print(dir(req))
    print(req.GET.get('id',''))
    num = req.GET.get('id','') 
    if len(num) < 1:
        return HttpResponse("<h1>version 1 : dynamic page</h1>")
    return HttpResponse(f"<h2> 구구단 : {gugu(num)}</h2>")
def git(req):
    return HttpResponse("<h2>git version</h2>")
def lotto(req):
    return ""
def squred(i):
    return int(i) * int(i)
def gugu(i):
    str = ''
    for vi in range(9):
        str += f"<br>{int(i)} * {vi+1}  = {(vi+1)*int(i)}<br />"
    return str
def test(req):
    return HttpResponse("<h2>Test</h2>")
def signup(req):
    if req.method == 'POST' :
        username = req.POST['username']
        email = req.POST['email']
        member = Members(
            username = username,
            useremail = email
        )
       
        member.save()
        res_data = {}
        res_data['res'] = '등록성공'
        return render(req, 'index.html', res_data)
    return render(req, 'index.html')  
