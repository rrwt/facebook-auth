import hashlib
import json

import requests
from allauth.socialaccount.models import SocialAccount


def profile_picture(user):
    """
    Get profile picture from user profile (graph api)
    :param user: user object
    :return: profile picture address url string
    """
    fb_uid = SocialAccount.objects.filter(user_id=user.id, provider='facebook')

    if len(fb_uid):
        json_response = requests.get('http://graph.facebook.com/v3.3/{}/picture?'
                                     'redirect=0&width=100&height=100'.format(fb_uid[0].uid))
        return json.loads(json_response.content)['data']['url']

    return 'http://www.gravatar.com/avatar/{}?s=40'\
        .format(hashlib.md5(user.email.encode('utf-8')).hexdigest())
