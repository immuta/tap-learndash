"""LearnDash tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_learndash.streams import (
    LearnDashStream,
    CoursesStream,
    CoursesUsersStream,
    CoursesPrerequisitesStream,
    CoursesGroupsStream,
    AssignmentsStream,
    EssaysStream,
    GroupsStream,
    LessonsStream,
    QuestionStream,
    QuizStream,
    # QuizStatisticsStream,
    # QuizStatisticsQuestionsStream,
    TopicStream,
    UserCourseProgressStream,
    UserCourseProgressStepsStream,
    UserCoursesStream,
    UserGroupsStream,
    UserQuizProgressStream
)
# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
# PriceTypeStream, ProgressStatusStream, QuestionTypeStream removed as data is reproduced in Courses, UserProgress and Question streams
# CoursesStepsStream removed as data returned is strange format (AL could not parse) and not critical
# QuizStatisticsStream and QuizStatisticsQuestionsStream have permissions issues
STREAM_TYPES = [
    CoursesStream,
    CoursesUsersStream,
    CoursesPrerequisitesStream,
    CoursesGroupsStream,
    AssignmentsStream,
    EssaysStream,
    GroupsStream,
    LessonsStream,
    QuestionStream,
    QuizStream,
    # QuizStatisticsStream,
    # QuizStatisticsQuestionsStream,
    TopicStream,
    UserCourseProgressStream,
    UserCourseProgressStepsStream,
    UserCoursesStream,
    UserGroupsStream,
    UserQuizProgressStream
]


class TapLearnDash(Tap):
    """LearnDash tap class."""
    name = "tap-learndash"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property("username", th.StringType, required=True),
        th.Property("password", th.StringType, required=True),
        th.Property("api_url", th.StringType, required=True),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
