from lib.API_lib import addcourse,listcourse,loginin,modifycourse
import random
loginres,session=loginin('auto','sdfsdfsdf')             #登录
coursename = 'python'+ str(random.randint(1,999999999))              #生成随机的课程名
addres = addcourse(coursename,'pythontest','7',session)          #添加课程
Cid = addres['id']
courselist1 = listcourse(session)['retlist']               #获取添加课程后的课程列表
coursename2 = 'python'+ str(random.randint(1,999999999))           #生成随机的课程名
modifyres = modifycourse(Cid,coursename2,'testdesc','666',session)            #修改课程
if modifyres.get('retcode','NA') == 0:
    print('检查点1====pass:retcode等于0')
else:
    print('检查点1====fail:retcode不等于0')
courselist2 = listcourse(session)['retlist']            #获取修改课程后的课程列表
assert len(courselist1) == len(courselist2)
course = None
for one in courselist2:
    if one not in courselist1:
        course = one
        break
assert course['id'] == Cid
assert course['name'] == coursename2
assert course['desc'] == 'testdesc'
assert course['display_idx'] == 666
print('用例3执行通过')