from django.shortcuts import render

# Create your views here.

import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import pandas as pd
from django.conf import settings
import tensorflow as tf
import base64
from PIL import Image
from io import BytesIO
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np

# 모델 load
print ("------------model load-------------")
model = tf.keras.models.load_model('dog_breed.hdf5')
print ("---------master load----------")
labels_ohe_names = pd.read_pickle("./master.pkl")

# Create your views here.
@api_view(['GET'])
def index_page(request):
    return_data = {
        "error" : "0",
        "message" : "Successful",
    }
    return Response(return_data)


count = 0
# Create your views here.
@api_view(['GET'])
def encore(request):
    id_ = request.query_params.get("id")
    pass_ = request.query_params.get("pass")
    print (id_, pass_)

    global count
    count += 1
    return_data =  "{},{}<br> {} :: ".format(id_, pass_, count)

    return Response(return_data)

def encore_view(request):
    return render(request, 'ajax01_count.html')

@api_view(["POST"])
def predict_model(request):
    base64_string = request.data.get('image')
    img = Image.open(BytesIO(base64.b64decode(base64_string)))
    print (type(img))
    img.save("3.png")
    dog_image =img_to_array(load_img("./{}".format("3.png"), target_size=(299,299))).astype('float32')
    # img_to_array(load_img("{}".format(target), target_size=(299,299))).astype('float32')
    dog_image = dog_image.reshape(1, 299, 299, 3)
    dog_image /= 255
    result = labels_ohe_names.columns[np.argmax(model.predict(dog_image))]
    
    return_value = { "breed" : result}
    
    return Response(return_value)
