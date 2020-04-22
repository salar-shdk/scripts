import requests, notify2, googletrans, six
from googletrans import Translator
from subprocess import check_output

FROM = 'auto'
TO = 'fa'
text = check_output('xclip -out -selection'.split()).decode()

translate_client = Translator()

if isinstance(text, six.binary_type):
    text = text.decode('utf-8')

result = translate_client.translate(
    text,dest=TO, src=FROM)

notify2.init(text)
n = notify2.Notification(text, result.text)
n.show()
print(googletrans.LANGUAGES)
