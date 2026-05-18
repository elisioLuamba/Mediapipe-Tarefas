import cv2
import mediapipe as mp

# Inicializa detector de rostos e utilitários de desenho
mp_face = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Inicializa o modelo de inferência
model = mp_face.FaceDetection(min_detection_confidence=0.5)

# Inicializa captura da Webcam (0 = padrão)
cap = cv2.VideoCapture(0)

print("Engine ativa. Pressione 'q' na janela de vídeo para encerrar.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Erro: Falha na captura do hardware.")
        continue

    # Inverte o frame horizontalmente (efeito espelho para interação natural)
    frame = cv2.flip(frame, 1)

    # Conversão BGR -> RGB (Exigência estrutural do MediaPipe)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Executa a inferência matemática no frame
    results = model.process(frame_rgb)

    # Renderização das detecções sobre o frame original
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(frame, detection)

    # Exibição do buffer na janela nativa do SO
    cv2.imshow("Mediapipe-Tarefas", frame)

    # Condição de saída: tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Desalocação estrita de hardware e memória
cap.release()
cv2.destroyAllWindows()
model.close()
print("Recursos liberados de forma limpa.")