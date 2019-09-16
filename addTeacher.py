import requests

#添加教师
#UI 登录--会员中心--教师列表--添加教师--输入信息--保存
#接口  登录--保存
#登录
lgn_url = 'http://127.0.0.1/admin.php?m=mgr/admin.chklogin&ajax=1'
lgn_data = {
    'username': 'admin',
    'password': 'admin',
}
data2 = requests.post(url=lgn_url, data=lgn_data)
#获取cookis
headers=data2.headers
d1 = headers['Set-Cookie']
d2=d1.split('=')
phpid1=d2[1].split(';')[0]
phpid2=d2[3].split('; ')[0]
#添加教师接口
add_teacher_url='http://127.0.0.1/admin.php?m=mgr/member2.saveMemberInfo&id='

headers={
    'Cookie':'PHPSESSID={}'.format(phpid2)
}
#输入信息
add_teacher_data={
    'username':'13066988000',
    'realname':'sss',
    'password':'123456',
    'sex':'0',
    'orid1':'123',
    'roleid':'5',
    'email': '1222@163.com',
    'phone': '13066988000',
    'location_p':'北京市',
    'location_c':'市辖区',
    'location_a':'东城区',
    'address':'深圳',
    'introduce':'what i ',
    'type': '1',
    }
#保存数据
result=requests.post(url=add_teacher_url,data=add_teacher_data,headers=headers)


