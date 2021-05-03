import logging
import sys

from app import github_oauth, gitlab_oauth
from app.views import (
    github_oauth as gh_auth,
    gitlab_oauth as gl_auth,
    goal,
    request,
    requests_interests,
    user,
)


def main():
    logging.basicConfig(
        stream=sys.stdout,
        format="%(asctime)s - %(message)s",
        datefmt="%d/%m/%Y %H:%M%S",
        level=logging.INFO,
    )
    """
    Methods and functions where log statements are written are organized here
    for easier reference.
        :param generate_github_access_token: Github's access token used to read
        the Github user's information.
        :param generate_gitlab_access_token: Gitlab's access token used to read
        the Gitlab user's information.
        :param github_authenticate: Github login flow that authenticates and adds
        the user to our database.
        :param gitlab_authenticate: Gitlab login flow that authenticates and adds
        the user to our database.
        :param RequestDetail: Checks if a request object exists for read, update or delete
        operations.
        :param MentorRequestInterest: Checks if an interest object exists for a particular
        request.
        :param RequestInterestDetail: Checks if an interest object exists for update or delete
        operations.
        :param UserDetail: Checks if a user object exists for read, update or delete operations.
    """

    github_oauth.generate_github_access_token()
    gitlab_oauth.generate_gitlab_access_token()
    gh_auth.github_authenticate()
    gl_auth.gitlab_authenticate()
    goal.RetrieveUserGoal()
    request.RequestDetail()
    requests_interests.MentorRequestInterest()
    requests_interests.RequestInterestDetail()
    user.UserDetail()


if __name__ == "__main__":
    main()
