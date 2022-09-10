from tensorflow import keras
import cv2
import tensorflow as tf
from PIL import Image
import numpy as np

################################################
#           Muhammad Talha Ejaz                #
#          talha.ej@hotmail.com                #   
################################################

image_size = (180, 180)
interpreter = tf.lite.Interpreter("model.tflite")  #license plate classification
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def obs_classify(image):
    cvt_image =  cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(cvt_image)
    img = im_pil.resize((180, 180))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis
    input_shape = input_details[0]['shape']
    input_data = np.array(img_array, dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])[0][0]
  
  
    print(output_data)

    if output_data >=0.5:

        return("OBSTACLE Detected")
    else:
        return("OBSTACLE Not Detected")
