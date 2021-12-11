"""
translate between english and french
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator('7COw0tNIo7eeX1ismhAJdcvO6T9OZ7QkuaVleRLX4WRj')
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/c3be346f-a2b1-4277-afde-4fe634425ef0')


def english_to_french(english_text):
    """
    translate english to french
    """
    try:
        french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        return french_text['translations'][0]['translation']
    except ValueError:
        return None


def french_to_english(french_text):
    """
    translate french to english
    """
    try:
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        return english_text['translations'][0]['translation']
    except ValueError:
        return None
