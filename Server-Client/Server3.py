import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from reconnaissance_visage import *

import base64


path_base="./Base_visages"
path_image_test='hugo.jpeg'

HOST_NAME = '10.7.177.93'
PORT_NUMBER = 4000


class MyHandler(BaseHTTPRequestHandler):
    
    # def do_HEAD(self):
    #     self.send_response(200)
    #     self.send_header('Content-type', 'text/html')
    #     self.end_headers()

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        # Recibe la informacion desde el cliente
        print ("Se ha recibido la solicitud")
        # Senal de respuesta
        content_length = int(self.headers['Content-Length'])
        # Recibe la informacion en cuestion
        data_received = self.rfile.read(content_length)
        imgdata = base64.b64decode(data_received)
        # Escribe el archivo
        f = open('imagen3.jpeg', 'wb')
        f.write(imgdata)
        res=reconnaissance_visage(path_base,path_image_test)
        print(res)
        f.close()
        print ("Se ha realizado la trasferencia exitosamente")

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

    def do_GET(self):
        print ("Solicitud producida")
        try:
            print( " Buscando la imagen" )
            f = open("imagen.jpeg") #open requested file
            print (" Imagen encontrada ")
            # Se envia un codigo de respuesta
            self.send_response(200)
            # Se envia el header
            self.send_header('Content-type','image/jpeg')
            self.end_headers()
            # Se envia la imagen
            print ("Mandando imagen")
            self.wfile.write(f.read())
            print ( "La imagen ha sido enviada exitosamente" )
            f.close()
            return
        except IOError:
            self.send_error(404, 'Archivo no encontrado')

    # def handle_http(self, status_code, path):
    #     self.send_response(status_code)
    #     self.send_header('Content-type', 'text/html')
    #     self.end_headers()
    #     content = '''
    #     <html><head><title>Title goes here.</title></head>
    #     <body><p>This is a test.</p>
    #     <p>You accessed path: {}</p>
    #     </body></html>
    #     '''.format(path)
    #     return bytes(content, 'UTF-8')

    # def respond(self, opts):
    #     response = self.handle_http(opts['status'], self.path)
    #     self.wfile.write(response)

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    print("Server closes")
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))