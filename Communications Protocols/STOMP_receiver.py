import time
import stomp

class MyListener(object):
    def on_error(self, headers, message):
        print('received an error %s' % message)
    def on_message(self, headers, message):
        w_result = open("../flask/database/humdity.txt", "a")
        w_result.write(str(message)+"\n")
        w_result.close()
        print('received a message %s' % message)


conn = stomp.Connection10([('47.103.20.207',61613)])
conn.set_listener('logicServerQueue', MyListener())
conn.start()
conn.connect(wait=True)


# 发送消息到testQueue队列，指定consumerId='88.3@6006'
conn.send(body="humdity ready", destination='/humdity_response', headers={'consumerId': 'humdity_response'})
# 从testQueue队列中接收消息，用selector过滤，只接收consumerId = '88.3@6006'的消息
conn.subscribe(destination='/humdity_sender', headers={'selector' : "consumerId = 'humdity_sender'"})


while True:
    try:
        time.sleep(0)
    except:
        break

conn.disconnect()

time.sleep(0)
conn.disconnect()
