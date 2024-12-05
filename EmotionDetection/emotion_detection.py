import requests
import json

def emotion_detector(text_to_analyze):
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    Input_json={ "raw_document": { "text": text_to_analyze }}
    
    response= requests.post(url=URL, headers=Headers, json=Input_json)

    json_response=response.json()
    emotions=json_response["emotionPredictions"][0]
    all_emotions={}

    for key, value in emotions['emotion'].items():
        all_emotions[key]= value
    
    dominant_emotion=max(all_emotions.items(),key=lambda x: x[1])
    all_emotions['dominant_emotion']= dominant_emotion[0] 
    return all_emotions
