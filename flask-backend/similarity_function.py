import random
import cv2
import numpy as np


def random_similarity(a, b):
  return random.random()

def mse(a, b):
  imageA = cv2.imread(a)
  imageB = cv2.imread(b)
  # the 'Mean Squared Error' between the two images is the
  # sum of the squared difference between the two images;
  # NOTE: the two images must have the same dimension
  err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
  print("shape[0] is " + str(imageA.shape[0]))
  print("shape[1] is " + str(imageA.shape[1]))
  # print("err is " + str(err))
  err /= float(imageA.shape[0] * imageA.shape[1])
	
  # return the MSE, the lower the error, the more "similar"
  # the two images are
  return err