from lib.API_lib import addcourse,addteacher,loginin,listteacher,deleteteacher
import random
loginres,sessionid =loginin('auto','sdfsdfsdf')              #登录系统
classname = 'python'+str(random.randint(1,999999999))
add_course_res = addcourse(classname,'python',7,sessionid)        #添加课程
classid = add_course_res['id']
teachername = 'liumou'+str(random.randint(1,999999999))
courses =[{"id":classid,"name":classname}]
add_teacher_res1 = addteacher(teachername,'sq888','liumou','liumoulaoshi',courses,6,sessionid)   #添加老师
teacher_list1 =listteacher(sessionid)['retlist']           #获取添加老师后的教师列表
teacherid =add_teacher_res1['id']
delete_teacher_res =deleteteacher(teacherid,sessionid)
assert delete_teacher_res['retcode'] == 0        #检查retcode
teacher_list2 =listteacher(sessionid)['retlist']           #获取删除老师后的教师列表

#检查删除后的教师信息
teacherinfo= None
for one in teacher_list1:
    if one not in teacher_list2:
        teacherinfo = one
        break
assert teacherinfo['id'] ==teacherid