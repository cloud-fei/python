#根据user name / group name 查询对应的 uid / gid
import pwd
import grp
uid=pwd.getpwnam('nginx').pw_uid
print(uid)
gid=grp.getgrnam('nginx').gr_gid
print(gid)

