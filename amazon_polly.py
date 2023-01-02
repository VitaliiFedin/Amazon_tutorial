import boto3

polly = boto3.client('polly')
result = polly.synthesize_speech(Text='Hello my name is Venator',
                                 OutputFormat='mp3',
                                 VoiceId='Kendra')

audio = result['AudioStream'].read()
with open('myfile.mp3', 'wb') as file:
    file.write(audio)
