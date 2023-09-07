from jsonplaceholder_assignment.src.utilities.request_utilities import RequestsUtility


class CommentsUtilities(object):

    def __init__(self):
        self.requestUtility = RequestsUtility()

    def get_comments(self, postId):
        endpoint = '/posts/{}/comments'.format(postId)

        return self.requestUtility.get(endpoint)

    def post_comment(self, postId, data):
        endpoint = '/posts/{}/comments'.format(postId)

        return self.requestUtility.post(endpoint, data)
