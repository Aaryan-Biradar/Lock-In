import cv2
import dlib

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Check if the webcam opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()

    # # Load the pre-trained face detector and shape predictor
    # detector = dlib.get_frontal_face_detector()
    # predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    ret, frame = cap.read()

    # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # faces = detector(frame)

    # for face in faces:
    #     landmarks = predictor(frame, face)

    #     for n in range(0, 68):
    #         x = landmarks.part(n).x
    #         y = landmarks.part(n).y
    #         cv2.circle(frame, (x, y), 1, (255, 0, 0), -1)



    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        cap.release()
        cv2.destroyAllWindows()
