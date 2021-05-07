from wxpy import *
bot = Bot()
my_friends = bot.friends().search('虢梁', sex=MALE, city='济宁')
friend = ensure_one(my_friends)
friend.send('这是通过Python发送给你的消息')


#
# import itchat
# #登录微信
# itchat.auto_login(enableCmdQR=True)#enableCmdQR在终端或命令行中为True,在notebook中为-1
#
# def sendMessageToWechat(markName=u'虢梁',message=u'已经处理完毕'):
#     '''
#     markName: 微信备注的名字
#     message: 要发送的内容
#     eg: sendMessageToWechat(markName=u'鹏举',message=u'已经处理完毕')
#     '''
#     #想给谁发信息，先查找到这个朋友
#     users = itchat.search_friends(name=markName)
#     if users:
#         #找到UserName
#         userName = users[0]['UserName']
#         itchat.send(message,toUserName = userName)
#     else:
#         print('通讯录中无此人')
#
#
# from time import sleep
#
#
# def func1():
#     sleep(20)
# def func2():
#     sleep(40)
#
# func1()
# sendMessageToWechat(markName=u'虢梁',message=u'func1已经处理完毕')
# func2()
# sendMessageToWechat(markName=u'虢梁',message=u'func2已经处理完毕')
