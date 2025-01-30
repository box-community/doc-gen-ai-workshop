from dataclasses import dataclass

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
class Location:
    pass
    # name: str = ""
    # description: str = ""

    # def to_dict(self):
    #     return self.__dict__.copy()

    # def to_json(self):
    #     return json.dumps(self.to_dict(), indent=4)


@dataclass_json
@dataclass
class Character(MergeBase):
    name: str = ""
    description: str = ""
    suggested_actors: list[str] = None

    # def to_dict(self):
    #     return self.__dict__.copy()

    # def to_json(self):
    #     return json.dumps(self.to_dict(), indent=4)


@dataclass_json
@dataclass
class MergeData(MergeBase):
    title: str = ""
    author: str = ""
    genre: str = ""
    date_written: str = ""
    summary: str = ""
    character_list: list[Character] = None
    locations: list[Location] = None
    props: list[Prop] = None
    directors: list[Director] = None
    producers: list[Producer] = None
    screen_writer: Writer = None

    # def to_dict(self):
    #     return self.__dict__.copy()

    # def to_json(self):
    #     return json.dumps(self.to_dict(), indent=4)
