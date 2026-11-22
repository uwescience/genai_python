# Generative AI For Python Programmers

This repository contains materials for a course for self-taught Python programmers to use AI assists in a manner to provides consistent, well-engineered results. The core princile is that humans are in control. This is achieved by:

1. Testable implementation. Humans have ways to test that their intent has been implemented.
2. Comprehensible implementation. Code is implemented so that humans can read it and understand where and how features are implemented.

The specific skills taught are:

1. Code understanding
2. Code review
3. Test construction and implementation
4. Implementing (and co-implementing) small features
5. Specification-driven implementation of large features

## Pedagogy

The course uses a running example to provide a context for the foregoing. The context is analyzing survey results from Google Forms for a hypothetical wholesaler of chocolates called "Wonder Chocolates".

## Exercise 1: Survey Design

The first problem is survey design. The compony serves several thousand retailer stores in North America, and is seeing substantial changes in purchasing patterns. They want to know: (a) why is this happening; (b) what chocolate offerings have larger demands; and (c) how this compares with competitive offerings that their customers are considering.

The students will do the following:

1. "Vibe code" a survey by having Google Forms construct a draft. Part of this exercise is converting the Google Forms output to Mark Down.
2. Critique the result, and construct your own survey
3. "AI" review of the revised survey.

## Exercise 2: Data Cleansing

This is a programming exercise. The problem addressed is that responses can be non-standardized and/or contain typographical errors.

1. zip code validity checks
2. City, State (fill in blank)
3. Incomplete survey: summarize as dict: response: number of occurrences with a response of None

## Exercise 3: Finding Trends

This programming exercise looks at trends over time and geography using colorized maps. The following choices are considered:

1. Total volume of product purchased.
2. Volume of products by product line.

The analysis considers data over 5 years, estimating a line to the data with a measure of uncertainty.

## Exercise 4: Sentiment Analysis

Use Vader to do sentiment analysis for "Other comments" part of survey. Relate to product trends. Plot the results on a map.

