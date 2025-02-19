import queue
import threading
import cv2 as cv


window_name = 'Ass cam'
readed = []
qrcodes = open("qrcodes.txt","w",encoding="utf-8")
qcd = cv.QRCodeDetector()

def camera():
    input_buffer = queue.Queue()

    def feldogoz():
        while True:
            frame = input_buffer.get()
            cv.imshow('stream',frame)
        return


    cap = cv.VideoCapture(0)
    #cap2 = cv.VideoCapture(2)


    def make480p():
        cap.set(3,640)
        cap.set(4,480)
    #def make480p2():
    #    cap2.set(3,640)
    #    cap2.set(4,480)

    def change_res(szelesseg,magassag):
        cap.set(3,szelesseg)
        cap.set(4,magassag)

    #def change_res2(szelesseg,magassag):
    #    cap2.set(3,szelesseg)
    #    cap2.set(4,magassag)



    make480p()
    #make480p2()

    change_res(600,700)
    #change_res2(500,400)



    t = threading.Thread(target=feldogoz)


    while True:
        ret, frame = cap.read()
        #ret2, frame2 = cap2.read()


        input_buffer.put(frame)
        #input_buffer.put(frame2)
        #frame = cv.flip(frame, 1)
        #frame2 = cv.flip(frame2,0)

        cv.imshow(window_name, frame)
        #cv.imshow(window_name2, frame2)

        if cv.waitKey(1) == ord('q'):
            break
camera()

for line in readed:
    qrcodes.write(line+"\n")


