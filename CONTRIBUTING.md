# Contributing to MentorPaired

Thank you for indicating interest in contributing to MentorPaired. Following these guidelines help to communicate that you respect the time of the developers managing and working on this open source project. In return, they should reciprocate that respect in addressing your issue, assessing changes, and also helping you finalise your pull requests

### What do I do? How do I get started?

Follow the [README.md](/README.md) guide. If you've noticed a bug or have a question, [search the issue tracker](https://github.com/mentorpaired/core/issues) to see if someone else already created a ticket. If that has not been done yet, go ahead and [make one](https://github.com/mentorpaired/core/issues/new).

### Fork & create a branch

If this is something you think you can fix, [fork MentorPaired](https://help.github.com/en/articles/fork-a-repo) and create a branch with a descriptive name. Always checkout from the staging branch, that is the default and up-to-date branch.

A good branch name would be:

```sh
git checkout -b 90-fix-signup-page
```

### Implement your fix or feature

At this point, you're ready to make your changes. Feel free to ask for help; everyone was once a beginner.

The [requirements](/requirements.txt) file contain the packages and dependencies to be installed and set up. CI is set up, so the tests have to pass before your PR is reviewed and merged.

Please ensure that the issue you've fixed is related to the branch you're currently working from. If you want to fix something else unrelated to whatever you've worked on, do another checkout from the staging branch and give the new branch an appropriate name. This makes it easy for the maintainers to track your fixes.

### Keeping your Pull Request updated

Related to the above, if a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

### Merging a PR (for maintainers only)

A PR can only be merged into staging by a maintainer if:

* It is passing CI.
* It has no requested changes
* It is up-to-date with current staging branch

Any maintainer is allowed to merge a PR if all of these conditions are met.
