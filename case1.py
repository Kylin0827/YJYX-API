from lib.API_lib import addcourse,listcourse,loginin
import random
loginres,session=loginin('auto','sdfsdfsdf')
courselist1 = listcourse(session)['retlist'] #获取添加课程前的课程列表
coursename = 'python'+ str(random.randint(1,999999999)) #生成随机的课程名
addres = addcourse(coursename,'pythontest','7',session)
if addres.get('retcode','NA') ==0:
    print('检查点1====pass:课程创建成功')
else:
    print('检查点1====fail:课程创建失败')
courselist2 = listcourse(session)['retlist'] #获取添加课程后的课程列表
if len(courselist2) - len(courselist1) == 1:
    print('检查点2====pass:课程列表多了一个课程')
else:
    print('检查点2====fail:课程列表没有增加一个课程')
course = None
for one in courselist2:
    if one not in courselist1:
        course = one
        break
assert course['name'] == coursename
assert course['desc'] == 'pythontest'
assert course['display_idx'] == 7
assert course['id'] == addres['id']
print('用例1执行通过')