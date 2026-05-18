# 🧠 Mediapipe-Tarefas

Pipeline simples de Visão Computacional em tempo real usando **MediaPipe + OpenCV** para detecção facial via webcam.

Simples na superfície. Complexo o suficiente por baixo para lembrar que visão computacional não é magia — é matemática aplicada com paciência.

---

## ⚙️ 1. Ambiente de Desenvolvimento

```bash
# Criar ambiente isolado
conda create -n Mediapipe-Tarefas python=3.10 -y

# Ativar ambiente
conda activate Mediapipe-Tarefas

# Instalar dependências
pip install mediapipe opencv-python
```

---

## 📦 2. Estrutura do Projeto

```
Mediapipe-Tarefas/
│
├── main.py
└── README.md
```

---

## 🧩 3. Código Principal (main.py)

```python
import cv2
import mediapipe as mp

# Inicializa detector de rostos
mp_face = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
model = mp_face.FaceDetection()

# Webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Conversão BGR -> RGB (MediaPipe exige isso)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Inferência
    results = model.process(frame_rgb)

    # Desenho das detecções
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(frame, detection)

    # Exibição
    cv2.imshow("Mediapipe-Tarefas", frame)

    # Sair com tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

---

## 🔄 4. Fluxo de Execução

**1. Captura**

* Webcam fornece frames em BGR via OpenCV

**2. Pré-processamento**

* Conversão BGR → RGB (requisito do MediaPipe)

**3. Inferência**

* `model.process()` detecta rostos e retorna bounding boxes

**4. Renderização**

* MediaPipe desenha landmarks diretamente no frame

**5. Exibição**

* OpenCV renderiza o resultado em tempo real

---

## 🧠 Ideia Central

Este projeto é a base mínima de qualquer sistema de visão computacional em tempo real:

* captura
* pré-processamento
* inferência
* renderização

O resto é escala, dados e sofrimento otimizado.

---

## 🚀 Possíveis Expansões

* Integração com YOLO para detecção de múltiplos objetos
* MediaPipe Hands (gestos)
* MediaPipe Pose (ergonomia / postura)
* Integração com Arduino para feedback físico
* Sistema de alertas em tempo real (fadiga, atenção, etc)

---

## ⚠️ Observação Técnica

Se isso rodar liso na tua máquina, ótimo.
Se não rodar, parabéns: você acabou de entrar no mundo real da computação gráfica e dependências nativas.

Bem-vindo.
