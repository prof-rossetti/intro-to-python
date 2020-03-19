# "Codebase Cleanup" Exercise

> Prerequisites:
>  + [Software Maintenance and Quality Control](/units/unit-8.md), including all linked notes
>  + ["Code Simplification" Exercise](https://github.com/prof-rossetti/code-simplification-exercise-py/)
>  + ["Testing, 1,2,3" Exercise](/exercises/testing-123/README.md)
>  + ["CI, 1,2,3" Exercise](/exercises/ci-123/README.md)

## Learning Objectives

  + Practice simplifying and refactoring code to improve readability and quality and decrease maintenance costs.
  + Practice writing and executing automated tests to verify your program behaves as expected, and incorporating automated testing into your development workflow.
  + Practice incorporating GitHub Pull Requests into your development workflow.
  + Practice running automated tests on a Continuous Integration server, and incorporating CI checks into your development workflow.

## Instructions

Revisit your previous projects and tackle their respective "testing challenges":

  + [Shopping Cart Project - Testing Challenges](/projects/shopping-cart/testing.md)
  + [Robo Advisor Project - Testing Challenges](/projects/robo-advisor/testing.md)

Start developing on a new branch called something like "cleanup" or "qc", and incorporate [Git Branch operations](/notes/clis/git.md#branch-operations) and GitHub Pull Requests and code self-reviews into your development workflow. Optionally ask a friend to review your PR and make a comment, or add them as a collaborator on your repository and they'll be able to conduct an official "review".

Optionally also configure your application's tests to run on a platform like Travis CI, and incorporate Continuous Integration (CI) into your workflow (BONUS).

## Examples

See the following examples of fully-tested projects:

  + [Shopping Cart Tests](https://github.com/s2t2/shopping-cart-screencast/tree/testing)
  + [Robo Advisor Tests](https://github.com/s2t2/robo-advisor-screencast/tree/v3-testing)

## Evaluation

Category | Description | Weight
--- | --- | ---
Pull Request Workflow | At least one or two Pull Requests used during development | 20%
Simplification | Previous code has been simplified or organized in at least a few minor ways | 20%
Documentation | Most if not all functions are documented via "docstring" comments | 20%
Automated Testing | Presence of at least a few tests which directly invoke functions from the source code to verify the program behaves as expected | 30%
Continuous Integration | Presence of tests being run on a CI server at least once, ideally integrated into the PR workflow | 10%
