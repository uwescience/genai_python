# AI-Assisted Python Programming: Course Outline

This document provides brief descriptions of the content of episodes (a teaching session lasting about 1 hour). Each numbered bullet is an episode.  

1. Course introduction and old school software engineering
   1. Course learning objectives.
   2. AI/ML background
      1. History
      2. Key concepts in neural networks
      3. Capabilities and limitations of LLMs
      4. AI ethics
   3. Old school software engineering
      1. Agile programming: specify, implement/test, evaluate
      2. Documentation: overall spec, module, function/method
      3. Design
      4. Tests

2. Running Example and AI Warmup
   1. Overview of "Wonder Chocolates"
   2. Review of LLM basics: prompts, tokens, contexxt
   3. "Vibe" design from Google forms.
      1. Discuss what's present and what's not
   4. Review an existing survey
      1. Ask AI to crtique @customer_survey.md
   5. Summary of insights
   6. Summary

3. AI Code Review and AI Pair Programming
   1. Setup
      1. Set up in VSCode
      2. ``git`` best practices (e.g., separate branch; use diff)
   2. Problem addressed: data cleansing
      1. Display survey results and issues with city, state, zipcode
   3. Coding task
      1. Complete partial implementation
      2. AI code review
      3. AI improvements

4. AI-Assisted implementation of unit tests
   1. What is a test?
   2. Writing manual tests.
   3. Tests for data cleansing
      1. Examples of cases
   4. Considerations for tests: coverage, not "brittle", robust (not "flakey"), computationally efficient
   5. Test generation
   6. Reviewing/modifying tests
   7. When to modify tests and when to re-generate tests.

5. Assisted small feature implementation
   1. Scope: function/method or small refactor
   2. Problem: Two level DataFrame: (a) question, (b) count of each response and none
   3. Write a python application that takes as arguments the input and output file and provides status update on progress
   4. Have AI review your implementation
   5. AI writes tests

6. Assists for large feature: Part 1
   1. Scope: Sentiment analysis of customer comments with colorized plot of trend by state in the US
   2. Application: point to directory of survey results
   3. Write specification
      1. What we want
      2. Requirements in terms of dependencies
   4. Review for: completeness, ambiguities, consistency

7. Assists for large features: Part 2
   1. Write a plan and review
   2. Execute each step of the plan.
   3. Uses of specifications: documentation, refactoring, sustainability

8. Using the specification
   1. Documentation
   2. Refactoring
   3. Sustainability

9. Course review
   1. Summary
   2. What's next: Skills, Agents
