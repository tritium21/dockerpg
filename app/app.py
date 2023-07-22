import logging
import socket

from aiohttp import web

app = web.Application()
logging.basicConfig(level=logging.DEBUG)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    ip = get_ip()
    logging.debug(f"Hit on machine {ip}")
    return web.Response(text=f"Hello, world from {ip}")

app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app)
