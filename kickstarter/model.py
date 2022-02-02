import pandas as pd
import tensorflow as tf

# Loading the pre-built model from local directory
MODEL = tf.keras.models.load_model('saved_model/kick_model')