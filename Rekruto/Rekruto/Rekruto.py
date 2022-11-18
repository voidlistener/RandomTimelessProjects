
import cherrypy
@cherrypy.expose
class Hello_There(object):
    @cherrypy.tools.accept(media='text/plain')
    def GET(self, name="Rekruto", message="Давай дружить!"):
        return "Hello {}! {}!".format(name, message)
if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.quickstart(Hello_There(), '/', conf)