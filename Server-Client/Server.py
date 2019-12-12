import time
from http.server import BaseHTTPRequestHandler, HTTPServer

import base64

HOST_NAME = '10.7.177.93'
PORT_NUMBER = 4000


class MyHandler(BaseHTTPRequestHandler):
    

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        # Nous avons recu l'information du client
        print ("Nous avons recu l'information")
        # Signal de reponse 
        content_length = int(self.headers['Content-Length'])
        # Information
        data_received = self.rfile.read(content_length)
        imgdata = base64.b64decode(data_received)
        # Ecrire dans le fichier
        f = open('imagen3.jpeg', 'wb')
        f.write(imgdata)
        f.close()
        print ("Transfert reussie")

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

    def do_GET(self):
        print ("Requet recu")
        try:
            print( " Cherche l'image" )
            f = open("imagen.jpeg") 
            print (" Image trouvee ")
            # On envoie le code de response
            self.send_response(200)
            # On envoie le header
            self.send_header('Content-type','image/jpeg')
            self.end_headers()
            # On envoie l'image
            print ("Envoyer image")
            self.wfile.write(f.read())
            print ( "L'image a ete envoyee" )
            f.close()
            return
        except IOError:
            self.send_error(404, 'Fichier pas trouve')


if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), 'Serveur commence - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    print("Serveur ferme")
    httpd.server_close()
    print(time.asctime(), 'Serveur ferme - %s:%s' % (HOST_NAME, PORT_NUMBER))