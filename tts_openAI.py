import openai

your_openai_key = 'sk-...' #Your openAI API key
d = {
    'English': 'Artificial Inteligence is a mind blowing!',
    'Hindi': 'कृत्रिम बुद्धिमता अद्भुत है!'
}


client = openai.OpenAI(api_key=your_openai_key)
voices = ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer']

for language in d:
    response = client.audio.speech.create(
        model="tts-1",
        voice='onyx',
        input=d[language]
    )

    response.stream_to_file(f'{language}.mp3')