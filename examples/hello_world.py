import tornado.ioloop
import tornado.web
from werobot import WeRoBot
from tornado_werobot import make_handler

robot = WeRoBot(token='token')


@robot.handler
def hello(message):
    return 'Hello World!'

application = tornado.web.Application([
    (r"/", make_handler(robot)),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()