from dataclasses import asdict # Converts dataclasses into dictionaries.
from .component import Component # Imports the Component class.
import json # convert SBOM dtaa from JSON

class SBOM:
    def __init__(self): #Initializing the SBOM with the Component class.
        # store all discovered componenets.
        self.components = []
    
    def add_component(self, component):
        #add one component to the SBOM
        self.components.append(component)

    def to_dict(self):
        # Convert the sbom into json friendly data.
        return{
            "components": [asdict(component) for component in self.components]
        }
    
    def to_json(self, output_path):
        data = json.dumps(self.to_dict(), indent = 2) #convert to readable string with indent.

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(data)

