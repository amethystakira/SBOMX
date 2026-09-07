from dataclasses import dataclass # creates simple structured data class.

@dataclass
class Component:
    # Stores information about one software dependency.Component
    name: str
    version: str
    ecosystem : str