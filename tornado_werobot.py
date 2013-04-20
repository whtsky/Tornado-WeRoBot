# -*- coding: utf-8 -*-
"""
Tornado-WeRoBot
---------------

Adds WeRoBot support to Tornado.

:copyright: (c) 2013 by whtsky.
:license: BSD, see LICENSE for more details.

Links
`````

* `documentation <https://tornado-werobot.readthedocs.org/>`_
"""

__version__ = '0.1'
__all__ = ['make_handler']

from werobot.robot import BaseRoBot
from werobot.parser import parse_user_msg
from tornado.web import RequestHandler


def make_handler(robot):
    """
    为一个 BaseRoBot 生成 Tornado Handler。

    :param robot: 一个 BaseRoBot 实例。
    :return: 一个标准的 Tornado Handler
    """
    assert isinstance(robot, BaseRoBot),\
        "RoBot should be an BaseRoBot instance."

    class WeRoBotHandler(RequestHandler):
            def prepare(self):
                timestamp = self.get_argument('timestamp', '')
                nonce = self.get_argument('nonce', '')
                signature = self.get_argument('signature', '')

                if not robot.check_signature(
                    timestamp=timestamp,
                    nonce=nonce,
                    signature=signature
                ):
                    self.finish('Unvailed request.')

            def get(self):
                echostr = self.get_argument('echostr', '')
                self.write(echostr)

            def post(self):
                body = self.request.body
                message = parse_user_msg(body)
                self.set_header("Content-Type",
                                "application/xml;charset=utf-8")

                reply = robot._get_reply(message)
                self.write(reply)
    return WeRoBotHandler
