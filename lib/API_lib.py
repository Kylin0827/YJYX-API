import requests
import cfg
import pprint
import json
def loginin(username,password):
    res = requests.post(f'{cfg.host}/api/mgr/loginReq',
                        data={'username':username,
                              'password':password
                              })
    sessionid = res.cookies['sessionid']
    res_json = res.json()
    pprint.pprint(res.json())
    return res_json,sessionid
def addcourse(name,desc,idx,sessionid):
    res = requests.post(f'{cfg.host}/api/mgr/sq_mgr/',
                        data={'action':'add_course',
                              'data':f'''{{
                                  "name":"{name}",
                                  "desc":"{desc}",
                                  "display_idx":"{idx}"
                                }}
                                '''},
                        cookies ={'sessionid':sessionid})
    res_json = res.json()
    pprint.pprint(res.json())
    return res_json
def listcourse(sessionid):
    res = requests.get(f'{cfg.host}/api/mgr/sq_mgr/',
                       params={'action':'list_course',
                               'pagenum':'1',
                               'pagesize':'20'
                               },
                       cookies={'sessionid': sessionid})
    res_json = res.json()
    pprint.pprint(res.json())
    return res_json
def modifycourse(Cid,name,desc,idx,sessionid):
    res = requests.put(f'{cfg.host}/api/mgr/sq_mgr/',
                      data={'action': 'modify_course',
                            'id':{Cid},
                            'newdata': f'''{{
                                "name":"{name}",
                                "desc":"{desc}",
                                "display_idx":"{idx}"
                              }}
                              '''},
                      cookies={'sessionid': sessionid})
    res_json = res.json()
    pprint.pprint(res.json())
    return res_json
def deletecourse(Cid,sessionid):
    res = requests.delete(f'{cfg.host}/api/mgr/sq_mgr/',
                        data={'action':'delete_course',
                              'id':Cid
                              },
                        cookies ={'sessionid':sessionid})
    res_json = res.json()
    pprint.pprint(res.json())
    return res_json
def addteacher(username,password,realname,desc,courses,idx,sessionid):
    res = requests.post(f'{cfg.host}/api/mgr/sq_mgr/',
                        data ={'action':'add_teacher',
                               'data':f'''{{
                               "username":"{username}",
                                "password":"{password}",
                                "realname":"{realname}",
                                "desc":"{desc}",
                                "courses":{json.dumps(courses)},
                                "display_idx":{idx}
                                }}'''
                               },
                        cookies = {'sessionid':sessionid})
    res_json = res.json()
    pprint.pprint(res.json())
    return res_json
def listteacher(sessionid):
    res = requests.get(f'{cfg.host}/api/mgr/sq_mgr/',
                       params={'action':'list_teacher',
                               'pagenum':'1',
                               'pagesize':'20'
                               },
                       cookies={'sessionid': sessionid})
    res_json = res.json()
    pprint.pprint(res.json())
    return res_json
def modifyteacher(id,username,password,realname,desc,courses,idx,sessionid):
    res = requests.put(f'{cfg.host}/api/mgr/sq_mgr/',
                        data ={'action':'modify_teacher',
                               'id':{id},
                               'newdata':f'''{{
                               "username":"{username}",
                                "password":"{password}",
                                "realname":"{realname}",
                                "desc":"{desc}",
                                "courses":{json.dumps(courses)},
                                "display_idx":{idx}
                                }}'''
                               },
                        cookies = {'sessionid':sessionid})
    res_json = res.json()
    pprint.pprint(res.json())
    return res_json
def deleteteacher(id,sessionid):
    res = requests.delete(f'{cfg.host}/api/mgr/sq_mgr/',
                        data ={'action':'delete_teacher',
                               'id':{id}
                               },
                        cookies = {'sessionid':sessionid})
    res_json = res.json()
    pprint.pprint(res.json())
    return res_json