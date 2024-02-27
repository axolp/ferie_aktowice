import cv2


def check_if_blank(image_path):
    image= cv2. imread(image_path)
    n_rows, n_columns, nothing= image.shape

    for i in range(n_columns):
        if image[n_rows//2][i][1] 

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
                    #print("left: ", j)
                    break
            if left != 0:
                return left - margin
    else:
        
        right= 0
        for i in range(n_columns):
            for j in range(n_rows):
                #print(n_columns-i-1)
                if image[j][n_columns-i-1][1] == 0:
                    
                    right= n_columns-i-1
                    #print("right: ", n_columns-i-1)
                    break
            if right != 0:
                return right + margin
    
l= find_black_column('roi1356.jpg', 'left', 5)
r= find_black_column('roi1356.jpg', 'right', 5)
print("funckja: ", l)
print("funckja: ", r)
   

x= 200
y= 650
h= 35
w= 825

frame= cv2. imread('roi1356.jpg')
roi = frame[0:1000, l:r]
cv2.imwrite("aftercut2.jpg", roi)