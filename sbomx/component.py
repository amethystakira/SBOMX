from dataclasses import dataclass # creates simple structured data class.

@dataclass
class Component:
    # Stores information about one software dependency.Component
    name: str
    version: str
    ecosystem : str

    @classmethod #let us create [Componenet] from another piece of data.{the other data is parsed}
    def from_dependency(cls, dependency, ecosystem): #receives {parsed dependency dictionary}, {eg. "python or "node}
        return cls( #creates a new component, {cls reefers to the "Component" class itself}
            name = dependency["name"], #gets the package name
            version=dependency["version"], #version
            ecosystem=ecosystem #ecosystem we detected
        )