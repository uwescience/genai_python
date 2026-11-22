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

2. Running example
   1. Description of the survey manager
      1. Survey authoring
      2. Survey taking
      3. Survey analysis
   2. ``Dash`` overview
   3. A simple ``Dash`` application
   4. HTML
   5. ``callbacks``
   6. Information model. These are the functions in storage. (See docs/data-model.md.) This is the main abstraction that is shared between the human and the AI.
      1. Survey
      2. Question
      3. Response
   7. (A1) Adding a simple feature
      1. Get a "hover" on the Survey Maker by assigning a value to ``title``
      2. Keep it current by adding an ``Output`` to ``refresh_survey_lists`` (the app must keep exactly five callbacks)

3. AI assisted code review
   1. Review of LLM basics
      1. Prompts, tokens, context
      2. Set up in VSCode
      3. ``git`` best practices (e.g., separate branch; use diff)
   2. Coding task - Check for duplicate survey taker ID
      1. Where in code this is done
      2. How the system responds (run it: submit the same ID twice)

4. AI-Assisted implementation of unit tests
   1. What is a test?
   2. Writing manual tests.
   3. Write tests for ``assemble_questions_from_state`` (pure function, no Dash or files needed), then for ``storage.py`` using the ``tmp_storage`` fixture
   4. Considerations for tests: coverage, not "brittle", robust (not "flakey"), computationally efficient
   5. Test generation
   6. Reviewing/modifying tests
   7. When to modify tests and when to re-generate tests.

5. Assisted small feature implementation
   1. Scope: function/method or small refactor
   2. Example: Check if a response duplicates an existing ID (fixing the findings from episode 3), then delete a survey with confirmation (``dcc.ConfirmDialog``)
      1. Alternative: show the Options field only for ``checkbox`` question rows
   3. Use case 1: Complete a partial implementation
      1. Implementation may have comments in sections and errors in others.
   4. Use case 2: AI creates from scratch
      1. Write function doc
      2. AI implementation
      3. Review and iterate
      4. AI writes tests
      5. Review tests

6. Assists for large feature: Part 1
   1. Scope: Add a hover for Survey Analyzer that summarizes the responses
   2. Example: Show what a hover looks like
   3. Write specification
      1. What's required for a hover: (a) ID for "tipped" widget; (b) tooltip widget
      2. Processing to create summary statistics
   4. Review for: completeness, ambiguities, consistency

7. Assists for large features: Part 2
   1. Write a plan and review
   2. Execute each step of the plan.
   3. Uses of specifications: documentation, refactoring, sustainability

8. Using the specification
   1. Documentation
   2. Refactoring
   3. Sustainability

9.  Course review
   1. Summary
   2. What's next: Skills, Agents
