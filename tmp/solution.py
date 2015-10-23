#!/usr/bin/env python
# encoding: utf-8

'''
主要区别就是tuple是immutable的，
list的mutable
'''


'''
平时感觉就是这几种方式：
一种是直接第三方登陆，这种的优势是用户一键登陆，方便快捷。但是我们
能拿到的消息就比较少

第二种
通过第三登陆后，用户再绑定注册email 手机。
这种的优势是我们可以得到用户的消息，用户注册的话会比较烦。

最后一种是直接email 或者 手机号验证注册。
简单快捷。脱离第三方

同时借鉴知乎上一哥们的回答：
把一套用户信息升级为sso系统，可以像google那样所有的应用服务都为一个账号。
'''


'''
RESTful API
MVC

我个人的经验来说的话就是服务模块一定要分开，把耦合度降到最低。
业务层一定不能混杂着DB操作，同样DB也是不能混着其他不相干的操作。

'''

'''
系统消息是相当于发送广播，用户之间是p2p
有个消息队列，这个消息队列应该在服务器端，每发送消息都应该有
sender receiver。
通过comet技术 或者h5 web_socket类似技术实现推送就可以了。
每次请求要请求 receiver 为自己的就可以了。
'''

