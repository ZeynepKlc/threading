import cv2
import threading
import numpy as np


class MainProject:
    def __init__(self):

        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.frame = None

        first_thread = threading.Thread(target=self.edges_det, args=())
        first_thread.daemon = True
        first_thread.start()

        sec_thread = threading.Thread(target=self.tracking, name="Thread2", args=())
        sec_thread.start()

    def edges_det(self):

        """
        Kamera açılıp köşeler algılanır ve ekranda gösterilir.
        """

        while 1:
            _, self.frame = self.cap.read()

            self.edges = cv2.Canny(self.frame, 150, 200)

            cv2.imshow("Frame1", self.frame)

            cv2.imshow("Edges", self.edges)

            if cv2.waitKey(4) & 0xFF == ord("q"):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def tracking(self):

        """
        Kamera açılıp nesnenin izi sürülür ve ekranda gösterilir.
        """

        while True:
            _, self.frame = self.cap.read()

            self.frame = cv2.resize(self.frame, (640, 480))

            if self.frame is not None and self.frame.size > 0 and self.frame.shape[0] > 0 and self.frame.shape[1] > 0:

                hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
                sensitivity = 30
                lower_white = np.array([0, 0, 255 - sensitivity])
                upper_white = np.array([255, sensitivity, 255])

                self.mask = cv2.inRange(hsv, lower_white, upper_white)

                cv2.imshow("mask", self.mask)
            else:

                print("Görüntü boş veya boyutu sıfır.")

            if cv2.waitKey(2) & 0xFF == ord("q"):
                break

        self.cap.release()
        cv2.destroyAllWindows()


a = MainProject()
