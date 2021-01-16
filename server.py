import threading
from flask import Flask, render_template
from picamera import PiCamera, Color
from time import sleep
import datetime as dt

app = Flask(__name__, static_url_path="", static_folder="templates")

def take_picture():
    camera = PiCamera()
    while True:
        camera.start_preview()
        camera.annotate_background = Color('black')
        camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sleep(5)
        camera.capture("/home/pi/Int-Run-Image/templates/image.jpg")
        camera.stop_preview()
th = threading.Thread(target=take_picture)
th.start()

@app.route('/')
def show_index():
    return render_template("index.html")

def run_server_api():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    run_server_api()

