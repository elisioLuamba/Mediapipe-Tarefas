# 🧠 Mediapipe-Tarefas

Pipeline simples de Visão Computacional em tempo real usando **MediaPipe + OpenCV** para detecção facial via webcam.

---

## 🛠️ Configuração do Sistema

### Pré-requisitos

* Anaconda ou Miniconda instalada
* Python **3.10.19** (versão escolhida pela estabilidade com pacotes de ML)
* Câmera funcional para testes de visão computacional

---

## ⚙️ Instalação Passo a Passo

Para replicar o ambiente exatamente como configurado:

### 1. Criar e Ativar o Container

```bash
conda create -n Mediapipe-Tarefas python=3.10.19 -y
conda activate Mediapipe-Tarefas
```

---

### 2. Instalar a Trindade Essencial

```bash
pip install numpy==1.26.4 opencv-python==4.11.0.86 mediapipe==0.10.20
```

### Performance

Para maior fluidez:

```python
static_image_mode=False
```

Isso ativa tracking entre frames, evitando detecção completa a cada ciclo.

---
