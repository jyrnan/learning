from collections import deque

class ActorScheduler:
    def __init__(self):
        self._actors = {}           # Mapping of names to actors
        self._msg_queue = deque()   # Message queue 用来存储将要发送给actor的指令

    def new_actor(self, name, actor):
        ''' Admit a newly started actor to the scheduler and give it  a name'''
        self._msg_queue.append((actor, None)) # 相当于添加生成器的第一个动作指令： next(), 来启动生成器
        self._actors[name] = actor

    def send(self, name, msg):
        ''' Send a message to a named actor ，其实就是把给某名字的actor的指令存储在队列中'''
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor, msg)) #存贮的是包含actor和指令(msg)的元祖

    def run(self):
        ''' Run as long as there are pending messages.'''
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                actor.send(msg)
            except StopIteration:
                pass


# Example use
if __name__ == '__main__':
    def printer():
        while True:
            msg = yield
            print('Got:', msg)

    def counter(sched):
        while True:
            # Recieve the current count
            n = yield
            if n == 0:
                break
            # Send to the printer task
            sched.send('printer', n)
            # Send the next count to the counter task(recursive)递归？
            sched.send('counter', n-1)

    sched = ActorScheduler()
    # Create the initial actors
    sched.new_actor('printer', printer())
    sched.new_actor('counter', counter(sched))
    
    # Send an initial message to the counter to initiate
    sched.send('counter', 10)
    sched.run()

