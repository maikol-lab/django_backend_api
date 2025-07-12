# MAIKOL RODRIGUEZ
# YORGE AETEAGA

# Importamos librerias de la Inteligencia Artificial Python.
from imutils import face_utils
from .utils import *
import numpy as np
import pyautogui as pyag
import pyautogui as pag
import imutils
import dlib
import cv2
import time
from datos import Datos

#Esto quita el error del Mouse cuando sale de la pantalla
pag.FAILSAFE = False 

# Umbrales y longitud de fotograma consecutivo para activar la acción del mouse.
MOUTH_AR_THRESH = 0.6
MOUTH_AR_CONSECUTIVE_FRAMES = 15
EYE_AR_THRESH = 0.19
EYE_AR_CONSECUTIVE_FRAMES = 15
WINK_AR_DIFF_THRESH = 0.04
WINK_AR_CLOSE_THRESH = 0.19
WINK_CONSECUTIVE_FRAMES = 10

# Inicialice los contadores de fotogramas para cada acción, así como
# booleanos utilizados para indicar si la acción se realiza o no.
MOUTH_COUNTER = 0
EYE_COUNTER = 0
WINK_COUNTER = 0
INPUT_MODE = False
EYE_CLICK = False
LEFT_WINK = False
RIGHT_WINK = False
SCROLL_MODE = False
ANCHOR_POINT = (0, 0)
WHITE_COLOR = (255, 255, 255)
YELLOW_COLOR = (0, 255, 255)
RED_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 255, 0)
BLUE_COLOR = (255, 0, 0)
BLACK_COLOR = (0, 0, 0)

# Inicialice el detector de rostros de Dlib (basado en HOG) y luego cree
# el predictor de puntos de cursorwffefefreferencia facial
shape_predictor = "model/shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shape_predictor)

# Tome los índices de los puntos de referencia faciales para la izquierda y
# ojo derecho, nariz y boca respectivamente
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
(nStart, nEnd) = face_utils.FACIAL_LANDMARKS_IDXS["nose"]
(mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]

# Video capture
vid = cv2.VideoCapture(0)
resolution_w = 1366
resolution_h = 768
cam_w = 700
cam_h = 750
unit_w = resolution_w / cam_w
unit_h = resolution_h / cam_h

while True:
    # Tome el fotograma de la secuencia del archivo de vídeo encadenado y cambie el tamaño
    # y convertirlo a escala de grises
    # canales)
    _, frame = vid.read()
    frame = cv2.flip(frame, 1)
    frame = imutils.resize(frame, width=cam_w, height=cam_h)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostros en el marco de escala de grises
    rects = detector(gray, 0)

    # Recorre las detecciones de rostros
    if len(rects) > 0:
        rect = rects[0]
    else:
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        continue

    # Determine los puntos de referencia faciales para la región de la cara y luego
    # convertir las coordenadas del punto de referencia facial (x, y) a NumPy.
    # matriz
    shape = predictor(gray, rect)
    shape = face_utils.shape_to_np(shape)

    # Extraiga las coordenadas del ojo izquierdo y derecho, luego use el
    # coordenadas para calcular la relación de aspecto de ambos ojos.
    mouth = shape[mStart:mEnd]
    leftEye = shape[lStart:lEnd]
    rightEye = shape[rStart:rEnd]
    nose = shape[nStart:nEnd]

    # Debido a que volteé el marco, la izquierda es la derecha y la derecha es la izquierda.
    temp = leftEye
    leftEye = rightEye
    rightEye = temp

    # Promediar la relación de aspecto de la boca para ambos ojos
    mar = mouth_aspect_ratio(mouth)
    leftEAR = eye_aspect_ratio(leftEye)
    rightEAR = eye_aspect_ratio(rightEye)
    ear = (leftEAR + rightEAR) / 2.0
    diff_ear = np.abs(leftEAR - rightEAR)

    nose_point = (nose[3, 0], nose[3, 1])

    # Calcule el casco convexo para el ojo izquierdo y derecho, luego
    # visualizar cada uno de los ojos.
    mouthHull = cv2.convexHull(mouth)
    leftEyeHull = cv2.convexHull(leftEye)
    rightEyeHull = cv2.convexHull(rightEye)
    cv2.drawContours(frame, [mouthHull], -1, YELLOW_COLOR, 1)
    cv2.drawContours(frame, [leftEyeHull], -1, YELLOW_COLOR, 1)
    cv2.drawContours(frame, [rightEyeHull], -1, YELLOW_COLOR, 1)

    for (x, y) in np.concatenate((mouth, leftEye, rightEye), axis=0):
        cv2.circle(frame, (x, y), 2, GREEN_COLOR, -1)
        
    # Verifique si la relación de aspecto del ojo está por debajo del parpadeo
    # umbral y, si es así, incrementar el contador de fotogramas de parpadeo.

    if diff_ear > WINK_AR_DIFF_THRESH:

        if leftEAR < rightEAR:
            if leftEAR < EYE_AR_THRESH:
                WINK_COUNTER += 5

                if WINK_COUNTER > WINK_CONSECUTIVE_FRAMES:
                    pag.click(button='left')

                    WINK_COUNTER = 0.00001

        elif leftEAR > rightEAR:
            if rightEAR < EYE_AR_THRESH:
                WINK_COUNTER += 5

                if WINK_COUNTER > WINK_CONSECUTIVE_FRAMES:
                    pag.click(button='right')

                    WINK_COUNTER = 0.00001
        else:
            WINK_COUNTER = 0
    else:
        if ear <= EYE_AR_THRESH:
            EYE_COUNTER += 1

            if EYE_COUNTER > EYE_AR_CONSECUTIVE_FRAMES:
                SCROLL_MODE = not SCROLL_MODE
                #INPUT_MODE = not INPUT_MODE
                EYE_COUNTER = 1

       # punta de la nariz para dibujar un cuadro delimitador a su alrededor

        else:
            EYE_COUNTER = 0
            WINK_COUNTER = 0

    if mar > MOUTH_AR_THRESH:
        MOUTH_COUNTER += 1

        if MOUTH_COUNTER >= MOUTH_AR_CONSECUTIVE_FRAMES:
             #SCROLL_MODE = not SCROLL_MODE
             #Si la alarma no está encendida, enciéndela.
             INPUT_MODE = not INPUT_MODE
             MOUTH_COUNTER = 0
             ANCHOR_POINT = nose_point

    else:
        MOUTH_MODE = 0


    #clase de envio de datos
    datos_enviados = Datos()
    
    # Activar el programa Abriendo la boca con la Formula EAR para la detencion del mismo
    if INPUT_MODE:
        cv2.putText(frame, "READING INPUT!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
        x, y = ANCHOR_POINT
        nx, ny = nose_point
        w, h = 80, 30
        multiple = 1
        cv2.rectangle(frame, (x - w, y - h), (x + w, y + h), GREEN_COLOR, 2)
        cv2.line(frame, ANCHOR_POINT, nose_point, BLUE_COLOR, 2)
        
        # Direccionar todos los angulos del Cursor de la Nariz con los movimientos que se Realice
        dir = direction(nose_point, ANCHOR_POINT, w, h)
        cv2.putText(frame, dir.upper(), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
        drag = 28
        #condicional de movimiento
        if dir == 'right':
            #Envio de datos
            datos_enviados.setattr("right")
            datos_enviados.set_datosActualizados()        
            pyag.moveRel(drag, 0)
            
        elif dir == 'left':
            #Envio de datos
            datos_enviados.setattr("left")
            datos_enviados.set_datosActualizados()
            pyag.moveRel(-drag, 0)
            
        elif dir == 'up':
            #Envio de datos
            datos_enviados.setattr("up")
            datos_enviados.set_datosActualizados()
                        
            if SCROLL_MODE:
                pyag.scroll(40)
            else:
                pyag.moveRel(0, -drag)

                
        elif dir == 'down':
            #Envio de datos
            datos_enviados.setattr("down")
            datos_enviados.set_datosActualizados()
            
            if SCROLL_MODE:
                pyag.scroll(-40)
            else:
                pyag.moveRel(0, drag)

                
        elif dir == 'up-right':
            #Envio de datos
            datos_enviados.setattr("up-right")
            datos_enviados.set_datosActualizados()            
            
            pyag.moveRel(drag, -drag)
            
        elif dir == 'up-left':
            #Envio de datos
            datos_enviados.setattr("up-left")
            datos_enviados.set_datosActualizados()            
            
            pyag.moveRel(-drag, -drag)  # Añadido
            
        elif dir == 'up-left':
            #Envio de datos
            datos_enviados.setattr("up-left")
            datos_enviados.set_datosActualizados()            
            
            pyag.moveRel(-drag, drag)
            
        elif dir == 'down-right':
            #Envio de datos
            datos_enviados.setattr("down-right")
            datos_enviados.set_datosActualizados()            
            
            pyag.moveRel(drag, drag)
            
        elif dir == 'down-left':
            #Envio de datos
            datos_enviados.setattr("down-left")
            datos_enviados.set_datosActualizados()            
            
            pyag.moveRel(-drag, drag)  # Añadido
                
        
       
    if SCROLL_MODE:
        #Envio de datos
        cv2.putText(frame, 'SCROLL MODE IS ON!', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)

    #Envio de datos
    datos_enviados.setattr("MAR: {:.2f}".format(mar))
    datos_enviados.set_datosActualizados()      
    cv2.putText(frame, "MAR: {:.2f}".format(mar), (500, 30),
    cv2.FONT_HERSHEY_SIMPLEX, 0.7, YELLOW_COLOR, 2)

    #Envio de datos
    datos_enviados.setattr("Right EAR: {:.2f}".format(rightEAR))
    datos_enviados.set_datosActualizados()          
    cv2.putText(frame, "Right EAR: {:.2f}".format(rightEAR), (460, 80),
                 cv2.FONT_HERSHEY_SIMPLEX, 0.7, YELLOW_COLOR, 2)

    #Envio de datos
    datos_enviados.setattr("Left EAR: {:.2f}".format(leftEAR))
    datos_enviados.set_datosActualizados()          
    cv2.putText(frame, "Left EAR: {:.2f}".format(leftEAR), (460, 130),
                 cv2.FONT_HERSHEY_SIMPLEX, 0.7, YELLOW_COLOR, 2)

    #Envio de datos
    datos_enviados.setattr("Diff EAR: {:.2f}".format(np.abs(leftEAR - rightEAR)))
    datos_enviados.set_datosActualizados()      
    cv2.putText(frame, "Diff EAR: {:.2f}".format(np.abs(leftEAR - rightEAR)), (460, 180),
                 cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    
    # mostrar el marco de imagen
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # Si se presionó la tecla `Esc`, salga del bucle
    if key == 27:
        break

# Haz un poco de limpieza
cv2.destroyAllWindows()
vid.release()
