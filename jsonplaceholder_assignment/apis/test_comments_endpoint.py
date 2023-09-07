import json
import logging as logger
import random
from jsonplaceholder_assignment.apis.base_test import BaseTest
from jsonplaceholder_assignment.src.helpers.generators import generate_random_comment


class TestCommentsEndpoint(BaseTest):
    def test_get_2nd_comment_for_3rd_post(self):
        logger.info("TEST: getting the 3rd post and verifying its 2nd comment is correct")

        post_const = 3

        logger.info("getting all comments for 3rd post")
        all_comments_of_3rd_post = self.comments_utils.get_comments(post_const)

        logger.info("getting the second comment of 3rd post")
        comments_number = len(all_comments_of_3rd_post.json())
        assert comments_number >= 2
        second_comment = all_comments_of_3rd_post.json()[1]
        logger.info("2nd comment is {}".format(second_comment))

        logger.info("verifying second comment is correct")
        assert all_comments_of_3rd_post.status_code == 200
        assert second_comment['name'] == 'modi ut eos dolores illum nam dolor'
        assert second_comment['email'] == 'Oswald.Vandervort@leanne.org'
        assert second_comment[
                   'body'] == 'expedita maiores dignissimos facilis\nipsum est rem est fugit velit sequi\neum odio dolores dolor totam\noccaecati ratione eius rem velit'

    def test_adding_new_comment_to_the_post(self):
        logger.info("TEST: Adding new comment to a post ")

        logger.info("getting id of random post")
        all_posts = self.post_utils.get_posts()
        posts_id_list = list(map(lambda x: x['id'], all_posts.json()))
        logger.info("id list is {}".format(posts_id_list))
        post_id = random.choice(posts_id_list)
        logger.info("post id is {}".format(post_id))

        logger.info("getting all comments for a post")
        all_comments_of_a_post = self.comments_utils.get_comments(post_id)
        comments_number = len(all_comments_of_a_post.json())
        logger.info("number of comments is {}".format(comments_number))

        logger.info("adding a comment for 3rd post")
        new_comment = json.dumps(generate_random_comment())
        logger.info("random comment is {}".format(new_comment))
        resp_add_comment = self.comments_utils.post_comment(post_id, new_comment)
        assert resp_add_comment.status_code == 201

        logger.info("verify new comment is in the list of all comments 3rd post")
        all_comments_of_3rd_post = self.comments_utils.get_comments(post_id)
        new_comments_number = len(all_comments_of_3rd_post.json())
        assert new_comments_number == comments_number + 1
        new_comment_id = resp_add_comment.json()['id']
        comments_id_list = list(map(lambda x: x['id'], all_comments_of_3rd_post.json()))
        logger.info("id list is {}".format(comments_id_list))
        assert new_comment_id in comments_id_list

        logger.info("verify new comment is correct")
        assert new_comment['name'] == resp_add_comment.json()['name']
        assert new_comment['email'] == resp_add_comment.json()['email']
        assert new_comment['body'] == resp_add_comment.json()['body']
