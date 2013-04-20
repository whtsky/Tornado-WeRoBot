.. module:: tornado_werobot

Tornado-WeRoBot
===========================================
Tornado-WeRoBot 是一个帮助你将 WeRoBot 集成进 Tornado 的插件。
你可以通过调用 :func:`make_handler` 轻松的在你的 Tornado 应用中集成 `WeRoBot <http://werobot.readthedocs.org/en/latest/>`_ 。

入门
---------
最简单的 Hello World ::

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

API
----------

.. autofunction:: make_handler

ChangeLog
-----------

Version v0.1.0
~~~~~~~~~~~~~~~~

+ 框架可用。