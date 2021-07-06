"""Stream type classes for tap-learndash."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_learndash.client import LearnDashStream

# TODO: Delete this is if not using json files for schema definition - AL
# SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition. - AL
#       - Copy-paste as many times as needed to create multiple stream types. - AL


class CoursesStream(LearnDashStream):
    """Define custom stream."""
    name = "courses"
    path = "/sfwd-courses"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("date", th.DateTimeType),
        th.Property("date_gmt", th.DateTimeType),
        th.Property("guid", th.StringType),
        th.Property("id", th.IntegerType),
        th.Property("modified", th.DateTimeType),
        th.Property("modified_gmt", th.DateTimeType),
        th.Property("slug", th.StringType),
        th.Property("status", th.StringType),
        th.Property("type", th.StringType),
        th.Property("link", th.StringType),
        th.Property("title", th.StringType),
        th.Property("content", th.StringType),
        th.Property("author", th.IntegerType),
        th.Property("featured_media", th.IntegerType),
        th.Property("menu_order", th.IntegerType),
        th.Property("template", th.StringType),
        th.Property("categories", th.ArrayType(th.StringType)),
        th.Property("tags", th.ArrayType(th.StringType)),
        th.Property("ld_course_category", th.ArrayType(th.IntegerType)),
        th.Property("ld_course_tag", th.ArrayType(th.IntegerType)),
        th.Property("materials_enabled", th.BooleanType),
        th.Property("materials", th.StringType),
        th.Property("certificate", th.IntegerType),
        th.Property("disable_content_table", th.BooleanType),
        th.Property("lessons_per_page", th.BooleanType),
        th.Property("lesson_per_page_custom", th.IntegerType),
        th.Property("topic_per_page_custom", th.IntegerType),
        th.Property("price_type", th.StringType),
        # th.Property("price_type_paynow_price", th.StringType),
        # th.Property("price_type_subscribe_price", th.StringType),
        # th.Property("price_type_closed_price", th.StringType),
        # th.Property("price_type_closed_custom_button_url", th.StringType),
        th.Property("prerequisite_enabled", th.BooleanType),
        th.Property("prerequisite_compare", th.StringType),
        th.Property("prerequisites", th.ArrayType(th.StringType)),
        th.Property("points_enabled", th.BooleanType),
        th.Property("points_access", th.NumberType),
        th.Property("points_amount", th.NumberType),
        th.Property("progression_disabled", th.BooleanType),
        th.Property("expire_access", th.BooleanType),
        th.Property("expire_access_days", th.IntegerType),
        th.Property("expire_access_delete_progress", th.BooleanType)
    ).to_dict()


# class GroupsStream(LearnDashStream):
#     """Define custom stream."""
#     name = "groups"
#     path = "/groups"
#     primary_keys = ["id"]
#     replication_key = "modified"
#     schema = th.PropertiesList(
#         th.Property("name", th.StringType),
#         th.Property("id", th.StringType),
#         th.Property("modified", th.DateTimeType),
#     ).to_dict()
