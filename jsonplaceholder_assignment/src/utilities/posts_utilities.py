from jsonplaceholder_assignment.src.utilities.request_utilities import RequestsUtility


class PostsUtilities(object):

    def __init__(self):
        self.requestUtility = RequestsUtility()

    def get_posts(self):
        endpoint = '/posts'

        return self.requestUtility.get(endpoint)
