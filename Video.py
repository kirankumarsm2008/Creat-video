import os
import cv2

path = 'E:/Projects/Project - 117/images/Images/'

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

    count = len(images)
    print(count)

    frame = cv2.imread(images[0])

    out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'MP42'),0.8,(500,330))

    for i in range(0,count-1):
        out.write(cv2.imread(images[i]))
        out.release()