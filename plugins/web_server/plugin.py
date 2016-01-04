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
	self.allowed_actions = ['created', 'opened']


    def render_GET(self, request):
        return "<html>Hello, world!</html>"

    def render_POST(self, request, **kwargs):
        data = json.loads(request.content.read())
	import pdb; pdb.set_trace()
        if 'action' in data:
	    if data['action'] in self.allowed_actions:
	        if 'issue' in data: 
 		    message = ("New issue: %s" % data['issue']['html_url']).encode('utf8')
           	    self.cardinal.sendMsg(self.config['channel'].encode('utf8'), message)

        return "<html><body>Issue comment recieved received</body></html>"

def setup(cardinal, config):
    site = server.Site(Webserver(cardinal, config))
    reactor.listenTCP(8973, site)

