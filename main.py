import cv2
import random

def operacao_aleatoria(numero):
    trigger = random.random()

    if trigger < 0.6:
        return numero
    elif 0.6 < trigger < 0.8:
        return numero + 1
    else:
        return numero - 1

number_1 = 90
number_2 = 73
number_3 = 25

video_file = 'video.mp4'
cap = cv2.VideoCapture(video_file)

if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

# informações do vídeo original
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# arquivo de saída e o codec de vídeo
output_file = 'output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Fim do vídeo.")
        break

    overlay = frame.copy()
    cv2.rectangle(overlay, (220, 200), (380, 430), (0, 0, 0), thickness=cv2.FILLED)
    cv2.addWeighted(overlay, 0.55, frame, 0.45, 0, frame)

    font = cv2.FONT_HERSHEY_DUPLEX
    font_scale = 1.5
    font_thickness = 3

    text_1 = "HR"
    if count % 2 == 0:  # Apenas para que nos frames pares ele tente mudar a métrica - para não oscilar tanto
        number_1 = operacao_aleatoria(number_1)
    text_color_1 = (113, 244, 164)
    cv2.putText(frame, str(number_1), (280, 265), font, font_scale, text_color_1, font_thickness)
    cv2.putText(frame, text_1, (250, 265), font, font_scale * 0.4, text_color_1, 1)

    text_2 = "SpO2"
    if count % 2 == 0:
        number_2 = operacao_aleatoria(number_2)
    text_color_2 = (81, 249, 249)
    cv2.putText(frame, str(number_2), (280, 325), font, font_scale, text_color_2, font_thickness)
    cv2.putText(frame, text_2, (230, 325), font, font_scale * 0.4, text_color_2, 1)

    text_3 = "etCO2"
    if count % 2 == 0:
        number_3 = operacao_aleatoria(number_3)
    text_color_3 = (220, 246, 77)
    cv2.putText(frame, str(number_3), (280, 385), font, font_scale, text_color_3, font_thickness)
    cv2.putText(frame, text_3, (227, 385), font, font_scale * 0.4, text_color_3, 1)

    cv2.imshow('Video', frame)
    out.write(frame)

    count += 1

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
