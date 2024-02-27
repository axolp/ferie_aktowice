import cv2
import pytesseract
from pytesseract import Output
def find_black_column(image_path, side, margin):
    
    image= cv2. imread(image_path)
    print(image[0][0])
    n_rows, n_columns, nothing= image.shape

    if side == 'left':
       left= 0
       for i in range(n_columns):
            for j in range(n_rows):
                if image[j][i][1] == 0:
                    left= i
                    break

            if left != 0:
                return left - margin
       return 0
    
    else:
        right= 0
        for i in range(n_columns):
            for j in range(n_rows):
                if image[j][n_columns-i-1][1] == 0:
                    right= n_columns-i-1
                    break

            if right != 0:
                return right + margin
        return n_columns

# Konfiguracja ścieżki do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\PC\Desktop\Uczelnia\projekty\chinski\tessaract\tesseract.exe'  # Zmień ścieżkę według swojej instalacji
custom_config = r'--psm 7'
# Odczyt wideo
video = cv2.VideoCapture('wideo2.mp4')
# Ustalanie framerate
fps = video.get(cv2.CAP_PROP_FPS)
interval = int(fps*0.7)  # Co 0,5 sekundy

video.set(cv2.CAP_PROP_POS_MSEC, 2000)

# Przetwarzanie klatek
prev_l, prev_r= -69, -69
frame_number = 0
sekunda= 0
while True:
    success, frame = video.read()
    if not success:
        break
    x= 200
    y= 650
    h= 35
    w= 825
    sekunda= (frame_number / fps) + 2
    # Przetwarzanie co 0,5 sekundy
    if frame_number % interval == 0 :
        
        # Wyciągnij określony obszar ekranu (x, y, szerokość, wysokość)
        roi = frame[y:y+h, x:x+w]
        gray_roi= cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        nothing, final_roi= cv2.threshold(gray_roi, 200, 255, cv2.THRESH_BINARY_INV)
        
        #sum_cols = cv2.reduce(final_roi, 0, cv2.REDUCE_SUM, dtype=cv2.CV_32S)
        #left = cv2.findNonZero(sum_cols.T)[0][0]
        #right = cv2.findNonZero(sum_cols.T)[-1][0]

        # Przycięcie ROI
        #cropped_roi = final_roi[:, left:right]
        
        cv2.imwrite(f"roi{frame_number}.jpg", final_roi)
        l= find_black_column(f'roi{frame_number}.jpg', 'left', 5)
        r= find_black_column(f'roi{frame_number}.jpg', 'right', 5)
        print(l, r)

        if l ==0:
            continue
        if l == prev_l and r == prev_r:
            print("skipuje bo to samo")
            continue

        print(final_roi.shape)
        try:    
            cropped_roi = final_roi[0:35, l:r]
            cv2.imwrite(f"aftercut{frame_number}.jpg", cropped_roi)
            # Stosowanie OCR
            text = pytesseract.image_to_string(final_roi, lang='chi_sim', config=custom_config)  # Użyj 'chi_sim' dla uproszczonego chińskiego
        except:
            text= "error"
        # Zapis do pliku
        with open('transkrypt.txt', 'a', encoding='utf-8') as file:
            file.write(f'Frame number: {frame_number}  Sekunda {sekunda}: {text}\n')

    frame_number += 1
    prev_l, prev_r= l, r
    

video.release()

