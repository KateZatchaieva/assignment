from jsonplaceholder_assignment.src.utilities.comments_utilities import CommentsUtilities
from jsonplaceholder_assignment.src.utilities.posts_utilities import PostsUtilities


class BaseTest(object):
    post_utils = PostsUtilities()
    comments_utils = CommentsUtilities()