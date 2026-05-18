import cv2
import mediapipe as mp

# 1. Configuração Inicial do MediaPipe
mp_utils = mp.solutions.drawing_utils    # Ferramenta para desenhar na tela
mp_hands = mp.solutions.hands            # Exemplo: Módulo de Mãos (pode mudar para FaceMesh ou Pose)

# Inicializa o modelo de IA com configurações leves
modelo_ia = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# 2. Inicializa a Webcam
cap = cv2.VideoCapture(0)

print("Estrutura MediaPipe ativa. Pressione 'q' na janela para fechar.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    # Inverte a imagem (efeito espelho)
    frame = cv2.flip(frame, 1)

    # O MediaPipe exige conversão de cores de BGR para RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # 3. Executa o processamento da IA no Frame
    resultados = modelo_ia.process(frame_rgb)

    # 4. Verifica se a IA detectou algo
    if resultados.multi_hand_landmarks:
        for landmarks in resultados.multi_hand_landmarks:
            # Desenha os pontos e as conexões estruturais no frame original
            mp_utils.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

    # 5. Renderiza a imagem na janela do Windows
    cv2.imshow("Wandi Engine - MediaPipe Base", frame)

    # Condição de saída rápida
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 6. Limpeza e Liberação de Hardware
cap.release()
cv2.destroyAllWindows()
modelo_ia.close()
print("Processo encerrado com sucesso.")