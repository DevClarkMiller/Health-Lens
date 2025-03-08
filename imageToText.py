import PIL.Image
from PIL.ImageFile import ImageFile
from client import getFormatting, imagePrompt

class ImageToFacts:
    def __init__(self):
        self.format = getFormatting('label')

    def extractFacts(self, image: ImageFile):
        response =  imagePrompt(f"Please extract the text from this image into the following json format: {self.format}", image)
        return response

if __name__ == "__main__":
    imgToFacts = ImageToFacts()

    image = PIL.Image.open('pills.jpg')
    text = imgToFacts.extractFacts(image)
    print(text)