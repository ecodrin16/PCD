from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import json
import cgi



cars = [
{"id":"1", "brand":"BMW", "fuel":"petrol", "price":"45000"},
{"id":"2", "brand":"Toyota", "fuel":"hybrid", "price":"33000"}

]

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        
    # GET sends back a Hello world message
    def do_GET(self):
        global cars
        if self.path == '/cars':
            self._set_headers()
            self.wfile.write(json.dumps(cars))
        else:
            _id = self.path.split('/')[2]
            flag = True
            if self.path.split('/')[1] == 'cars' and _id:
                for car in cars:
                    if car["id"] == _id:
                        self._set_headers()
                        self.wfile.write(json.dumps([car]))
                        flag = False
            if flag:
                self.send_response(404)
                self.end_headers()
                return
        
    def do_PUT(self):
        _id = None
        if len(self.path.split('/')) > 2:
            _id = self.path.split('/')[2]

        if self.path.split('/')[1] == 'cars' and _id is None:
            # read the message and convert it into a python dictionary
            length = int(self.headers.getheader('content-length'))
            responce = json.loads(self.rfile.read(length))
            
            global cars
            globals().update(cars=responce)
            self._set_headers()
            self.wfile.write(json.dumps(cars))
        
        else:
            if self.path.split('/')[1] == 'cars' and _id:             
                # read the message and convert it into a python dictionary
                length = int(self.headers.getheader('content-length'))
                responce = json.loads(self.rfile.read(length))


                # flag for looking for id , if it stays True means I could not find the id
                flag = True
                global cars
                for idx,car in enumerate(cars):
                    if car["id"] == _id:
                        self._set_headers()
                        #create local copy
                        copy_cars = cars
                        # update local copy
                        copy_cars.remove(copy_cars[idx])
                        copy_cars.append(responce)
                        #update global variable
                        globals().update(cars=copy_cars)
                        self.wfile.write(json.dumps([cars]))
                        flag = False
                if flag:
                    self.send_response(404)
                    self.end_headers()
                    return
    
    def do_POST(self):
        _id = self.path.split('/')[2]
        if self.path.split('/')[1] == 'cars' and _id:
            # read the message and convert it into a python dictionary
            length = int(self.headers.getheader('content-length'))
            responce = json.loads(self.rfile.read(length))
            
            global cars
            cars.append(dict(responce))

            # send the message back
            self._set_headers()
            self.wfile.write(json.dumps(cars))

    def do_DELETE(self):
        _id = None
        if len(self.path.split('/')) > 2:
            _id = self.path.split('/')[2]

        if self.path.split('/')[1] == 'cars' and _id is None:
            global cars
            globals().update(cars=None)
            self._set_headers()
            self.wfile.write(json.dumps(cars))
        else:
            if self.path.split('/')[1] == 'cars' and _id:
                # flag for looking for id , if it stays True means I could not find the id
                flag = True
                global cars
                for idx,car in enumerate(cars):
                    if car["id"] == _id:
                        self._set_headers()
                        #create local copy
                        copy_cars = cars
                        # update local copy
                        copy_cars.remove(copy_cars[idx])
                        globals().update(cars=copy_cars)
                        self.wfile.write(json.dumps([cars]))
                        flag = False
                if flag:
                    self.send_response(404)
                    self.end_headers()
                    return
        
def run(server_class=HTTPServer, handler_class=Server, port=8008):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    print ('Starting httpd on port %d...' % port)
    httpd.serve_forever()
    
if __name__ == "__main__":
    run()