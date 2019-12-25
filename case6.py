from lib.API_lib import addcourse,addteacher,loginin,listteacher,modifyteacher
import random
loginres,sessionid =loginin('auto','sdfsdfsdf')              #登录系统
classname1 = 'python'+str(random.randint(1,999999999))
classname2 = 'python'+str(random.randint(1,999999999))
add_course_res1 = addcourse(classname1,'python',7,sessionid)        #添加课程1
add_course_res2 = addcourse(classname2,'python2',6,sessionid)        #添加课程2
classid1 = add_course_res1['id']
classid2 = add_course_res2['id']
teachername1 = 'liumou'+str(random.randint(1,999999999))
courses1 =[{"id":classid1,"name":classname1}]
courses2 =[{"id":classid2,"name":classname2}]
add_teacher_res1 = addteacher(teachername1,'sq888','liumou','liumoulaoshi',courses1,6,sessionid)   #添加老师
teacherlist1 = listteacher(sessionid)['retlist']                  #获取添加老师后的列表
teacherid =add_teacher_res1['id']
teachername2 = 'lubenwei'+str(random.randint(1,999999999))
modify_teacher_res =modifyteacher(teacherid,teachername2,'666666','lubenwei','55kai',courses2,7,sessionid)  #修改老师信息
assert modify_teacher_res['retcode'] == 0                     #检查retcode
teacherlist2 = listteacher(sessionid)['retlist']               #获取修改老师后的列表

#检查修改后的教师信息
teacherinfo= None
for one in teacherlist2:
    if one not in teacherlist1:
        teacherinfo = one
        break
assert teacherinfo['courses']== [{'course_id':classid2}]
assert teacherinfo['id'] ==teacherid
assert teacherinfo['desc'] == '55kai'
assert teacherinfo['display_idx'] == 7
assert teacherinfo['realname'] == 'lubenwei'
assert teacherinfo['username'] == teachername2