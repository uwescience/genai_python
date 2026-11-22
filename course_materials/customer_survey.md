# Wonder Chocolate Customer Survey

## Purpose (for instructors)

Wonder Chocolates has seen **declining sales**. This survey is meant to answer three questions:

| Goal | Business question | Survey sections |
|------|-------------------|-----------------|
| (a) | Why are sales declining? | B, C, F |
| (b) | Which chocolate offerings are in higher demand? | D |
| (c) | How does Wonder compare with the competitors customers are considering? | E |

Design notes:

- **Target time:** about 8–10 minutes, 25 questions.
- **Who takes it:** current and lapsed Wonder customers (anyone who bought in the last 24 months).
- **Order:** screening and behavior questions come first, before opinion questions, so earlier questions don't bias the answers. Demographics come last.
- **Scales:** 5-point scales with labels on every point. Each one has a "Don't know / N/A" option where it makes sense.
- **Location fields** (Q22–Q24) are free text on purpose, so the data has realistic quality problems for the data-cleansing module.
- **Open-ended comments** (Q13, Q20, Q25) are the input for the sentiment-analysis module.

---

## Introduction (shown to respondents)

> Thank you for taking part in this survey from Wonder Chocolates. It takes about 10 minutes. Your answers are confidential and will be used only to improve our products and service. There are no right or wrong answers.

---

## Section A — Screening

**Q1.** When did you last buy Wonder Chocolates products?
- [ ] In the past month
- [ ] 1–6 months ago
- [ ] 7–12 months ago
- [ ] 13–24 months ago
- [ ] More than 24 months ago → *end survey*
- [ ] Never → *end survey*

**Q2.** How often do you buy chocolate of any brand?
- [ ] Weekly or more
- [ ] 2–3 times a month
- [ ] Monthly
- [ ] A few times a year
- [ ] Once a year or less

---

## Section B — Purchase Behavior *(Goal a)*

**Q3.** Compared with a year ago, how much Wonder Chocolates do you buy now?
- [ ] Much more
- [ ] Somewhat more
- [ ] About the same → *skip to Q5*
- [ ] Somewhat less
- [ ] Much less
- [ ] I have stopped buying Wonder Chocolates

**Q4.** *(If less or stopped)* What are the main reasons you buy less Wonder Chocolates? *(Select up to 3)*
- [ ] Price went up / too expensive
- [ ] Quality or taste got worse
- [ ] Smaller portion or package size
- [ ] Hard to find in stores I visit
- [ ] Online ordering or shipping problems
- [ ] Switched to another brand
- [ ] Products I like were discontinued
- [ ] Not enough new flavors or variety
- [ ] Health or dietary reasons (sugar, allergens, vegan, etc.)
- [ ] Concerns about ethical sourcing or sustainability
- [ ] Eating less chocolate in general
- [ ] Bad customer-service experience
- [ ] Other (please specify): ________

**Q5.** Where do you usually buy Wonder Chocolates? *(Select all that apply)*
- [ ] Grocery store / supermarket
- [ ] Specialty or gourmet shop
- [ ] Wonder Chocolates retail store
- [ ] Wonder Chocolates website
- [ ] Amazon or other online marketplace
- [ ] Convenience store / gas station
- [ ] Warehouse club (e.g., Costco)
- [ ] Other: ________

**Q6.** Why do you usually buy Wonder Chocolates? *(Select all that apply)*
- [ ] Treat for myself
- [ ] Gift for someone else
- [ ] Holidays or special occasions
- [ ] Baking / cooking
- [ ] Sharing at work or at home
- [ ] Other: ________

---

## Section C — Satisfaction with Wonder Chocolates *(Goal a)*

**Q7.** How satisfied are you with Wonder Chocolates on each of the following?

| Attribute | Very dissatisfied (1) | Dissatisfied (2) | Neutral (3) | Satisfied (4) | Very satisfied (5) | Don't know |
|---|---|---|---|---|---|---|
| Taste | | | | | | |
| Ingredient quality | | | | | | |
| Price / value for money | | | | | | |
| Variety of flavors | | | | | | |
| Packaging | | | | | | |
| Easy to find / buy | | | | | | |
| Freshness | | | | | | |
| Healthier options (low sugar, vegan, etc.) | | | | | | |
| Ethical / sustainable sourcing | | | | | | |
| Customer service | | | | | | |

**Q8.** Has the quality of Wonder Chocolates changed over the past year?
- [ ] Much better
- [ ] Somewhat better
- [ ] No change
- [ ] Somewhat worse
- [ ] Much worse
- [ ] Don't know

**Q9.** Has the value for money of Wonder Chocolates changed over the past year?
- [ ] Much better
- [ ] Somewhat better
- [ ] No change
- [ ] Somewhat worse
- [ ] Much worse
- [ ] Don't know

**Q10.** How likely are you to recommend Wonder Chocolates to a friend or colleague? *(0 = Not at all likely, 10 = Extremely likely)*

0 — 1 — 2 — 3 — 4 — 5 — 6 — 7 — 8 — 9 — 10

---

## Section D — Product Demand *(Goal b)*

**Q11.** In the past 6 months, which types of chocolate have you bought from any brand? Which ones did you buy from Wonder Chocolates?

| Product type | Bought (any brand) | Bought from Wonder |
|---|---|---|
| Milk chocolate bars | [ ] | [ ] |
| Dark chocolate bars (70%+) | [ ] | [ ] |
| White chocolate | [ ] | [ ] |
| Filled chocolates / truffles | [ ] | [ ] |
| Gift boxes / assortments | [ ] | [ ] |
| Chocolate with nuts or fruit | [ ] | [ ] |
| Seasonal / holiday items | [ ] | [ ] |
| Sugar-free or reduced-sugar | [ ] | [ ] |
| Vegan / dairy-free | [ ] | [ ] |
| Single-origin / craft bean-to-bar | [ ] | [ ] |
| Baking chocolate / cocoa | [ ] | [ ] |
| Chocolate drinks | [ ] | [ ] |

**Q12.** How interested would you be in buying each of these from Wonder Chocolates if they were offered?

| Offering | Not at all (1) | Slightly (2) | Moderately (3) | Very (4) | Extremely (5) |
|---|---|---|---|---|---|
| More dark / high-cacao options | | | | | |
| Reduced-sugar line | | | | | |
| Vegan / dairy-free line | | | | | |
| Protein or functional chocolate | | | | | |
| Bold or unusual flavors (e.g., chili, sea salt, matcha) | | | | | |
| Smaller, lower-priced packs | | | | | |
| Premium single-origin bars | | | | | |
| Personalized / custom gift boxes | | | | | |
| Subscription box | | | | | |
| Fair Trade / certified-sustainable range | | | | | |

**Q13.** *(Open-ended)* Is there a chocolate product you wish Wonder Chocolates made but doesn't?

________________________________________

**Q14.** For a typical 3.5 oz (100 g) premium chocolate bar, at what price would you consider it…
- …too cheap to trust the quality? $____
- …a bargain? $____
- …getting expensive, but you would still consider it? $____
- …too expensive to consider? $____

*(Instructor note: these four questions are the Van Westendorp price-sensitivity method.)*

---

## Section E — Competitive Comparison *(Goal c)*

**Q15.** Besides Wonder Chocolates, which chocolate brands have you bought or considered in the past 6 months? *(Select all that apply)*

*(Instructor note: these are fictional brands, each representing a market segment. Replace them as needed.)*
- [ ] **CocoaCraft** — premium craft / bean-to-bar
- [ ] **SweetBar Co.** — mass-market, low price
- [ ] **PureLeaf Chocolate** — healthy / vegan / low-sugar
- [ ] **Maison Truffe** — luxury gift chocolatier
- [ ] **Store brand / private label**
- [ ] Other: ________
- [ ] None → *skip to Section F*

**Q16.** Which **one** of these brands do you buy most often now?
- [ ] Wonder Chocolates
- [ ] *(answers from Q15 are shown here)*

**Q17.** Compared with Wonder Chocolates, how does **[brand from Q16, or the first competitor chosen in Q15]** rate on each of the following?

| Attribute | Much worse | Somewhat worse | About the same | Somewhat better | Much better | Don't know |
|---|---|---|---|---|---|---|
| Taste | | | | | | |
| Price / value | | | | | | |
| Variety | | | | | | |
| Healthier options | | | | | | |
| Ethical sourcing | | | | | | |
| Packaging / gift appeal | | | | | | |
| Easy to find / buy | | | | | | |
| Promotions / discounts | | | | | | |

**Q18.** *(If they buy a competitor more than Wonder)* What is the **main** reason you choose that brand instead of Wonder Chocolates?
- [ ] Lower price
- [ ] Better taste
- [ ] Healthier options
- [ ] More variety / new flavors
- [ ] Easier to find
- [ ] Better promotions
- [ ] Stronger ethical / sustainability credentials
- [ ] Better for gifts
- [ ] Other: ________

**Q19.** How likely are you to buy Wonder Chocolates in the next 3 months?
- [ ] Definitely will
- [ ] Probably will
- [ ] Might or might not
- [ ] Probably will not
- [ ] Definitely will not

---

## Section F — Open Feedback *(Goal a)*

**Q20.** *(Open-ended)* What is the **one thing** Wonder Chocolates could change that would make you buy more?

________________________________________

---

## Section G — About You

**Q21.** What is your age?
- [ ] Under 18 → *end survey*
- [ ] 18–24
- [ ] 25–34
- [ ] 35–44
- [ ] 45–54
- [ ] 55–64
- [ ] 65+
- [ ] Prefer not to say

**Q22.** City: ________

**Q23.** State: ________

**Q24.** ZIP code: ________

**Q25.** *(Optional, open-ended)* Any other comments about Wonder Chocolates?

________________________________________

---

## Closing (shown to respondents)

> Thank you for your time! Your feedback helps Wonder Chocolates make better chocolate.

---

## Instructor Appendix — Suggested Analysis

- **Goal (a), why sales are declining:** count how often each Q4 reason is chosen. Check which Q7 attributes predict Q3 (buying less) and Q10 (NPS). Look at trends in Q8 and Q9. Run themes and sentiment on Q20 and Q25.
- **Goal (b), what's in demand:** compare purchases in Q11 to find categories where customers buy from other brands but not from Wonder. Rank the Q12 interest scores using the top-2-box share (answers of 4 or 5). Use Q14 to find an acceptable price range.
- **Goal (c), competition:** use Q15 to see which competitors customers also consider. Average the Q17 ratings for each competitor to see where Wonder is stronger or weaker. Use Q18 to see why customers switch.
- **Segments to compare:** lapsed vs. current customers (Q1), age (Q21), region (Q23), and buying occasion (Q6).

### Critique prompts for the "vibe design" exercise
1. Does any question lead respondents toward an answer, or ask about two things at once?
2. Is the survey too long? Which questions would you cut first?
3. Could the order of questions bias the answers (e.g., Section C before Section E)?
4. What is missing? (e.g., household income, dietary restrictions, how respondents heard about Wonder)
5. Is free-text location a good choice in a real survey? What would you do instead?
