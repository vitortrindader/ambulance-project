# Importando bibliotecas
import cv2
import random


import cv2

def display_values(frame, value_1, value_2, value_3):
    # Get the dimensions of the input frame
    height, width, _ = frame.shape

    # Define rectangle coordinates for overlay
    p1 = int(height / 28.33)
    p2_w = int(width / 3.55)
    p2_h = int(height / 2.05)

    # Create a copy of the frame for overlay
    overlay = frame.copy()

    # Draw a filled rectangle to serve as the background for text
    cv2.rectangle(overlay, (p1, p1), (p2_w, p2_h), (0, 0, 0), thickness=cv2.FILLED)

    # Blend the overlay with the original frame
    cv2.addWeighted(overlay, 0.55, frame, 0.45, 0, frame)

    # Define font properties
    font = cv2.FONT_HERSHEY_DUPLEX
    font_scale = 1.5
    font_thickness = 3

    # Calculate positions for text display
    p_w = int(width / 7.73)
    p_h = int(height / 5.37)

    # Display HR (Heart Rate) value
    text_1 = "HR"
    text_color_1 = (113, 244, 164)
    cv2.putText(frame, str(value_1), (p_w, p_h), font, font_scale, text_color_1, font_thickness)
    p_w1 = p_w - 40
    cv2.putText(frame, text_1, (p_w1, p_h), font, font_scale * 0.4, text_color_1, 1)

    # Display SpO2 (Oxygen Saturation) value
    text_2 = "SpO2"
    text_color_2 = (81, 249, 249)
    p_h2 = p_h + 60
    cv2.putText(frame, str(value_2), (p_w, p_h2), font, font_scale, text_color_2, font_thickness)
    p_w2 = p_w - 60
    cv2.putText(frame, text_2, (p_w2, p_h2), font, font_scale * 0.4, text_color_2, 1)

    # Display etCO2 (End-tidal Carbon Dioxide) value
    text_3 = "etCO2"
    text_color_3 = (220, 246, 77)
    p_h3 = p_h2 + 60
    cv2.putText(frame, str(value_3), (p_w, p_h3), font, font_scale, text_color_3, font_thickness)
    p_w3 = p_w - 60
    cv2.putText(frame, text_3, (p_w3, p_h3), font, font_scale * 0.4, text_color_3, 1)


number_1 = 80
def read_HR_value():

    trigger = random.random()

    if trigger < 0.9:
        return number_1
    elif 0.9 < trigger < 0.95:
        return number_1 + 1
    else:
        return number_1 - 1

number_2 = 70
def read_SpO2_value():
    
    trigger = random.random()

    if trigger < 0.9:
        return number_2
    elif 0.9 < trigger < 0.95:
        return number_2 + 1
    else:
        return number_2 - 1

number_3 = 34
def read_etCO2_value():
    
    trigger = random.random()

    if trigger < 0.9:
        return number_3
    elif 0.9 < trigger < 0.95:
        return number_3 + 1
    else:
        return number_3 - 1


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

cap = cv2.VideoCapture(0) # Começa captura de imagem
if not cap.isOpened():
    print("Erro ao abrir a webcam.")
    exit()
count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao ler o frame.")
        break

    number_1 = read_HR_value() 
    number_2 = read_SpO2_value()
    number_3 = read_etCO2_value()

    display_values(frame,number_1,number_2,number_3)
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    count = count + 1
