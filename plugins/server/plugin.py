from twisted.web import server, resource
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource

import json


class Simple(resource.Resource):
  isLeaf = True
    def render_GET(self, request):
      return "<html>Hello, world!</html>"

    def render_POST(self, request):
      data = json.loads(request.content.read())
      return ""


site = server.Site(Simple())
reactor.listenTCP(8973, site)
reactor.run()

