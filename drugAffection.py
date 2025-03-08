import json
from client import getFormatting, textPrompt, getPrompt
from database import getDB

class DrugRegionParser:
    def __init__(self, drugName: str):
        self.drugName = drugName
        self.format = getFormatting('affection')

    # Fn: prompt()
    # Brief: Prompts the language model for the regions and afflication types for the drug
    def prompt(self):
        # response = textPrompt(f"Please describe the regions which this drug {self.drugName} affects the human body. Please respond in the following json template, "
        #     f"in the brain section, create list element depending on if the drug affects any of those regions. Also please don't list any rare cases, I only want the most common side effects. Also make the responseDescriptions very understandable for the average person. Don't consider high dosages at all. Only think about the regular dosages: {self.format}")
        # return response

        req = f"""
        You are a medical information specialist tasked with analyzing and describing the effects of a specific drug on the human body. Your goal is to provide a structured JSON response containing clear, accurate information about the drug's common effects at regular dosages.

        Here is the name of the drug you need to analyze:

        <drug_name>
        {self.drugName}
        </drug_name>

        Follow these guidelines for your analysis and final JSON response:

        1. Focus only on common effects that occur at regular dosages. Exclude rare side effects or effects from high dosages.
        2. Include information for a body system only if there are notable effects. Omit systems not significantly affected.
        3. Use language that is easily understandable for the average person.
        4. For the brain section, choose from the following regions: Olfactory Nerve (CN I), Optic Nerve (CN II), Optic Chiasm, Trochlear Nerve (CN IV), Trigeminal Nerve (CN V), Abducens Nerve (CN VI), Facial Nerve (CN VII), Vestibulocochlear Nerve (CN VIII), Glossopharyngeal Nerve (CN IX), Vagus Nerve (CN X), Mammillary Body, Basilar Artery, Pons, Medulla, Pyramid, Olive, Precentral Gyrus (Motor), Postcentral Gyrus (Sensory), Central Sulcus, Broca (Expressive Language).
        5. Use "POSITIVE" for beneficial effects and "NEGATIVE" for adverse effects.

        After your analysis, generate a JSON response using the following structure:

        {{
          "brain": [
            {{
              "region": "[Name of affected brain region]",
              "responseType": "[POSITIVE or NEGATIVE]",
              "responseDescription": "[Clear description of the effect]"
            }}
          ],
          "muscular": [
            {{
              "name": "[Name of affected muscle or muscle group]",
              "responseType": "[POSITIVE or NEGATIVE]",
              "responseDescription": "[Clear description of the effect]"
            }}
          ],
          "skeletal": [
            {{
              "name": "[Name of affected bone or bone group]",
              "responseType": "[POSITIVE or NEGATIVE]",
              "responseDescription": "[Clear description of the effect]"
            }}
          ],
          "organs": [
            {{
              "name": "[Name of affected organ]",
              "responseType": "[POSITIVE or NEGATIVE]",
              "responseDescription": "[Clear description of the effect]"
            }}
          ]
        }}

        Important: Your final output must be valid JSON only, with no additional text or explanations outside the JSON structure. Ensure all descriptions are clear and easily understandable for non-medical professionals.

        Please proceed with your analysis and JSON response for the drug specified.    
        """

        data = textPrompt(req, False)
        return data

    # Fn: query()
    # Brief: Queries the db for the drug
    # Rets: The data or None if it wasn't found
    def query(self):
        db = getDB()
        drugs = db['Drug']
        drug = drugs.find_one({"name": self.drugName})
        return drug

    # Fn: addDrug()
    # Brief: Adds the drug into mongo
    def addDrug(self, data):
        db = getDB()
        drugs = db['Drug']
        res = drugs.insert_one(data)
        data['_id'] = res.inserted_id

        # Now fetch the drug
        return data

    def setDrugName(self, drugName):
        self.drugName = drugName

    # Fn findAffected()
    # Brief: Check if the name of the drug already exists in the db, else prompt for it
    # Rets: str - The json of the affected regions in this format { brain: [], muscular: [], skeletal: [], organs: [] }
    def findAffected(self):
        # 1. Query for data
        data = self.query()

        # 2. If drug doesn't exist, then prompt for it
        if not data:
            promptData = self.prompt()
            newData = {
                "name": self.drugName,
                "form": None,
                "affections": json.loads(promptData)
            }
            data = self.addDrug(newData)
            return newData
        return data


# Seems to work how it's expected
if __name__ == "__main__":
    # regionParser = DrugRegionParser("ibuprofen")
    regionParser = DrugRegionParser("tylenol")
    regionParser.findAffected()

    regionParser.setDrugName('advil')
    regions = regionParser.findAffected()
