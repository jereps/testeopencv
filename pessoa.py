import cv2

arqCasc1 = 'haarcascade_fullbody.xml'

faceCascade1 = cv2.CascadeClassifier(arqCasc1) #classificador para pessoa

def filtroRGB(src, r, g, b):
    if r == 0:
        src[:,:,2] = 0    #elimina o vermelho
    if g == 0:
        src[:,:,1] = 0    #elimina o verde
    if b == 0:
        src[:,:,0] = 0    #elimina o azul

total = 0

videocapture = cv2.VideoCapture("vivo.3gp")  #instancia o uso de video

while True:
    s, imagem = videocapture.read() #pega efeticamente a imagem 


    faces = faceCascade1.detectMultiScale(
        imagem,
        minNeighbors=20,
        minSize=(30, 30),
	maxSize=(300,300)
    )



    # Desenha um retangulo na imagem detectados
    for (x, y, w, h) in faces:
        #filtroRGB(imagem,0,0,1)
        total += 1
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 4)
        
        print (total)


    cv2.imshow('video', imagem) #mostra a imagem captura na janela

    #o trecho seguinte e apenas para parar o codigo e fechar a janela
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videocapture.release() #dispensa o uso do video
cv2.destroyAllWindows() #fecha todas a janelas abertas
