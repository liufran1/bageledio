import cv2
import matplotlib.pyplot as plt
import os
import re



count = 0
videoFile = ""
cap = cv2.VideoCapture(videoFile)   # capturing the video from the given path

x=1

first_iter = True # for getting background to average out

# todo - create temp folder

while(cap.isOpened()):
    frameId = cap.get(1) # current frame number
    ret, frame = cap.read()
    if (ret != True): # loop until no more frames
        break
    else:
    # if (frameId % math.floor(frameRate) == 0):
        filename =f"frames/frame{str(count).rjust(3, '0')}.jpg";\
        count+=1
        cv2.imwrite(filename, frame)
        # Get average frames
        if first_iter:
          avg = np.float32(frame)
          first_iter = False
        cv2.accumulateWeighted(frame, avg, 0.005) # https://machinelearningknowledge.ai/remove-moving-objects-from-video-in-opencv-python-using-background-subtraction-running-average-vs-median-filtering/
        result1 = cv2.convertScaleAbs(avg)
cap.release()


!rm -r diff_gray_frames
!mkdir diff_gray_frames

# kernel for image dilation
kernel = np.ones((4,4),np.uint8)

# directory to save the ouput frames
pathIn = "diff_gray_frames/"

for i in range(len(col_images)-1):

    # frame differencing

    diff_image = cv2.absdiff(cv2.cvtColor(col_images[i], cv2.COLOR_BGR2RGB), cv2.cvtColor(result1, cv2.COLOR_BGR2RGB))
    gray_diff = cv2.cvtColor(diff_image, cv2.COLOR_BGR2GRAY)


    # image thresholding
    ret, thresh = cv2.threshold(gray_diff, 30, 255, cv2.THRESH_BINARY)

    # image dilation
    dilated = cv2.dilate(thresh,kernel,iterations = 1)

    # cv2.imwrite(pathIn+str(i).rjust(3,'0')+'.png',dilated[contour_y:,:])
    cv2.imwrite(pathIn+str(i).rjust(3,'0')+'.png',thresh[contour_y:,:])


pathIn = "diff_frames/"

for i in range(len(col_images)-1):

    # frame differencing

    diff_image = cv2.absdiff(cv2.cvtColor(col_images[i], cv2.COLOR_BGR2RGB), cv2.cvtColor(result1, cv2.COLOR_BGR2RGB))

    cv2.imwrite(pathIn+str(i).rjust(3,'0')+'.png',diff_image[contour_y:,:])



# specify video name
pathOut = 'vehicle_detection_v4.mp4'

# specify frames per second
fps = 60

frame_array = []
file_list = [f for f in os.listdir(pathIn)]



frame_array = []

file_list.sort(key=lambda f: int(re.sub('\D', '', f)))

for i in range(len(file_list)):
    filename=pathIn + file_list[i]

    #read frames
    img = cv2.imread(filename)
    try:
      height, width, layers = img.shape
      size = (width,height)
    except:
      pass

    #inserting the frames into an image array
    frame_array.append(img)


out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])

out.release()
