from flask import Flask, render_template, Response
# from camera import Video
import urllib.request
import numpy as np
url='https://25giay.vn/wp-content/uploads/2021/09/jpg-la-gi.jpeg'
application=Flask(__name__)
@application.route('/')
def index():
    return render_template('index.html')
 #  return "Hello world!"

# def gen():
#     while True:
#         img_resp = urllib.request.urlopen(url)
#         imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
#         im = cv2.imdecode(imgnp,-1)
#         frame = im.tobytes()
#         yield(b'--frame\r\n'
#         b'Content-Type:  image/jpeg\r\n\r\n' + frame +
#         b'\r\n\r\n')

# @application.route('/video')
# def video():
#     return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

# application.run(debug=True)