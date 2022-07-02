import time
import cv2
from flask import Flask, render_template, Response
import warnings
import urllib.request
import numpy as np
warnings.filterwarnings("ignore")
from src.lp_recognition import E2E

# urlCamera = 'https://scontent.xx.fbcdn.net/v/t1.15752-9/262719541_1245270879292641_3943295472295597787_n.jpg?_nc_cat=100&ccb=1-5&_nc_sid=aee45a&_nc_ohc=AbrqOdmxL7IAX9YGc5D&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AVKgFGOti5k9o0DJ9xdnokGZmwm_umUtUzuVck0ODYQHrA&oe=6295B5C6'
# urlCamera = "https://www.sample-videos.com/video123/mp4/480/big_buck_bunny_480p_30mb.mp4"
# urlCamera = "https://6993-2402-800-6294-9b5c-95f6-ede4-d3-2657.ngrok.io/cam-hi.jpg"

# https://6993-2402-800-6294-9b5c-95f6-ede4-d3-2657.ngrok.io

urlCamera= "https://7133-2402-9d80-417-1627-2433-51b2-f275-7c96.ap.ngrok.io/cam-hi.jpg"

application = Flask(__name__)


@application.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen():
    """Video streaming generator function."""
    # cap = cv2.VideoCapture(urlCamera)
    model = E2E()
    # Read until video is completed
    while (True):
        # Capture frame-by-frame

        #video
        # ret, img = cap.read()

        # anh
        img_resp = urllib.request.urlopen(urlCamera)
        imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        img = cv2.imdecode(imgnp, -1)


        # img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
        try:
            image = model.predict(img)
        except ValueError:
            image = img

        frame = cv2.imencode('.jpg', img)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(0.1)


@application.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
# application.run(port=5025)