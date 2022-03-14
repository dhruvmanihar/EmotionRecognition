import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import time
from tkinter import *


class Table:
    def __init__(self, root):
        y,x = 7,2

        self.table = [[0 for x in range(x)] for y in range(y)]
        print(self.table)
        for i in range(7):
            for j in range(2):
                self.table[i][j] = Entry(root, width=20, fg='blue',
                                         font=('Arial', 16, 'bold'))

                self.table[i][j].grid(row=i, column=j)
                # self.e(END, lst[i][j])


root = Tk()
t = Table(root)

t.table[0][0].insert(0, "Anger")
t.table[1][0].insert(0, "Disgust")
t.table[2][0].insert(0, "Fear")
t.table[3][0].insert(0, "Happy")
t.table[4][0].insert(0, "Sad")
t.table[5][0].insert(0, "Surprise")
t.table[6][0].insert(0, "Neutral")

def analyze_face(cv2_read_image):
    prediction = DeepFace.analyze(cv2_read_image)
    return prediction


def draw_rectangle(cv2_read_image, face_cascade):
    gray = cv2.cvtColor(cv2_read_image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(cv2_read_image, (x, y), (x + w, y + h), (255, 255, 255), 10)
    # plt.imshow(cv2.cvtColor(cv2_read_image, cv2.COLOR_BGR2RGB))
    # plt.show()


def write_emotion(cv2_read_image, prediction):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(
        cv2_read_image,
        prediction["dominant_emotion"],
        (50, 50),
        font,
        2,
        (255, 255, 255),
        2,
        cv2.LINE_4,
    )
    # plt.imshow(cv2.cvtColor(cv2_read_image, cv2.COLOR_BGR2RGB))
    # plt.show()


def main():
    img = cv2.imread("image3.jpg")
    faceCascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    prediction = analyze_face(img)
    draw_rectangle(img, faceCascade)
    write_emotion(img, prediction)


def open_web_cam():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    return cap


cap = open_web_cam()

faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
lastCaptureTime = time.time()
firstTime = True
time.sleep(3)
while True:

    ret, frame = cap.read()
    try:

        # We show the video
        draw_rectangle(frame, faceCascade)
        if not firstTime:
            write_emotion(frame, emotion)
        cv2.imshow("Demo video", frame)

        if (time.time() - lastCaptureTime) > 1.5:
            lastCaptureTime = time.time()
            emotion = DeepFace.analyze(frame, actions=["emotion"])
            print(emotion['emotion'])

            firstTime = False

            for i in range(7):
                for j in range(2):
                    t.table[i][j] = Entry(root, width=20, fg='blue',
                                             font=('Arial', 16, 'bold'))

                    t.table[i][j].grid(row=i, column=j)

            t.table[0][0].insert(0, "Anger")
            t.table[1][0].insert(0, "Disgust")
            t.table[2][0].insert(0, "Fear")
            t.table[3][0].insert(0, "Happy")
            t.table[4][0].insert(0, "Sad")
            t.table[5][0].insert(0, "Surprise")
            t.table[6][0].insert(0, "Neutral")

            t.table[0][1].insert(0, round(emotion['emotion']["angry"], 2))
            t.table[1][1].insert(0, round(emotion['emotion']["disgust"], 2))
            t.table[2][1].insert(0, round(emotion['emotion']["fear"], 2))
            t.table[3][1].insert(0, round(emotion['emotion']["happy"], 2))
            t.table[4][1].insert(0, round(emotion['emotion']["sad"], 2))
            t.table[5][1].insert(0, round(emotion['emotion']["surprise"], 2))
            t.table[6][1].insert(0, round(emotion['emotion']["neutral"], 2))
            root.update()




    except BaseException as error:
        print(error)

    if cv2.waitKey(2) & 0xFF == ord("q"):
        cap.release()
        cv2.destroyAllWindows()
        break
