from Videoprocessing import extract_video_data
from keras.models import load_model

def detect_visual_events(frames):
    model = load_model("action_recognition_model.h5")
    important_frames = []
    
    for frame in frames:
        # Preprocess the frame before passing it to the model
        frame_resized = cv2.resize(frame, (224, 224))  # Resize for model input
        frame_resized = np.expand_dims(frame_resized, axis=0)
        
        prediction = model.predict(frame_resized)
        if prediction > 0.5:  # Assuming 0.5 as threshold for key event
            important_frames.append(True)
        else:
            important_frames.append(False)
    
    return important_frames

def detect_audio_events(audio, sr):
    energy = librosa.feature.rms(audio)[0]
    threshold = np.mean(energy) * 1.5  # Define a threshold for key moments
    
    audio_events = energy > threshold
    return audio_events

from transformers import BertTokenizer, BertForSequenceClassification

def analyze_commentary(commentary_texts):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased')
    
    key_event_commentary = []
    
    for commentary in commentary_texts:
        inputs = tokenizer(commentary, return_tensors="pt")
        outputs = model(**inputs)
        
        if outputs.logits[0][1] > 0.5:  # Assuming 0.5 threshold for important event detection
            key_event_commentary.append(True)
        else:
            key_event_commentary.append(False)
    
    return key_event_commentary

def combine_modalities(visual_events, audio_events, commentary_events):
    combined_events = []
    
    for i in range(len(visual_events)):
        if visual_events[i] or audio_events[i] or commentary_events[i]:
            combined_events.append(True)
        else:
            combined_events.append(False)
    
    return combined_events


