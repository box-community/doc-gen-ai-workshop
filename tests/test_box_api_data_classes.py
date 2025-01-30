from src.api import (
    Character,
    Director,
    GenericNameDescription,
    Location,
    MergeData,
    Movie,
    Prop,
    Writer,
)


def test_box_api_data_classes_generic():
    generic = GenericNameDescription(name="name", description="description")
    assert generic.name == "name"
    assert generic.description == "description"

    # to json
    generic_json = generic.to_json()
    assert generic_json == '{"name": "name", "description": "description"}'

    # to dict
    generic_dict = generic.to_dict()
    assert generic_dict == {"name": "name", "description": "description"}

    # from dict
    generic_new = GenericNameDescription.from_dict(generic_dict)
    assert generic_new.name == "name"
    assert generic_new.description == "description"
    assert generic_new == generic

    # from json
    generic_new = GenericNameDescription.from_json(generic_json)
    assert generic_new.name == "name"
    assert generic_new.description == "description"
    assert generic_new == generic

    # schema json
    schema_json = generic.json_schema()
    assert schema_json == {
        "allOf": [
            {"$ref": "#/definitions/MergeBase"},
            {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "default": ""},
                    "description": {"type": "string", "default": ""},
                },
            },
        ],
        "description": "GenericNameDescription(name: str = '', description: str = '')",
        "$schema": "http://json-schema.org/draft-06/schema#",
        "definitions": {
            "MergeBase": {
                "type": "object",
                "properties": {},
                "description": "MergeBase()",
            }
        },
    }


def test_box_api_data_classes_movies():
    movie = Movie(title="title", gross_revenue="gross_revenue")
    assert movie.title == "title"
    assert movie.gross_revenue == "gross_revenue"

    # to json
    movie_json = movie.to_json()
    assert movie_json == '{"title": "title", "gross_revenue": "gross_revenue"}'

    # to dict
    movie_dict = movie.to_dict()
    assert movie_dict == {"title": "title", "gross_revenue": "gross_revenue"}

    # from dict
    movie_new = Movie.from_dict(movie_dict)
    assert movie_new.title == "title"
    assert movie_new.gross_revenue == "gross_revenue"
    assert movie_new == movie

    # from json
    movie_new = Movie.from_json(movie_json)
    assert movie_new.title == "title"
    assert movie_new.gross_revenue == "gross_revenue"
    assert movie_new == movie

    # schema json
    schema_json = movie.json_schema()
    print(schema_json)
    assert schema_json == {
        "allOf": [
            {"$ref": "#/definitions/MergeBase"},
            {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "default": ""},
                    "gross_revenue": {"type": "string", "default": ""},
                },
            },
        ],
        "description": "Movie(title: str = '', gross_revenue: str = '')",
        "$schema": "http://json-schema.org/draft-06/schema#",
        "definitions": {
            "MergeBase": {
                "type": "object",
                "properties": {},
                "description": "MergeBase()",
            }
        },
    }
