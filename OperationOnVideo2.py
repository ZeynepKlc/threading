import threading
import cv2
import time
from OperationOnVideo1 import main


class Operation2:

    def __init__(self):

        fourth_thread = threading.Thread(target=self.add_text, name="Thread4", args=())
        fourth_thread.start()

    def add_text(self):
        cv2.namedWindow("Camera with Text")

        while 1:
            _, main.frame = main.cap.read()
            main.frame = cv2.resize(main.frame, (640, 480))

            if main.frame.shape[0] == 0 or main.frame.shape[1] == 0:
                continue
            else:
                print("cv2 resize error")

            cv2.putText(main.frame, "Camera with Text", (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (10, 255, 50), 2)

            cv2.imshow("Camera with Text", main.frame)
            time.sleep(0.30)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cv2.destroyAllWindows()


operation2 = Operation2()
