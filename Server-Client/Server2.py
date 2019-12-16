from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
import base64
from reconnaissance_visage import *
path_base = "/home/gonzalo/Documentos/Gonzalo/Java/Java_HTTP/PROJ942/Proj942/Server-Client/Base_visages"
path_image_test = 'myimage.jpeg'



#Se crea una clase HTTPRequestHandler propia
class MiHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        #Recibe la informacion desde el cliente
        print ("On a recu la raquette")
        #Senal de respuesta
        content_length = int(self.headers.getheader('content-length',0))
        #content_length = 100
        #content_length = 1000
        print("ContentLength")
        print(content_length)
        #Recibe la informacion en cuestion
        data_received = self.rfile.read(content_length)

        print (data_received)
        imgdata = base64.b64decode(data_received)
        #Escribe el archivo
        f = open('myimage.jpeg', 'wb')
        f.write(imgdata)
        f.close()
        print ("Transfert reusie")
        #print(data_received)
        #self.wfile.write(200
        self.send_response(200)
        res = reconnaissance_visage(path_base, path_image_test)
        print res





    def do_GET(self):
        print ("Raquette envoyee")
        try:
            print( "Cherche l'image" )
            f = open("imagen.jpeg") #open requested file
            print (" Image trouvee ")
            #Se envia un codigo de respuesta
            self.send_response(200)
            #Se envia el header
            self.send_header('Content-type','image/jpeg')
            self.end_headers()
            #Se envia la imagen
            print ("En train de envoyer l'image")
            self.wfile.write(f.read())
            print ( "L'image a ete envoyee" )
            f.close()
            return
        except IOError:
            self.send_error(404, 'Fichier pas trouve')



def runServer():
    #res = reconnaissance_visage(path_base, path_image_test)
    #print res
    print ("Initialiser le Serveuer")
    print('Serveur http en train de commencer...')
    server_address = ('10.7.177.93', 4000)
    httpd = HTTPServer(server_address, MiHTTPRequestHandler)
    print('Le serveur http en marchant...')
    httpd.serve_forever()

if __name__ == '__main__':
  runServer()




