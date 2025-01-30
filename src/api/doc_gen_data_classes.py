from dataclasses import dataclass, field
from datetime import date
from typing import Optional

from dataclasses_json import dataclass_json
from dataclasses_jsonschema import JsonSchemaMixin


@dataclass_json
@dataclass
class MergeBase(JsonSchemaMixin):
    def to_dict(self):
        return super().to_dict()

    def to_json(self):
        return super().to_json()

    # def from_dict(self):
    #     return super().from_dict()

    # def from_json(self):
    #     return super().from_json()

    # def schema(self):
    #     return super().json_schema()


@dataclass_json
@dataclass
class GenericNameDescription(MergeBase):
    name: str = ""
    description: str = ""


@dataclass_json
@dataclass
class Movie(MergeBase):
    title: str = ""
    gross_revenue: str = ""


@dataclass_json
@dataclass
class Writer(MergeBase):
    name: str = ""
    accomplishments: list[str] = None
    other_scripts: list[str] = None
    produced_movies: list[Movie] = None
    companies_worked_with: list[str] = None

    # def to_dict(self):
    #     return self.__dict__.copy()

    # def to_json(self):
    #     return json.dumps(self.to_dict(), indent=4)


@dataclass_json
@dataclass
class Producer(GenericNameDescription):
    pass
    # name: str = ""
    # description: str = ""

    # def to_dict(self):
    #     return self.__dict__.copy()

    # def to_json(self):
    #     return json.dumps(self.to_dict(), indent=4)


@dataclass_json
@dataclass
class Director:
    pass
    # name: str = ""
    # description: str = ""

    # def to_dict(self):
    #     return self.__dict__.copy()

    # def to_json(self):
    #     return json.dumps(self.to_dict(), indent=4)


@dataclass_json
@dataclass
class Prop:
    pass
    # name: str = ""
    # description: str = ""

    # def to_dict(self):
    #     return self.__dict__.copy()

    # def to_json(self):
    #     return json.dumps(self.to_dict(), indent=4)


@dataclass_json
@dataclass
class Location(GenericNameDescription):
    pass


@dataclass_json
@dataclass
class Character(MergeBase):
    name: str = ""
    description: str = ""
    suggested_actors: list[str] = field(
        default=None,
        metadata={
            "description": "suggest 5 actors this character "
            "do not suggest the original movie actors if the movie has been already produced."
        },
    )

    # def to_dict(self):
    #     return self.__dict__.copy()

    # def to_json(self):
    #     return json.dumps(self.to_dict(), indent=4)


@dataclass_json
@dataclass
class CharacterList(MergeBase):
    characters: list[Character] = None


@dataclass_json
@dataclass
class Script(MergeBase):
    title: str = ""
    author: str = ""
    genre: str = ""
    date_written: str = ""
    date_written_iso: date = field(
        default=None, metadata={"description": "script written data in iso format"}
    )
    plot_summary: str = field(
        default="",
        metadata={
            "description": "A summary of the plot of the movies script.",
        },
    )
    locations: list[Location] = field(
        default=None,
        metadata={
            "description": "read this movie script and give me a list of locations "
            "with one sentence description for each location "
            "do not suggest the original movie locations if the movie has been already produced. "
            "compose this locations list in a json format ",
        },
    )


@dataclass_json
@dataclass
class MergeData(MergeBase):
    script: Optional[Script] = None
    character_list: Optional[list[Character]] = None
    locations: Optional[list[Location]] = None
    props: Optional[list[Prop]] = None
    directors: Optional[list[Director]] = None
    producers: Optional[list[Producer]] = None
    screen_writer: Optional[Writer] = None

    # def to_dict(self):
    #     return self.__dict__.copy()

    # def to_json(self):
    #     return json.dumps(self.to_dict(), indent=4)
