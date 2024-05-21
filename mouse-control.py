import cv2
import mediapipe as mp
import pyautogui

def left_click():
    pyautogui.click()

def right_click():
    pyautogui.click(button='right')


def scrollup():
    pyautogui.scroll(10)

def scrolldown():
    pyautogui.scroll(-10)

def main():
    # Initialize MediaPipe Hands module
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    # Open default camera
    cap = cv2.VideoCapture(0)
    # Get screen resolution
    screen_width, screen_height = pyautogui.size()

    # Get the camera frame resolution
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

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
                thumb_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                index_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
                middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                middle_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
        
                thumb_x, thumb_y = int(thumb_tip.x * image.shape[1]), int(thumb_tip.y * image.shape[0])
                index_x, index_y = int(index_tip.x * image.shape[1]), int(index_tip.y * image.shape[0])
                middle_x, middle_y = int(middle_tip.x * image.shape[1]), int(middle_tip.y * image.shape[0])
                
                # Map the frame coordinates to screen coordinates
                screen_x = int(index_x * screen_width / frame_width)
                screen_y = int(index_y * screen_height / frame_height)

                # Move the mouse cursor to the mapped coordinates
                pyautogui.moveTo(screen_x, screen_y)

                # Calculate distances between fingertips and their MCP joints
                thumb_extended = thumb_tip.y < thumb_mcp.y
                index_flexed = index_tip.y > index_mcp.y
                middle_flexed = middle_tip.y > middle_mcp.y

                # Left click if thumb and index finger are close
                if abs(thumb_x - index_x) < 50 and abs(thumb_y - index_y) < 50:
                    left_click()

                # Right click if thumb and middle finger are close
                if abs(thumb_x - middle_x) < 50 and abs(thumb_y - middle_y) < 50:
                    right_click()

                # Scroll up if thumb and index finger are far apart
                if abs(thumb_x - index_x) > 100:
                    scrollup()

                # Scroll down if only thumb is extended and other fingers are flexed
                if thumb_extended and index_flexed and middle_flexed:
                    scrolldown()

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
