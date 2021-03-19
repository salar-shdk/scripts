from subprocess import check_output
import notify2
import googletrans
import six
from googletrans import Translator

FROM = 'auto'
TO = 'fa'
text = check_output('xclip -out -selection'.split()).decode()

translate_client = Translator()

if isinstance(text, six.binary_type):
    text = text.decode('utf-8')
print(text)
result = translate_client.translate(
    text, dest=TO, src=FROM)
# print(result)
notify2.init(text)

n = notify2.Notification(text, result.text)
n.show()
# print(googletrans.LANGUAGES)
