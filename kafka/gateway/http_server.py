import cgi
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

import grpc

import event_pb2
import event_pb2_grpc
from settings import grpc_settings, http_settings


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get_content_type())

        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))

        with grpc.insecure_channel(grpc_settings.url) as channel:
            stub = event_pb2_grpc.EventStub(channel)

            try:
                stub.post_event(event_pb2.CreateEventRequest(message=message['message']))
            except grpc.RpcError as e:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.wfile.write(json.dumps({'error': str(e)}).encode())
            else:
                self.send_response(200)
                self.wfile.write(''.encode())

        self.end_headers()


def run(server_class, handler_class):
    server_address = (http_settings.host, http_settings.port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run(HTTPServer, CustomHTTPRequestHandler)
