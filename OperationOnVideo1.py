import threading
import cv2
import main
import time


class Operation1:
    def __init__(self):

        third_thread = threading.Thread(target=self.firstOperation, name="Thread3", args=())
        third_thread.daemon = True
        third_thread.start()
        print("Thread is alive?\n", third_thread.is_alive())
        print("Active thread count:", threading.active_count())

    def firstOperation(self):

        while 1:
            _, main.frame = main.cap.read()

            try:
                main.frame = cv2.resize(main.frame, (640, 480))
            except:
                print("cv2 resize error")

            cv2.imshow("Operation1frame", main.frame)
            time.sleep(0.30)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cv2.destroyAllWindows()


main = main.MainProject()
operation1 = Operation1()
