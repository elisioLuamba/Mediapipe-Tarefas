# 🧠 Mediapipe-Tarefas

Pipeline simples de Visão Computacional em tempo real usando **MediaPipe + OpenCV** para detecção facial via webcam.

Simples na superfície. Complexo o suficiente por baixo para lembrar que visão computacional não é magia — é matemática aplicada com paciência.

---

## 🛠️ Configuração do Sistema

### Pré-requisitos

* Anaconda ou Miniconda instalada
* Python **3.10.19** (versão escolhida pela estabilidade com pacotes de ML)
* Câmera funcional para testes de visão computacional

---

## ⚙️ Instalação Passo a Passo

Para replicar o ambiente exatamente como configurado:

### 1. Criação do Container

```bash
conda create -n tarefas python=3.10.19 -y
conda activate tarefas
```

---

### 2. Dependências de Processamento e ML

```bash
pip install numpy==1.26.4 scipy==1.15.3 jax==0.6.2 jaxlib==0.6.2
```

---

### 3. Dependências de Visão e Interface

```bash
pip install opencv-python==4.12.0.88 opencv-contrib-python==4.11.0.86 mediapipe==0.10.20
```

---

### 4. Hardware e Utilitários (sem serial, porque simplicidade também é engenharia)

```bash
pip install matplotlib==3.10.8 pillow==12.1.0
```

---

## 🏗️ Arquitetura do Código de Exemplo

O script de teste básico segue o fluxo clássico de um pipeline de **Visão Computacional em tempo real**:

### 1. Entrada

* Captura de frames utilizando `cv2.VideoCapture`

### 2. Pré-processamento

* Conversão de cores de **BGR → RGB**

### 3. Inferência

* Processamento pelo modelo `mp.solutions.hands`

### 4. Saída de Dados

* Coordenadas normalizadas `(x, y, z)` dos **21 pontos da mão**

### 5. Ação (Opcional)

* Apenas visualização em tempo real (sem comunicação serial)

---

## 🚨 Notas de Manutenção (Realismo Técnico)

### Conflitos de Versão

O MediaPipe é sensível às versões do protobuf. Caso ocorra erro de importação, evite atualizar pacotes críticos sem validação de compatibilidade com `jax`.

---

### Performance

Para maior fluidez:

```python
static_image_mode=False
```

Isso ativa tracking entre frames, evitando detecção completa a cada ciclo.

---

## 🧠 Ideia Central

Este projeto é a base mínima de qualquer sistema de visão computacional em tempo real:

* captura
* pré-processamento
* inferência
* renderização

O resto é escala, dados e paciência com dependências que fingem que não te conhecem.

---

## 🚀 Possíveis Expansões

* Integração com YOLO para detecção de múltiplos objetos
* MediaPipe Pose (análise corporal)
* Sistema de alerta de atenção/fadiga
* Pipeline otimizado para edge devices

---

## ⚠️ Observação Técnica

Se isso rodar liso na tua máquina, ótimo.
Se não rodar, bem-vindo ao mundo real: versões, drivers e CUDA não negociam com otimismo.
