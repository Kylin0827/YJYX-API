from lib.API_lib import addcourse,addteacher,loginin,listteacher
import random
loginres,sessionid =loginin('auto','sdfsdfsdf')              #登录系统
classname = 'python'+str(random.randint(1,999999999))
add_course_res = addcourse(classname,'python',7,sessionid)        #添加课程
classid = add_course_res['id']
teachername = 'liumou'+str(random.randint(1,999999999))
courses =[{"id":classid,"name":classname}]
add_teacher_res1 = addteacher(teachername,'sq888','liumou','liumoulaoshi',courses,6,sessionid)   #添加老师
teacher_list1 =listteacher(sessionid)['retlist']           #获取添加老师后的教师列表
add_teacher_res2 = addteacher(teachername,'sq888','liumou','liumoulaoshi',courses,6,sessionid)   #添加相同的老师
assert add_teacher_res2['retcode'] == 1       #检查retcode
assert add_teacher_res2['reason'] ==f'登录名 {teachername} 已经存在'   #检查reason
teacher_list2 =listteacher(sessionid)['retlist']          #获取添加相同老师后的教师列表
assert teacher_list1 == teacher_list2             #检查添加老师前后列表是否相同