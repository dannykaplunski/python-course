from aiohttp import web
class Server:
    def __init__(self):
        self.port = 80
        self.app = web.Application()

    def run(self):
        self.app.add_routes([web.get("/a", self.a)])
        self.app.add_routes([web.get("/b", self.b)])
        web.run_app( self.app, port=self.port, )

    async def a(self, request):
        return web.json_response(dict(func='a'))
    async def b(self, request):
        return web.json_response(dict(func='b'))

server = Server()
server.run()