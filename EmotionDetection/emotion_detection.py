import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analisa o texto fornecido usando a API Watson NLP e retorna as pontuações das emoções.
    """
    url = 'https://sn-watson-emotion.p.cloud.ibm.com/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=header)
    
    # Tarefa 7: Tratamento de erro para código de status 400 (entrada vazia)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Tarefa 3: Formatação da saída
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    
    # Cálculo da emoção dominante
    emotion_dict = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
