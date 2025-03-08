import PIL.Image
from PIL.ImageFile import ImageFile
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get('GEMINI_KEY')

class ImageToFacts:
    def __init__(self):
        self.client = genai.Client(api_key=API_KEY)

    def extract_details(self, image: ImageFile):
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=["Please extract the text from this image into json format", image])
        return response.text

if __name__ == "__main__":
    imgToFacts = ImageToFacts()

    image = PIL.Image.open('pills.jpg')
    text = imgToFacts.extract_details(image)
    print(text)