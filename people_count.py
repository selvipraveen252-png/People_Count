import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

stop_flag = False

def stop():
    global stop_flag
    stop_flag = True

def run(source):
    global stop_flag
    stop_flag = False

    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print("Error: Cannot open source")
        return

    while True:
        if stop_flag:
            break

        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, classes=[0], conf=0.5)
        count = len(results[0].boxes)

        annotated = results[0].plot()
        cv2.putText(
            annotated,
            f"People Count: {count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("People Tracking", annotated)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

    cap.release()
    cv2.destroyAllWindows()
    stop_flag = False
