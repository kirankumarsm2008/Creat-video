import cv2
import os

path = 'E:/Projects/Project - 117/images/Images'

images = []

list_of_files = os.listdir(path)
print(list_of_files)

for ei in list_of_files:
    name, ext = os.path.splitext(ei)
    print(name)
    print(ext)

    if ext in ['.jpg','.gif','.png','.svg','.jpeg','.jfif']:
        file_name = path + "/" + ei
        print(file_name)

    images.append(ei)
    print(images)

frame = cv2.imread(images[0])
size = (frame.shape)
print(size)
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
