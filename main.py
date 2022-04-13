from time import sleep

import openai
from supabase import create_client

from constants import curse_words, API_KEY, emojis, supabase_url, supabase_key

openai.api_key = API_KEY
f = 'file-LXusegCxGmDfrqOfON1XB3qw'

def filter_words(text):
    new = text.lower()
    for key in curse_words:
        if key in new:
            new = new.replace(key, curse_words[key])
    return new

def run_inference(text):
    prompt_text = f"Determine if the Text's emotion is Joy, Fear, Anger, Sadness, Love, or Surprise.\n\nText: {text}\n\nEmotion:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_text,
        temperature=0.7,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    choices = response.get('choices')
    if not choices:
        return 'unknown'
    text = choices[0].get('text')
    if not text:
        return 'unknown'
    return text.strip().lower()

def run_classification(text):
    response = openai.Classification.create(
        file=f,
        query=text,
        search_model="ada",
        model="curie",
        max_examples=3
    )

    label = response.get('label')
    if label == "Unknown" or not label:
        print(response)
        return "unknown"
    return label.lower()

def get_latest_entry(supabase_client):
    data = supabase_client.table("journals").select("*").order('id', desc=True).limit(1).execute()
    if len(data.data) <= 0:
        return None
    return data.data[0]

if __name__=="__main__":
    # print(run_inference("I like trains."))
    supabase = create_client(supabase_url, supabase_key)
    while True:
        data = get_latest_entry(supabase)
        inference = data.get('inference')
        if not inference:
            print(data)
            try:
                # new_inference = run_classification(filter_words(data.get('entry')))
                new_inference = run_inference(data.get('entry'))
                if new_inference == 'unknown':
                    new_inference = data.get('mood')
                else:
                    new_inference = emojis[new_inference]
            except:
                new_inference = data.get('mood')
            data = supabase.table('journals').update({"inference": new_inference}).eq('id', data.get('id')).execute()
            print(data.data)
        sleep(5)