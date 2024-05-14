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
            print("Failed to read from camera.")
            break

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image_rgb = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        # Process hand landmarks
        results = hands.process(image_rgb)

        # Draw hand landmarks on the frame
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Extract thumb, index finger, and middle finger landmarks
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

                # Map landmarks to screen coordinates
                thumb_x, thumb_y = int(thumb_tip.x * image.shape[1]), int(thumb_tip.y * image.shape[0])
                index_x, index_y = int(index_tip.x * image.shape[1]), int(index_tip.y * image.shape[0])
                middle_x, middle_y = int(middle_tip.x * image.shape[1]), int(middle_tip.y * image.shape[0])

                # Print hand landmarks for debugging
                print(f"Thumb: ({thumb_x}, {thumb_y}), Index: ({index_x}, {index_y}), Middle: ({middle_x}, {middle_y})")

                # Control the mouse cursor
                pyautogui.moveTo(index_x, index_y)

                # Left click
                if abs(thumb_x - index_x) < 50 and abs(thumb_y - index_y) < 50:
                    print("Left click triggered.")
                    pyautogui.click()

                # Right click
                if abs(thumb_x - index_x) < 50 and abs(thumb_y - index_y) < 50:
                    if middle_y < index_y:
                        print("Right click triggered.")
                        pyautogui.rightClick()

                # Draw hand landmarks on the image
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS)

        # Display the frame
        cv2.imshow('MediaPipe Hands', image)

        # Check for exit key
        if cv2.waitKey(5) & 0xFF == 27:
            print("Exiting.")
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Call the main function if this script is executed directly
if __name__ == "__main__":
    main()
