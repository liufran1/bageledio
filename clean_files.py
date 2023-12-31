import cv2
import os
import re
import tempfile
import numpy as np
from datetime import date
from PIL import Image
import boto3
import json

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']


def get_video(awssession, today):
  # Download from s3
  s3 = awssession.resource('s3')
  s3_client = awssession.client('s3')

  filenames = [
    my_bucket_object.key
    for my_bucket_object in s3.Bucket('bageld-inputs').objects.all()
  ]

  videoFile = list(filter(lambda x: today in x, filenames))[0]

  player_name = videoFile.split(';')[1].replace('_', ' ')
  tour = videoFile.split(';')[2]
  s3_client.download_file('bageld-inputs', videoFile, videoFile[videoFile.find(';')+1:])

  return videoFile[videoFile.find(';')+1:], player_name, tour


def upload_game_params(awssession, player_name, tour):
  s3 = awssession.resource('s3')

  params_json = json.dumps(
    {
      'answerHash': hashAnswer(player_name.upper()),
      'tour': tour
    }, indent=4)

  s3.Bucket('bageld-inputs').put_object(Key='bageld_params.json',
                                        Body=params_json)


def gen_folders():
  temp_dir = tempfile.TemporaryDirectory()

  frames_path = os.path.join(temp_dir.name, "frames")
  dilate_path = os.path.join(temp_dir.name,
                             "diff_gray_dilate_frames")  # image 0
  gray_path = os.path.join(temp_dir.name, "diff_gray_frames")  # image 1
  diff_path = os.path.join(temp_dir.name, "diff_frames")  # image 2

  today = date.today()
  output_path = os.path.join(temp_dir.name, str(today))

  os.mkdir(frames_path)
  os.mkdir(dilate_path)
  os.mkdir(gray_path)
  os.mkdir(diff_path)
  os.mkdir(output_path)

  return temp_dir, [
    frames_path, dilate_path, gray_path, diff_path, output_path
  ]


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

    cv2.imwrite(os.path.join(filepath, str(i).rjust(3, '0') + '.png'), dilated)


def gen_gray_frames(col_images, background_image, filepath):

  for i in range(len(col_images) - 1):

    # frame differencing

    diff_image = cv2.absdiff(cv2.cvtColor(col_images[i], cv2.COLOR_BGR2RGB),
                             cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB))
    gray_diff = cv2.cvtColor(diff_image, cv2.COLOR_BGR2GRAY)

    # image thresholding
    ret, thresh = cv2.threshold(gray_diff, 30, 255, cv2.THRESH_BINARY)

    cv2.imwrite(os.path.join(filepath, str(i).rjust(3, '0') + '.png'), thresh)


def gen_diff_frames(col_images, background_image, filepath):

  for i in range(len(col_images) - 1):

    # frame differencing

    diff_image = cv2.absdiff(cv2.cvtColor(col_images[i], cv2.COLOR_BGR2RGB),
                             cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB))

    cv2.imwrite(os.path.join(filepath,
                             str(i).rjust(3, '0') + '.png'), diff_image)


def write_video(output_file, input_path, fps=60):

  frame_array = []
  file_list = [f for f in os.listdir(input_path)]

  file_list.sort(key=lambda f: int(re.sub('\D', '', f)))

  for i in range(len(file_list)):
    filename = os.path.join(input_path, file_list[i])

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


def write_gif(output_file, input_path):
  frame_array = []
  file_list = [f for f in os.listdir(input_path)]
  file_list.sort(key=lambda f: int(re.sub('\D', '', f)))

  for i in range(0, len(file_list), 4):
    filename = os.path.join(input_path, file_list[i])
    img = Image.open(filename)
    frame_array.append(img)

  frame_array[0].save(output_file,
                      format='GIF',
                      append_images=frame_array[1:],
                      save_all=True,
                      duration=0,
                      loop=0)


def hashAnswer(inputString):
  hash_value = 1
  if len(inputString) == 0:
    return hash_value
  for x in range(len(inputString)):
    ch = ord(inputString[x])
    hash_value = (hash_value * ch) % 100000000 + 1
  return hash_value


def main(cleanup_temp=True):
  today = str(date.today()).replace('-', '')

  session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
  s3_client = session.client('s3')

  videoFile, player_name, tour = get_video(awssession=session, today=today)
  upload_game_params(awssession=session, player_name=player_name, tour=tour)

  temp_dir, output_dirs = gen_folders()
  background = load_video(videoFile, temp_dir.name)
  col_images = load_frames(output_dirs[0])

  gen_dilated_frames(col_images, background, output_dirs[1])
  write_gif("mystery_0.gif", output_dirs[1])

  gen_gray_frames(col_images, background, output_dirs[2])
  write_gif("mystery_1.gif", output_dirs[2])

  gen_diff_frames(col_images, background, output_dirs[3])
  write_gif("mystery_2.gif", output_dirs[3])

  write_gif("mystery_3.gif", output_dirs[0])

  for i in range(4):
    s3_client.upload_file(f'mystery_{i}.gif', 'bagelio-files',
                          f'gifs/mystery_{i}.gif')

  # need new function to update the database of old games, and delete yesterday's raw video to save s3 space

  if cleanup_temp:
    temp_dir.cleanup()
  else:
    return temp_dir


if __name__ == "__main__":
  main()
