import cv2
import mediapipe as mp
import pyautogui

def main():
    # Initialize MediaPipe Hands module
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    # Open default camera
    cap = cv2.VideoCapture(0)
    hands = mp_hands.Hands()

    while True:
        success, image = cap.read()
        if not success:
            break

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        # To improve performance, optionally mark the image as not writable to
        # pass by reference.
        image.flags.writeable = False
        results = hands.process(image)

        # Draw hand landmarks on the frame
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Control the virtual mouse
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_x, thumb_y = int(thumb_tip.x * image.shape[1]), int(thumb_tip.y * image.shape[0])
                index_x, index_y = int(index_tip.x * image.shape[1]), int(index_tip.y * image.shape[0])
                pyautogui.moveTo(index_x, index_y)
                if abs(thumb_x - index_x) < 50 and abs(thumb_y - index_y) < 50:
                    pyautogui.click()

                # Draw hand landmarks on the image
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS)

        # Display the frame
        cv2.imshow('MediaPipe Hands', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Call the main function if this script is executed directly
if __name__ == "__main__":
    main()
