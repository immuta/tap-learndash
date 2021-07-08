"""Stream type classes for tap-learndash."""

import requests
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
        th.Property("price_type_paynow_price", th.StringType),
        th.Property("price_type_subscribe_price", th.StringType),
        th.Property("price_type_closed_price", th.StringType),
        th.Property("price_type_closed_custom_button_url", th.StringType),
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

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "course_id": record["id"]
        }


class CoursesPrerequisitesStream(LearnDashStream):
    """Define custom stream."""
    name = "courses_prerequisites"
    path = "/sfwd-courses/{course_id}/prerequisites"
    primary_keys = ["course_id", "id"]
    parent_stream_type = CoursesStream
    ignore_parent_replication_keys = True
    schema = th.PropertiesList(
        th.Property("course_id", th.IntegerType),
        th.Property("id", th.IntegerType),
        th.Property("date", th.DateTimeType),
        th.Property("date_gmt", th.DateTimeType),
        th.Property("guid", th.StringType),
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
        th.Property("ld_course_category", th.ArrayType(th.StringType)),
        th.Property("ld_course_tag", th.ArrayType(th.StringType)),
        th.Property("_links", th.StringType)
    ).to_dict()


class CoursesUsersStream(LearnDashStream):
    """Define custom stream."""
    name = "courses_users"
    path = "/sfwd-courses/{course_id}/users"
    primary_keys = ["course_id", "id"]
    parent_stream_type = CoursesStream
    ignore_parent_replication_keys = True
    schema = th.PropertiesList(
        th.Property("course_id", th.IntegerType),
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("url", th.StringType),
        th.Property("description", th.StringType),
        th.Property("link", th.StringType),
        th.Property("slug", th.StringType),
        th.Property("avatar_urls", th.StringType),
        th.Property("meta", th.StringType),
        th.Property("_links", th.StringType)
    ).to_dict()

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "user_id": record["id"]
        }

    def post_process(self, row: dict, context: Optional[dict] = None) -> dict:
        """As needed, append or transform raw data to match expected structure.
        Optional. This method gives developers an opportunity to "clean up" the results
        prior to returning records to the downstream tap - for instance: cleaning,
        renaming, or appending properties to the raw record result returned from the
        API.
        """
        row["course_id"] = context["course_id"]
        return row


class CoursesGroupsStream(LearnDashStream):
    """Define custom stream."""
    # At the moment this stream returns empty so I have no good idea what to add on the properties list
    name = "courses_groups"
    path = "/sfwd-courses/{course_id}/groups"
    primary_keys = ["course_id", "id"]
    parent_stream_type = CoursesStream
    ignore_parent_replication_keys = True
    schema = th.PropertiesList(
        th.Property("course_id", th.IntegerType)
    ).to_dict()


class AssignmentsStream(LearnDashStream):
    """Define custom stream."""
    name = "assignments"
    path = "/sfwd-assignment"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("date", th.DateTimeType),
        th.Property("date_gmt", th.DateTimeType),
        th.Property("guid", th.StringType),
        th.Property("modified", th.DateTimeType),
        th.Property("modified_gmt", th.DateTimeType),
        th.Property("slug", th.StringType),
        th.Property("status", th.StringType),
        th.Property("type", th.StringType),
        th.Property("link", th.StringType),
        th.Property("title", th.StringType),
        th.Property("author", th.IntegerType),
        th.Property("comment_status", th.StringType),
        th.Property("ping_status", th.StringType),
        th.Property("template", th.StringType),
        th.Property("course", th.IntegerType),
        th.Property("lesson", th.IntegerType),
        th.Property("topic", th.IntegerType),
        th.Property("approved_status", th.StringType),
        th.Property("points_enabled", th.BooleanType),
        th.Property("points_max", th.IntegerType),
        th.Property("points_awarded", th.IntegerType),
        th.Property("_links", th.StringType)
    ).to_dict()


class EssaysStream(LearnDashStream):
    """Define custom stream."""
    name = "essays"
    path = "/sfwd-essays"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("date", th.DateTimeType),
        th.Property("date_gmt", th.DateTimeType),
        th.Property("guid", th.StringType),
        th.Property("modified", th.DateTimeType),
        th.Property("modified_gmt", th.DateTimeType),
        th.Property("slug", th.StringType),
        th.Property("status", th.StringType),
        th.Property("type", th.StringType),
        th.Property("link", th.StringType),
        th.Property("title", th.StringType),
        th.Property("content", th.StringType),
        th.Property("author", th.IntegerType),
        th.Property("comment_status", th.StringType),
        th.Property("ping_status", th.StringType),
        th.Property("template", th.StringType),
        th.Property("course", th.IntegerType),
        th.Property("lesson", th.IntegerType),
        th.Property("topic", th.IntegerType),
        th.Property("points_max", th.IntegerType),
        th.Property("points_awarded", th.IntegerType),
        th.Property("_links", th.StringType)
    ).to_dict()


class GroupsStream(LearnDashStream):
    """Define custom stream."""
    # At the moment this stream returns empty so I have no good idea what to add on the properties list
    name = "groups"
    path = "/groups"
    primary_keys = []
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("date", th.DateTimeType),
        th.Property("date_gmt", th.DateTimeType),
        th.Property("guid", th.StringType),
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
        th.Property("template", th.StringType),
        th.Property("categories", th.ArrayType(th.StringType)),
        th.Property("tags", th.ArrayType(th.StringType)),
        th.Property("ld_group_category", th.ArrayType(th.StringType)),
        th.Property("ld_group_tag", th.ArrayType(th.StringType)),
        th.Property("materials_enabled", th.BooleanType),
        th.Property("materials", th.StringType),
        th.Property("certificate", th.IntegerType),
        th.Property("disable_content_table", th.BooleanType),
        th.Property("courses_per_page_custom", th.IntegerType),
        th.Property("courses_orderby", th.StringType),
        th.Property("courses_order", th.StringType),
        th.Property("price_type", th.StringType),
        th.Property("price_type_paynow_price", th.StringType),
        th.Property("price_type_subscribe_price", th.StringType),
        th.Property("price_type_closed_price", th.StringType),
        th.Property("price_type_closed_custom_button_url", th.StringType),
        th.Property("_links", th.StringType)
    ).to_dict()


class LessonsStream(LearnDashStream):
    """Define custom stream."""
    name = "lessons"
    path = "/sfwd-lessons"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("date", th.DateTimeType),
        th.Property("date_gmt", th.DateTimeType),
        th.Property("guid", th.StringType),
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
        th.Property("ld_lesson_category", th.ArrayType(th.StringType)),
        th.Property("ld_lesson_tag", th.ArrayType(th.StringType)),
        th.Property("materials_enabled", th.BooleanType),
        th.Property("materials", th.StringType),
        th.Property("video_enabled", th.BooleanType),
        th.Property("video_url", th.StringType),
        th.Property("video_shown", th.StringType),
        th.Property("video_auto_complete", th.BooleanType),
        th.Property("video_auto_complete_delay", th.IntegerType),
        th.Property("video_show_complete_button", th.BooleanType),
        th.Property("video_auto_start", th.BooleanType),
        th.Property("video_show_controls", th.BooleanType),
        th.Property("video_focus_pause", th.BooleanType),
        th.Property("video_resume", th.BooleanType),
        th.Property("assignment_upload_enabled", th.BooleanType),
        th.Property("assignment_points_enabled", th.BooleanType),
        th.Property("assignment_points_amount", th.IntegerType),
        th.Property("assignment_auto_approve", th.BooleanType),
        th.Property("assignment_deletion_enabled", th.BooleanType),
        th.Property("forced_timer_enabled", th.IntegerType),
        th.Property("forced_timer_amount", th.BooleanType),
        th.Property("course", th.IntegerType),
        th.Property("is_sample", th.BooleanType),
        th.Property("visible_type", th.StringType),
        th.Property("assignment_upload_limit_extensions", th.StringType),
        th.Property("assignment_upload_limit_size", th.StringType),
        th.Property("assignment_upload_limit_count", th.IntegerType),
        th.Property("visible_after", th.IntegerType),
        th.Property("visible_after_specific_date", th.DateTimeType),
        th.Property("_links", th.StringType)
    ).to_dict()


class QuestionStream(LearnDashStream):
    """Define custom stream."""
    name = "question"
    path = "/sfwd-question"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("date", th.DateTimeType),
        th.Property("date_gmt", th.DateTimeType),
        th.Property("guid", th.StringType),
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
        th.Property("quiz", th.IntegerType),
        th.Property("correct_message", th.StringType),
        th.Property("incorrect_message", th.StringType),
        th.Property("hints_enabled", th.BooleanType),
        th.Property("hints_message", th.BooleanType),
        th.Property("points", th.IntegerType),
        th.Property("points_per_answer", th.BooleanType),
        th.Property("question_type", th.StringType),
        th.Property("answer_sets", th.StringType),
        th.Property("_links", th.StringType)
    ).to_dict()


class QuizStream(LearnDashStream):
    """Define custom stream."""
    name = "quiz"
    path = "/sfwd-quiz"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("date", th.DateTimeType),
        th.Property("date_gmt", th.DateTimeType),
        th.Property("guid", th.StringType),
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
        th.Property("course", th.IntegerType),
        th.Property("lesson", th.IntegerType),
        th.Property("prerequisites", th.ArrayType(th.StringType)),
        th.Property("registered_users_only", th.BooleanType),
        th.Property("passing_percentage", th.NumberType),
        th.Property("certificate_award_threshold", th.NumberType),
        th.Property("retry_restrictions_enabled", th.BooleanType),
        th.Property("retry_repeats", th.StringType),
        th.Property("answer_all_questions_enabled", th.BooleanType),
        th.Property("time_limit_enabled", th.BooleanType),
        th.Property("time_limit_time", th.IntegerType),
        th.Property("materials_enabled", th.BooleanType),
        th.Property("materials", th.StringType),
        th.Property("auto_start", th.BooleanType),
        th.Property("quiz_modus", th.StringType),
        th.Property("review_table_enabled", th.BooleanType),
        th.Property("summary_hide", th.BooleanType),
        th.Property("skip_question_disabled", th.BooleanType),
        th.Property("custom_sorting", th.BooleanType),
        th.Property("sort_categories", th.BooleanType),
        th.Property("question_random", th.BooleanType),
        th.Property("show_max_question", th.BooleanType),
        th.Property("show_points", th.BooleanType),
        th.Property("show_category", th.BooleanType),
        th.Property("hide_question_position_overview", th.BooleanType),
        th.Property("hide_question_numbering", th.BooleanType),
        th.Property("numbered_answer", th.BooleanType),
        th.Property("answer_random", th.BooleanType),
        th.Property("title_hidden", th.BooleanType),
        th.Property("restart_button_hide", th.BooleanType),
        th.Property("show_average_result", th.BooleanType),
        th.Property("show_category_score", th.BooleanType),
        th.Property("hide_result_points", th.BooleanType),
        th.Property("hide_result_correct_question", th.BooleanType),
        th.Property("hide_result_quiz_time", th.BooleanType),
        th.Property("custom_answer_feedback", th.BooleanType),
        th.Property("hide_answer_message_box", th.BooleanType),
        th.Property("disabled_answer_mark", th.BooleanType),
        th.Property("view_question_button_hidden", th.BooleanType),
        th.Property("toplist_enabled", th.BooleanType),
        th.Property("toplist_data_add_permissions", th.StringType),
        th.Property("toplist_data_add_multiple", th.BooleanType),
        th.Property("toplist_data_add_automatic", th.BooleanType),
        th.Property("toplist_data_show_limit", th.IntegerType),
        th.Property("toplist_data_sort", th.StringType),
        th.Property("toplist_data_showin_enabled", th.BooleanType),
        th.Property("statistics_enabled", th.BooleanType),
        th.Property("view_profile_statistics_enabled", th.BooleanType),
        th.Property("statistics_ip_lock_enabled", th.BooleanType),
        th.Property("email_enabled", th.BooleanType),
        th.Property("email_admin_enabled", th.BooleanType),
        th.Property("email_user_enabled", th.BooleanType),
        th.Property("certificate", th.IntegerType),
        th.Property("_links", th.StringType)
    ).to_dict()

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "quiz_id": record["id"]
        }


# class QuizStatisticsStream(LearnDashStream):
#     """Define custom stream."""
#     # Working but getting access error for certain quiz_ids
#     name = "quiz_statistics"
#     path = "/sfwd-quiz/{quiz_id}/statistics"
#     primary_keys = ["quiz_id", "id"]
#     parent_stream_type = QuizStream
#     ignore_parent_replication_keys = True
#     schema = th.PropertiesList(
#         th.Property("quiz_id", th.IntegerType),
#         th.Property("id", th.IntegerType),
#         th.Property("quiz", th.IntegerType),
#         th.Property("user", th.IntegerType),
#         th.Property("date", th.DateTimeType),
#         th.Property("answers_correct", th.IntegerType),
#         th.Property("answers_incorrect", th.IntegerType),
#         th.Property("points_scored", th.IntegerType),
#         th.Property("points_total", th.IntegerType),
#         th.Property("_links", th.StringType)
#     ).to_dict()

#     def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
#         """Return a context dictionary for child streams."""
#         return {
#             "quiz_id": record["quiz"],
#             "statistic_id": record["id"]
#         }


# class QuizStatisticsQuestionsStream(LearnDashStream):
#     """Define custom stream."""
#     # Working but getting access error for certain quiz_ids
#     name = "quiz_statistics_questions"
#     path = "/sfwd-quiz/{quiz_id}/statistics/{statistic_id}"
#     primary_keys = ["quiz_id", "statistic_id", "id"]
#     parent_stream_type = QuizStatisticsStream
#     ignore_parent_replication_keys = True
#     schema = th.PropertiesList(
#         th.Property("quiz_id", th.IntegerType),
#         th.Property("statistic_id", th.IntegerType),
#         th.Property("id", th.IntegerType),
#         th.Property("statistic", th.IntegerType),
#         th.Property("quiz", th.IntegerType),
#         th.Property("question", th.IntegerType),
#         th.Property("question_type", th.StringType),
#         th.Property("points_scored", th.IntegerType),
#         th.Property("points_total", th.IntegerType),
#         th.Property("answers", th.ArrayType(th.StringType)),
#         th.Property("student", th.ArrayType(th.StringType)),
#         th.Property("_links", th.StringType)
#     ).to_dict()


class TopicStream(LearnDashStream):
    """Define custom stream."""
    name = "topic"
    path = "/sfwd-topic"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("date", th.DateTimeType),
        th.Property("date_gmt", th.DateTimeType),
        th.Property("guid", th.StringType),
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
        th.Property("ld_topic_category", th.ArrayType(th.StringType)),
        th.Property("ld_topic_tag", th.ArrayType(th.StringType)),
        th.Property("materials_enabled", th.BooleanType),
        th.Property("materials", th.StringType),
        th.Property("video_enabled", th.BooleanType),
        th.Property("video_url", th.StringType),
        th.Property("video_shown", th.StringType),
        th.Property("video_auto_complete", th.BooleanType),
        th.Property("video_auto_complete_delay", th.IntegerType),
        th.Property("video_show_complete_button", th.BooleanType),
        th.Property("video_auto_start", th.BooleanType),
        th.Property("video_show_controls", th.BooleanType),
        th.Property("video_focus_pause", th.BooleanType),
        th.Property("video_resume", th.BooleanType),
        th.Property("assignment_upload_enabled", th.BooleanType),
        th.Property("assignment_points_enabled", th.BooleanType),
        th.Property("assignment_points_amount", th.IntegerType),
        th.Property("assignment_auto_approve", th.BooleanType),
        th.Property("assignment_deletion_enabled", th.BooleanType),
        th.Property("forced_timer_enabled", th.BooleanType),
        th.Property("forced_timer_amount", th.IntegerType),
        th.Property("course", th.IntegerType),
        th.Property("lesson", th.IntegerType),
        th.Property("assignment_upload_limit_extensions", th.StringType),
        th.Property("assignment_upload_limit_size", th.StringType),
        th.Property("assignment_upload_limit_count", th.IntegerType),
        th.Property("_links", th.StringType)
    ).to_dict()


class UserCourseProgressStream(LearnDashStream):
    """Define custom stream."""
    name = "user_course_progress"
    path = "/users/{user_id}/course-progress"
    primary_keys = ["user_id", "course"]
    parent_stream_type = CoursesUsersStream
    ignore_parent_replication_keys = True
    schema = th.PropertiesList(
        th.Property("user_id", th.IntegerType),
        th.Property("course", th.IntegerType),
        th.Property("last_step", th.IntegerType),
        th.Property("steps_total", th.IntegerType),
        th.Property("steps_completed", th.IntegerType),
        th.Property("progress_status", th.StringType),
        th.Property("date_started", th.DateTimeType),
        th.Property("date_completed", th.DateTimeType),
        th.Property("_links", th.StringType)
    ).to_dict()

    def post_process(self, row: dict, context: Optional[dict] = None) -> dict:
        """As needed, append or transform raw data to match expected structure.
        Optional. This method gives developers an opportunity to "clean up" the results
        prior to returning records to the downstream tap - for instance: cleaning,
        renaming, or appending properties to the raw record result returned from the
        API.
        """
        row["user_id"] = context["user_id"]
        return row

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "user_id": record["user_id"],
            "course_id": record["course"]
        }


class UserCourseProgressStepsStream(LearnDashStream):
    """Define custom stream."""
    name = "user_course_progress_steps"
    path = "/users/{user_id}/course-progress/{course_id}/steps"
    primary_keys = ["user_id", "course_id", "step"]
    parent_stream_type = UserCourseProgressStream
    ignore_parent_replication_keys = True
    schema = th.PropertiesList(
        th.Property("user_id", th.IntegerType),
        th.Property("course_id", th.IntegerType),
        th.Property("step", th.IntegerType),
        th.Property("post_type", th.StringType),
        th.Property("date_started", th.DateTimeType),
        th.Property("date_completed", th.DateTimeType),
        th.Property("step_status", th.StringType)
    ).to_dict()

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        # TODO: Parse response body and return a set of records.
        resp_json = response.json()
        for row in resp_json[0]:
            yield row

    def post_process(self, row: dict, context: Optional[dict] = None) -> dict:
        """As needed, append or transform raw data to match expected structure.
        Optional. This method gives developers an opportunity to "clean up" the results
        prior to returning records to the downstream tap - for instance: cleaning,
        renaming, or appending properties to the raw record result returned from the
        API.
        """
        row["user_id"] = context["user_id"]
        row["course_id"] = context["course_id"]
        return row


class UserCoursesStream(LearnDashStream):
    """Define custom stream."""
    name = "user_courses"
    path = "/users/{user_id}/courses"
    primary_keys = ["user_id", "id"]
    parent_stream_type = CoursesUsersStream
    ignore_parent_replication_keys = True
    schema = th.PropertiesList(
        th.Property("user_id", th.IntegerType),
        th.Property("id", th.IntegerType),
        th.Property("date", th.DateTimeType),
        th.Property("date_gmt", th.DateTimeType),
        th.Property("guid", th.StringType),
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
        th.Property("ld_course_category", th.ArrayType(th.StringType)),
        th.Property("ld_course_tag", th.ArrayType(th.StringType)),
        th.Property("_links", th.StringType)
    ).to_dict()

    def post_process(self, row: dict, context: Optional[dict] = None) -> dict:
        """As needed, append or transform raw data to match expected structure.
        Optional. This method gives developers an opportunity to "clean up" the results
        prior to returning records to the downstream tap - for instance: cleaning,
        renaming, or appending properties to the raw record result returned from the
        API.
        """
        row["user_id"] = context["user_id"]
        return row


class UserGroupsStream(LearnDashStream):
    """Define custom stream."""
    # At the moment this stream returns empty so I have no good idea what to add on the properties list
    name = "user_groups"
    path = "/users/{user_id}/groups"
    primary_keys = ["user_id", "id"]
    parent_stream_type = CoursesUsersStream
    ignore_parent_replication_keys = True
    schema = th.PropertiesList(
        th.Property("user_id", th.IntegerType)
    ).to_dict()


class UserQuizProgressStream(LearnDashStream):
    """Define custom stream."""
    # At the moment this stream returns empty so I have no good idea what to add on the properties list
    name = "user_quiz_progress"
    path = "/users/{user_id}/quiz-progress"
    primary_keys = ["user_id", "id"]
    parent_stream_type = CoursesUsersStream
    ignore_parent_replication_keys = True
    schema = th.PropertiesList(
        th.Property("user_id", th.IntegerType)
    ).to_dict()
