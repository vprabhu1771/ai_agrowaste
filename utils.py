import speech_recognition as sr
import tensorflow as tf
import numpy as np
from PIL import Image

LABELS = ["banana_stem", "paddy_husk", "sugarcane_bagasse"]

def recognize_voice_in_tamil():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak your agro-waste in Tamil:")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='ta-IN')
        print("You said:", text)
        # Simple keyword mapping
        if "வாழை" in text:
            return "banana_stem"
        elif "நெல்" in text:
            return "paddy_husk"
        elif "கரும்பு" in text:
            return "sugarcane_bagasse"
        else:
            return "unknown"
    except Exception as e:
        print("Voice recognition error:", e)
        return "unknown"

def classify_image(image_path):
    model = tf.keras.models.load_model('model/agro_waste_classifier.h5')
    img = Image.open(image_path).resize((128, 128))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    return LABELS[class_index]

def estimate_co2_saved(waste_type):
    co2_map = {
        "banana_stem": 1.2,
        "paddy_husk": 0.9,
        "sugarcane_bagasse": 1.5
    }
    return co2_map.get(waste_type, 0.0)
