# Developer Collaboration Exercise

## Learning Objectives

  + Adopt and practice a Pull Request Workflow to:
    + Collaborate with yourself (on independent projects)
    + Collaborate with people you don't know (on open source projects)
    + Collaborate with teammates (on team projects)

## Instructions

Follow the instructions in each of the exercises below, to practice collaboration for three different use cases. For the second and third use case, we'll be using specific repos and wanting to make specific changes to those repos.

### Independent Projects

This is the process we will follow to add or revise the functionality of our own existing repos:

  1. Choose one of your existing GitHub repos, or create a new one (i.e. the "origin" repo).
  2. Clone the repo locally if you haven't already done so. Ensure your local main branch is up-to-date with the origin main branch.
  3. Checkout a new branch called something like "new-feature-123".
  4. Modify some trivial part of the codebase, save your work, and make a commit on the branch.
  5. Push the code to a remote branch in the origin repo.
  6. Create a Pull Request to prepare to merge the remote branch with the remote main branch.
  7. Review the changes via the Pull Request, and optionally make some comments.
  8. When you are satisfied with the changes, merge the Pull Request via the GitHub interface.

To repeat the process (after changes have been merged):

  9.  From the command-line, check-out the main branch, and pull the most recent changes from the origin main branch.
  10. Then repeat steps 3-8 above.


### Open Source Projects

This is the process we will follow to add or revise the functionality of repos we don't own or have write access to:

  1. Choose a repo owned by someone else, that you don't have direct write access to (i.e. the "upstream" repo). For this exercise we'll use this [example open source repo](https://github.com/prof-rossetti/example-open-source-repo-2021).
  2. Fork the upstream repo to create a copy under your own control (i.e. the "origin" repo).
  3. Clone the origin repo locally. Ensure your local main branch is up-to-date with the upstream and origin main branches.
  4. Checkout a new branch called something like "new-feature-123".
  5. Modify some trivial part of the codebase (for this exercise, the change we'll make is to add a new file in the app directory called "[USERNAME]_script.py", with some example print statements inside it), then save your work, and make a commit on the branch. Be aware that conflicts may arise if editing the same file as someone else.
  6. Push the code to a remote branch in the origin repo.
  7. Create a Pull Request to prepare to merge the remote origin branch with the upstream main branch.
  8. Wait until a maintainer of the upstream repo takes further action - eventually hopefully merging your code.

To repeat the process (after changes have been merged):

  9. From the command-line, check-out the main branch, and pull the most recent changes from the upstream main branch. Then push those changes to the origin main branch, to ensure it is up-to-date with the upstream main branch.
  10. Then repeat steps 4-8 above.

### Team Projects

This is the process we will follow to add or revise the functionality of shared repos we may or may not be the owner of, but which we have write access to:

  1. Choose an existing shared GitHub repo, or create a new one and share it with friends (i.e. the "origin" repo). For this exercise we'll use this [example shared repo](https://github.com/prof-rossetti/our-shared-repo-2021) that the professor has invited you to collaborate on.
  2. Clone the repo locally if you haven't already done so. Ensure your local main branch is up-to-date with the origin main branch.
  3. Checkout a new branch called something like "[USERNAME]-new-feature-123". We include the username in the branch name so our branch names will stay unique and not conflict with other people's branches.
  4. Modify some trivial part of the codebase (for this exercise, the change we'll make is to add a new file in the app directory called "[USERNAME]_script.py", with some example print statements inside it), then save your work, and make a commit on the branch. Be aware that conflicts may arise if editing the same file as someone else.
  5. Push the code to a remote branch in the origin repo.
  6. Create a Pull Request to prepare to merge the remote branch with the remote main branch.
  7. Ask a repo collaborator for a Code Review.
  8. Wait until a collaborator takes further action - reviewing your code and eventually hopefully merging your code.

To repeat the process (after changes have been merged):

  9.  From the command-line, check-out the main branch, and pull the most recent changes from the origin main branch.
  10. Then repeat steps 3-8 above.
