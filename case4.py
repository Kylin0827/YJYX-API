from lib.API_lib import addcourse,listcourse,loginin,deletecourse
import random
loginres,session=loginin('auto','sdfsdfsdf')             #登录
coursename = 'python'+ str(random.randint(1,999999999))              #生成随机的课程名
addres = addcourse(coursename,'pythontest','7',session)          #添加课程
Cid = addres['id']
courselist1 = listcourse(session)['retlist']               #获取添加课程后的课程列表
deleteres = deletecourse(Cid,session)            #删除课程
courselist2 = listcourse(session)['retlist']               #获取删除课程后的课程列表
assert len(courselist1) - len(courselist2) ==1         #检查删除后的列表课程是否少1
courses = []
for one in courselist1:
    if one not in courselist2:
        courses.append(one)
assert len(courses) ==1
course = courses[0]
assert course['id'] == Cid
print('用例4执行通过')