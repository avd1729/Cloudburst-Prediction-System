import tensorflow as tf
import requests
import datetime as dt

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

API_KEY = ""

CITY = "New Delhi"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

json_data = response


def extract_features_from_json(json_data, feature_names):
    result = []

    for item in json_data:
        feature_values = [get_nested_value(item, name)
                          for name in feature_names]
        result.append(feature_values)

    return result


def get_nested_value(obj, key):
    keys = key.split('.')
    for k in keys:
        if isinstance(obj, dict) and k in obj:
            obj = obj[k]
        elif isinstance(obj, list) and len(obj) > 0:
            obj = obj[int(k)]
        else:
            return None
    return obj


feature_names = ['coord.lat', 'coord.lon', 'main.temp', 'main.feels_like',
                 'main.pressure', 'main.humidity', 'wind.speed', 'wind.deg']

result = extract_features_from_json([json_data], feature_names)


model = tf.keras.models.load_model(
    'C:/Users/Aravind/Work/PROJECTS/Cloudburst-Prediction-System/models/api_model')

pred = model.predict(result)
print(pred)
