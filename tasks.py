"""
Invoke tasks
"""
from invoke import task


@task
def lint(ctx):
    """ check lint """
    ctx.run("pylint app")


@task
def types(ctx):
    """ check type """
    ctx.run("mypy app")


@task
def serve(ctx):
    """ start server """
    ctx.run("python manage.py runserver")


# @task
# def merge(ctx):
#     """ rebase against staging branch and merge if no conflicts occur """
#     ctx.run("git pull --rebase origin staging")
