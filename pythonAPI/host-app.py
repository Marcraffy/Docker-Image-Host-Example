import tornado.ioloop
import tornado.web
import random
from io import BytesIO
from os import listdir
from PIL import Image


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        image = getPicture()
        self.set_header('Content-type', 'image/jpeg')
        self.set_header('Content-length', len(image.getvalue()))
        self.write(image.read())
        self.finish()

def getPicture(): 
    path = './images/'
    imagesList = listdir(path)
    imagePath = imagesList[random.randint(0, len(imagesList) - 1)]
    img_io = BytesIO()
    Image.open(path + imagePath).save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return img_io

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(51115)
    tornado.ioloop.IOLoop.current().start()