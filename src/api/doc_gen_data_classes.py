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


@dataclass_json
@dataclass
class Accomplishment(GenericDescription):
    pass


@dataclass_json
@dataclass
class OtherScript(GenericDescription):
    pass


@dataclass_json
@dataclass
class CompanyWorked(GenericDescription):
    pass


# TODO: Dead code, remove it
# @dataclass_json
# @dataclass
# class Writer(MergeBase):
#     name: str = ""
#     accomplishments: list[Accomplishment] = None
#     other_scripts: list[OtherScript] = None
#     produced_movies: list[Movie] = None
#     companies_worked_with: list[CompanyWorked] = None


@dataclass_json
@dataclass
class Producer(GenericNameDescription):
    pass


@dataclass_json
@dataclass
class Director(GenericNameDescription):
    pass


@dataclass_json
@dataclass
class Prop(GenericNameDescription):
    pass


@dataclass_json
@dataclass
class Location(GenericNameDescription):
    pass


@dataclass_json
@dataclass
class Actor(GenericDescription):
    pass


@dataclass_json
@dataclass
class Character(MergeBase):
    name: str = ""
    description: str = ""
    suggested_actors: list[Actor] = field(
        default=None,
        metadata={
            "description": "suggest 5 actors this character "
            "do not suggest the original movie actors if the movie has been already produced."
        },
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
            "description": "A summary of the plot of the movies script.",
        },
    )

    locations: list[Location] = field(
        default=None,
        metadata={
            "description": "read this movie script and give me a list of up to a maximum 10 locations "
            "with one sentence description for each location "
            "do not suggest the original movie locations if the movie has been already produced. "
        },
    )
    props: Optional[list[Prop]] = field(
        default=None,
        metadata={
            "description": "read this movie script and give me a list of up to 10 props "
            "with one sentence description for each prop. "
        },
    )


@dataclass_json
@dataclass
class MergeData(MergeBase):
    script: Optional[Script] = None
    character_list: Optional[list[Character]] = field(
        default=None,
        metadata={
            "description": "read this movie script and give me a character list, "
            "(without the original actor name, just the character name) "
            "with one sentence description ",
        },
    )

    directors: Optional[list[Director]] = None
    producers: Optional[list[Producer]] = None
    # screen_writer: Optional[Writer] = None
    accomplishments: Optional[list[Accomplishment]] = None
    other_scripts: Optional[list[OtherScript]] = None
    produced_movies: Optional[list[Movie]] = None
    companies_worked_with: Optional[list[CompanyWorked]] = None
