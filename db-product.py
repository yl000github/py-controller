# #!/usr/bin/env python
# # coding=utf-8
# 
# import MySQLdb  
# from sshtunnel import SSHTunnelForwarder  
# import ConfigParser
# cf = ConfigParser.ConfigParser()
# cf.read("d:/config/mysql.conf")
# print cf.get('product', 'ssh.ip')
# def getConfig(key):
#     return cf.get('product', key)
# with SSHTunnelForwarder(  
#          (getConfig('ssh.ip'), 22),    #B机器的配置  
#          ssh_password=getConfig('ssh.password'),  
#          ssh_username=getConfig('ssh.username'),  
#          remote_bind_address=(getConfig('mysql.ip'), 3306)
#          ) as server:  #A机器的配置  
#     
#     print 'server start'
# #     print server
# #     print getConfig('mysql.username')
# #     print getConfig('mysql.password')
#     conn = MySQLdb.connect(host='127.0.0.1',              #此处必须是是127.0.0.1  
#                            port=3306,  
#                            user=getConfig('mysql.username'),  
#                            passwd=getConfig('mysql.password'),  
# #                            db='dlb_v2'
#                            )  
#     
#     cur=conn.cursor()
# #     cur.execute('select *from users')
#     cur.execute('show databases')
#     print cur.fetchall()
#     conn.close()
#     