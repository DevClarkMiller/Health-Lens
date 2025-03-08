import PIL.Image
from client import getFormatting, imagePrompt

class ImageToText:
    def __init__(self, format: str, context: str = None):
        self.format = getFormatting(format)
        if context:
            self.prompt = f"Please extract the text from this image into the following json format using this context {context}: {self.format}"
        else:
            self.prompt = f"Please extract the text from this image into the following json format: {self.format}"

    def process(self, imagePath):
        image = PIL.Image.open(imagePath)
        response = imagePrompt(self.prompt, image)
        return response

class ImageToFacts(ImageToText):
    def __init__(self):
        super(ImageToFacts, self).__init__('label')

class ImageToDoctorsNote(ImageToText):
    def __init__(self, prefferredLanguage):
        context = f"Please simplify this doctors note into something that even a 10 year old could understand, and also translate into this language {prefferredLanguage}. If it's too hard to read and the sentence you piece together isn't complete, just enter null for all fields"

        context += ""
        super(ImageToDoctorsNote, self).__init__('doctornote', context)


if __name__ == "__main__":
    # imgToFacts = ImageToFacts()
    # text = imgToFacts.process('pills.jpg')
    imgToDoctorNote = ImageToDoctorsNote("english")
    text = imgToDoctorNote.process('docNote.webp')
    print(text)