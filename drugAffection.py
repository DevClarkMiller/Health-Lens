import json
from client import getFormatting, textPrompt

class DrugRegionParser:
    def __init__(self, drugName: str):
        self.drugName = drugName
        self.format = getFormatting('affection')

    # Fn: promptRegions()
    # Brief: Prompts the language model for the regions and afflication types for the drug
    def promptRegions(self):
        response = textPrompt(f"Please describe the regions which this drug {self.drugName} affects the human body. Please respond in the following json template, "
                              f"in the brain section, create list element depending on if the drug affects any of those regions. Also please don't list any rare cases.: {self.format}")
        return response

    # Fn affectedRegions()
    # Brief: Check if the name of the drug already exists in the db, else prompt for it
    # Rets: str - The json of the affected regions in this format { brain: [], muscular: [], skeletal: [], organs: [] }
    # def affectedRegions(self):
    #     # 1. Check db for existence of drug
    #
    #     # 2. If drug doesn't exist, then prompt for it
    #
    #     pass


# Seems to work how it's expected
if __name__ == "__main__":
    regionParser = DrugRegionParser("ibuprofen")
    regions = regionParser.promptRegions()
    print(regions)
    # print(json.loads(regions))