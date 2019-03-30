import time
import stomp


class MyListener(object):
    def on_error(self, headers, message):
        print('received an error %s' % message)

    def on_message(self, headers, message):
        print('received a message: %s' % message)


def STOPM_sender(value):

    conn = stomp.Connection10([('47.103.20.207',61613)])
    conn.set_listener('', MyListener())
    conn.start()
    conn.connect()

    # 发送消息到testQueue队列，指定consumerId='88.3@6006'
    conn.send(body=value, destination='/humdity_sender', headers={'consumerId': 'humdity_sender'})
    # 从testQueue队列中接收消息，用selector过滤，只接收consumerId = '88.3@6006'的消息
    conn.subscribe(destination='/humdity_response', headers={'selector': "consumerId = 'humdity_response'"})
    conn.disconnect()

# STOPM_sender("hello")