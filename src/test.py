import tensorflow as tf

model = tf.keras.models.load_model(
    'C:/Users/Aravind/Work/PROJECTS/Cloudburst-Prediction-System/models/api_model')

temp = [[28.6128, 77.2311, 302.24, 302.69, 1012, 48, 0, 0]]
pred = model.predict(temp)
print(pred)
