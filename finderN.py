from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np


model = load_model('keras_modelN.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def machine(image):
    #image = Image.open('ksyoa.png')

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)

    prediction = prediction[0]
    values = np.array(prediction)
    index_min = np.argmax(values)

    return list[index_min]


list = [
    '2',
    '3',
    '4',
    '6',
    '7',
    '8',
    '9',
    'T',
    'J',
    'Q',
    'K',
    'A',
    '5'
]
