"""LearnDash tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_learndash.streams import (
    CoursesStream,
    CourseUsersStream,
    CoursePrerequisitesStream,
    CourseGroupsStream,
    AssignmentsStream,
    EssaysStream,
    GroupsStream,
    LessonsStream,
    QuestionsStream,
    QuizzesStream,
    TopicsStream,
    UserCourseProgressStream,
    UserCoursesStream,
    UserGroupsStream,
    UsersStream
)

STREAM_TYPES = [
    CoursesStream,
    CourseUsersStream,
    CoursePrerequisitesStream,
    CourseGroupsStream,
    AssignmentsStream,
    EssaysStream,
    GroupsStream,
    LessonsStream,
    QuestionsStream,
    QuizzesStream,
    TopicsStream,
    UserCourseProgressStream,
    UserCoursesStream,
    UserGroupsStream,
    UsersStream
]


class TapLearnDash(Tap):
    """LearnDash tap class."""
    name = "tap-learndash"

    config_jsonschema = th.PropertiesList(
        th.Property("username", th.StringType, required=True),
        th.Property("password", th.StringType, required=True),
        th.Property("api_url", th.StringType, required=True),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
