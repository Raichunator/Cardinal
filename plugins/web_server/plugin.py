from twisted.web import server, resource
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource

import json
from cardinal import bot

class Webserver(resource.Resource):
    isLeaf = True

    def __init__(self, cardinal, config):
        self.cardinal = cardinal
	self.config = config

    def render_GET(self, request):
        return "<html>Hello, world!</html>"

    def render_POST(self, request, **kwargs):
        data = json.loads(request.content.read())
        hook_name = data['hook']['name']
	self.cardinal.sendMsg(
	    self.config['channel'].encode('utf8'), str(hook_name))
        return "<html><body>Payload received</body></html>"

def setup(cardinal, config):
    site = server.Site(Webserver(cardinal, config))
    reactor.listenTCP(8973, site)

