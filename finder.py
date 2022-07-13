from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np


model = load_model('keras_model.h5')
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
    '2c',
    '2d',
    '2h',
    '2s',
    '3c',
    '3d',
    '3h',
    '3s',
    '4c',
    '4d',
    '4h',
    '4s',
    '5c',
    '5d',
    '5h',
    '5s',
    '6c',
    '6d',
    '6h',
    '6s',
    '7c',
    '7d',
    '7h',
    '7s',
    '8c',
    '8d',
    '8h',
    '8s',
    '9c',
    '9d',
    '9h',
    '9s',
    'Tc',
    'Td',
    'Th',
    'Ts',
    'Jc',
    'Jd',
    'Jh',
    'Js',
    'Qc',
    'Qd',
    'Qh',
    'Qs',
    'Kc',
    'Kd',
    'Kh',
    'Ks',
    'Ac',
    'Ad',
    'Ah',
    'As'
]
