from lib.API_lib import addcourse,listcourse,loginin
import random
loginres,session=loginin('auto','sdfsdfsdf')
coursename = 'python'+ str(random.randint(1,999999999)) #生成随机的课程名
addres1 = addcourse(coursename,'pythontest','7',session)
courselist1 = listcourse(session)
addres2 = addcourse(coursename,'pythontest','7',session)
courselist2 = listcourse(session)
if addres2.get('retcode','NA') ==2:
    print('检查点1====pass:retcode等于2')
else:
    print('检查点1====fail:retcode不等于2')
if addres2.get('reason','NA') == '同名课程已存在':
    print('检查点2====pass:reason正确')
else:
    print('检查点2====fail:reason不正确')
courselist1 = listcourse(session)
assert courselist1 ==courselist2
print('用例2执行通过')