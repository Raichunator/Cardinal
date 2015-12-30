from twisted.web import server, resource
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource

import json


class Github2Irc(object):
    def __init__(self, cardinal):
        """Register our event"""
        cardinal.event_manager.register('webserver.github_webhook', 1)
        self.callback_id = cardinal.event_manager.register_callback(
          'webserver.github_webhook', self.send_message)

    def send_message(self, cardinal, user, channel):
        cardinal.sendMsg(channel, "Am primit!")

    def close(self, cardinal):
        "Remove the event"""
        cardinal.event_manager.remove('webserver.github_webhook')


class Webserver(resource.Resource):
  isLeaf = True
  def render_GET(self, request):
    return "<html>Hello, world!</html>"

  def render_POST(self, request):
    data = json.loads(request.content.read())
    hook_name = data['hook']['name']
    cardinal.event_manager.fire('webserver.github_webhook')
    import ipdb;ipdb.set_trace()
    return ""


site = server.Site(Simple())
reactor.listenTCP(8973, site)

def setup():
    return Webserver()
