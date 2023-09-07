import logging as logger
import string
import random

def generate_random_comment(name_length=None, email_length=None, body_length=None):
    logger.debug("Generating random comment data")

    if not name_length:
        random_name_length = 10
    if not email_length:
        random_email_length = 10
    if not body_length:
        random_body_length = 10

    random_name_string = ''.join(random.choices(string.ascii_lowercase, k=random_name_length))
    random_email_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_length))
    random_body_string = ''.join(random.choices(string.ascii_lowercase, k=random_body_length))

    email = random_email_string + '@mailinator.com'

    random_comment = {'name': random_name_string, 'email': email, 'body': random_body_string}

    return random_comment

def generate_random_post(userId, title_length=None, body_length=None):
    logger.debug("Generating random comment data")

    if not title_length:
        random_title_length = 10
    if not body_length:
        random_body_length = 10

    random_title_string = ''.join(random.choices(string.ascii_lowercase, k=random_title_length))
    random_body_string = ''.join(random.choices(string.ascii_lowercase, k=random_body_length))

    random_post = {'userId': userId, 'title': random_title_string, 'body': random_body_string}

    return random_post