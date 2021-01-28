import logging
import sys

from app import github_oauth, gitlab_oauth
from app.views import (
    github_oauth as gh_auth,
    gitlab_oauth as gl_auth,
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

    github_oauth.generate_github_access_token()
    gitlab_oauth.generate_gitlab_access_token()
    gh_auth.github_authenticate()
    gl_auth.gitlab_authenticate()
    request.RequestDetail()
    requests_interests.MentorRequestInterest()
    requests_interests.RequestInterestDetail()
    user.UserDetail()


if __name__ == "__main__":
    main()
