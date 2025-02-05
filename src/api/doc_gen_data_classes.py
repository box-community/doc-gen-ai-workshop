import random
from dataclasses import dataclass, field
from datetime import date
from typing import Optional

from dataclasses_json import dataclass_json
from dataclasses_jsonschema import JsonSchemaMixin


@dataclass_json
@dataclass
class MergeBase(JsonSchemaMixin):
    def to_dict(
        self,
        omit_none: bool = True,
        validate: bool = False,
        validate_enums: bool = True,
    ):
        return super().to_dict(
            omit_none,
            validate,
            validate_enums,
        )

    def to_json(self, **json_kwargs):
        return super().to_json(**json_kwargs)


@dataclass_json
@dataclass
class GenericNameDescription(MergeBase):
    name: str = ""
    description: str = ""


@dataclass_json
@dataclass
class GenericDescription(MergeBase):
    description: str = ""


@dataclass_json
@dataclass
class Movie(MergeBase):
    title: str = ""
    gross_revenue: str = ""

    def gen_sample_data():
        return Movie(
            title=f"The {random.randint(1111, 9999)} movie name",
            gross_revenue=f"{random.randint(100, 555)} million USD",
        )


@dataclass_json
@dataclass
class Accomplishment(GenericDescription):
    def gen_sample_data():
        return Accomplishment(description=f"Accomplished {random.randint(1, 10)} times")


@dataclass_json
@dataclass
class OtherScript(GenericDescription):
    def gen_sample_data():
        return OtherScript(description=f"Script Z{random.randint(1, 10)}")


@dataclass_json
@dataclass
class CompanyWorked(GenericDescription):
    def gen_sample_data():
        return CompanyWorked(description=f"Company X{random.randint(1, 10)}")


@dataclass_json
@dataclass
class Producer(GenericNameDescription):
    def gen_sample_data():
        return Producer(
            name=f"Producer {random.randint(1, 10)}",
            description=f"Famous for Movie V{random.randint(1, 10)}",
        )


@dataclass_json
@dataclass
class Director(GenericNameDescription):
    def gen_sample_data():
        return Director(
            name=f"Director {random.randint(1, 10)}",
            description=f"Famous for Movie Y{random.randint(1, 10)}",
        )


@dataclass_json
@dataclass
class Prop(GenericNameDescription):
    def gen_sample_data():
        return Prop(
            name=f"Prop {random.randint(1, 10)}",
            description=f"X{random.randint(1, 10)} description",
        )


@dataclass_json
@dataclass
class Location(GenericNameDescription):
    def gen_sample_data():
        return Location(
            name=f"Location {random.randint(1, 10)}",
            description=f"X{random.randint(1, 10)} description",
        )


@dataclass_json
@dataclass
class Actor(GenericDescription):
    def gen_sample_data():
        return Actor(description=f"Actor {random.randint(1, 10)}")


@dataclass_json
@dataclass
class Character(MergeBase):
    name: str = ""
    description: str = ""
    suggested_actors: str = ""

    def gen_sample_data():
        return Character(
            name=f"Character {random.randint(1, 10)}",
            description=f"Character {random.randint(1, 10)} description",
            suggested_actors="Actor A, Actor B, Actor C",
        )


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
            "description": "A summary of the plot of this movie script.",
        },
    )
    character_list: Optional[list[Character]] = None
    props: Optional[list[Prop]] = None
    locations: Optional[list[Location]] = None
    directors: Optional[list[Director]] = None
    producers: Optional[list[Producer]] = None
    accomplishments: Optional[list[Accomplishment]] = None
    other_scripts: Optional[list[OtherScript]] = None
    produced_movies: Optional[list[Movie]] = None
    companies_worked_with: Optional[list[CompanyWorked]] = None

    def gen_sample_data():
        return Script(
            title=f"Script {random.randint(1, 10)}",
            author=f"Author {random.randint(1, 10)}",
            genre=f"Genre {random.randint(1, 10)}",
            date_written="April 1st, 2021",
            date_written_iso=date(2021, 4, 1),
            plot_summary=f"Plot summary {random.randint(1, 10)}",
            character_list=[Character.gen_sample_data() for _ in range(3)],
            props=[Prop.gen_sample_data() for _ in range(3)],
            locations=[Location.gen_sample_data() for _ in range(3)],
            directors=[Director.gen_sample_data() for _ in range(3)],
            producers=[Producer.gen_sample_data() for _ in range(3)],
            accomplishments=[Accomplishment.gen_sample_data() for _ in range(3)],
            other_scripts=[OtherScript.gen_sample_data() for _ in range(3)],
            produced_movies=[Movie.gen_sample_data() for _ in range(3)],
            companies_worked_with=[CompanyWorked.gen_sample_data() for _ in range(3)],
        )
