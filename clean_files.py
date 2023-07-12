import cv2
import os
import re
import tempfile
import numpy as np


def gen_folders():
  temp_dir = tempfile.TemporaryDirectory()

  frames_path = os.path.join(temp_dir.name, "frames")
  dilate_path = os.path.join(temp_dir.name,
                             "diff_gray_dilate_frames")  # image 0
  gray_path = os.path.join(temp_dir.name, "diff_gray_frames")  # image 1
  diff_path = os.path.join(temp_dir.name, "diff_frames")  # image 2

  os.mkdir(frames_path)
  os.mkdir(dilate_path)
  os.mkdir(gray_path)
  os.mkdir(diff_path)

  return temp_dir, [frames_path, dilate_path, gray_path, diff_path]


def load_video(videoFile, filepath):
  count = 0

  cap = cv2.VideoCapture(videoFile)  # capturing the video from the given path
  frameRate = cap.get(5)  #frame rate - want to bump it up
  x = 1

  first_iter = True

  while (cap.isOpened()):
    frameId = cap.get(1)  #current frame number
    ret, frame = cap.read()
    if (ret != True):
      break
    else:
      filename = f"{filepath}/frames/frame{str(count).rjust(3, '0')}.jpg"
      count += 1
      cv2.imwrite(filename, frame)
      # Get average frames
      if first_iter:
        avg = np.float32(frame)
        first_iter = False
      cv2.accumulateWeighted(frame, avg, 0.005)
      background_image = cv2.convertScaleAbs(avg)
  cap.release()
  return background_image


def load_frames(filepath='frames/'):
  col_frames = os.listdir(filepath)

  # sort file names
  col_frames.sort(key=lambda f: int(re.sub('\D', '', f)))

  # empty list to store the frames
  col_images = []

  for i in col_frames:
    # read the frames
    img = cv2.imread(os.path.join(filepath, i))
    # append the frames to the list
    col_images.append(img)

  return col_images


def gen_dilated_frames(col_images, background_image, filepath):
  kernel = np.ones((4, 4), np.uint8)

  for i in range(len(col_images) - 1):

    # frame differencing

    diff_image = cv2.absdiff(cv2.cvtColor(col_images[i], cv2.COLOR_BGR2RGB),
                             cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB))
    gray_diff = cv2.cvtColor(diff_image, cv2.COLOR_BGR2GRAY)

    # image thresholding
    ret, thresh = cv2.threshold(gray_diff, 30, 255, cv2.THRESH_BINARY)

    # image dilation
    dilated = cv2.dilate(thresh, kernel, iterations=1)

    cv2.imwrite(filepath + str(i).rjust(3, '0') + '.png', dilated)


def gen_gray_frames(col_images, background_image, filepath):

  for i in range(len(col_images) - 1):

    # frame differencing

    diff_image = cv2.absdiff(cv2.cvtColor(col_images[i], cv2.COLOR_BGR2RGB),
                             cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB))
    gray_diff = cv2.cvtColor(diff_image, cv2.COLOR_BGR2GRAY)

    # image thresholding
    ret, thresh = cv2.threshold(gray_diff, 30, 255, cv2.THRESH_BINARY)

    cv2.imwrite(filepath + str(i).rjust(3, '0') + '.png', thresh)


def gen_diff_frames(col_images, background_image, filepath):

  for i in range(len(col_images) - 1):

    # frame differencing

    diff_image = cv2.absdiff(cv2.cvtColor(col_images[i], cv2.COLOR_BGR2RGB),
                             cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB))

    cv2.imwrite(filepath + str(i).rjust(3, '0') + '.png', diff_image)


def write_video(output_file, input_path, fps=60):

  frame_array = []
  file_list = [f for f in os.listdir(input_path)]

  file_list.sort(key=lambda f: int(re.sub('\D', '', f)))

  for i in range(len(file_list)):
    filename = input_path + file_list[i]

    #read frames
    img = cv2.imread(filename)
    try:
      height, width, layers = img.shape
      size = (width, height)
    except:
      pass

    #inserting the frames into an image array
    frame_array.append(img)

  out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'DIVX'), fps,
                        size)

  for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])

  out.release()


def main(videoFile="mystery_3.mp4"):

  temp_dir, output_dirs = gen_folders()
  background = load_video(videoFile, temp_dir.name)
  col_images = load_frames(output_dirs[0])

  gen_dilated_frames(col_images, background, output_dirs[1])
  write_video("mystery_0.mp4", output_dirs[1])

  gen_gray_frames(col_images, background, output_dirs[2])
  write_video("mystery_1.mp4", output_dirs[2])

  gen_diff_frames(col_images, background, output_dirs[3])
  write_video("mystery_2.mp4", output_dirs[3])

  temp_dir.cleanup()


if __name__ == "__main__":
  main()
