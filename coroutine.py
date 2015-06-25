# coding: utf-8
import time

def consumer():
    r = 'start'
    while True:
        n = yield r # 此处,返回r 然后`等待`数据传入到 n
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'

def produce(c):
    print c.next() # 启动生成器, consumer执行到 yield处, 返回 'start', 然后等待下一个输入 
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) # 切换到consumer执行, 在yield处继续执行, n 被传给了
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

if __name__=='__main__':
    c = consumer()
    produce(c)
