"""Generate 20 synthetic Wonder Chocolates survey responses.
@author: Claude
"""
import csv
import random
import sys

random.seed(42)
OUT = sys.argv[1]

Q7 = ["taste", "ingredient_quality", "price_value", "variety", "packaging",
      "availability", "freshness", "healthier_options", "ethical_sourcing",
      "customer_service"]
Q11 = ["milk_bars", "dark_bars", "white", "truffles", "gift_boxes", "nuts_fruit",
       "seasonal", "reduced_sugar", "vegan", "single_origin", "baking", "drinks"]
Q12 = ["more_dark", "reduced_sugar_line", "vegan_line", "functional",
       "bold_flavors", "smaller_packs", "single_origin", "custom_gift_boxes",
       "subscription", "fair_trade"]
Q17 = ["taste", "price_value", "variety", "healthier", "ethical",
       "packaging_gift", "availability", "promotions"]
COMPARE = ["Much worse", "Somewhat worse", "About the same",
           "Somewhat better", "Much better", "Don't know"]

COLUMNS = (
    ["respondent_id", "submitted_at", "q1_last_purchase", "q2_chocolate_frequency",
     "q3_purchase_change", "q4_reasons_less", "q4_other", "q5_channels",
     "q5_other", "q6_occasions"]
    + [f"q7_{a}" for a in Q7]
    + ["q8_quality_change", "q9_value_change", "q10_nps"]
    + [f"q11_any_{c}" for c in Q11] + [f"q11_wonder_{c}" for c in Q11]
    + [f"q12_{o}" for o in Q12]
    + ["q13_wish_product", "q14_too_cheap", "q14_bargain", "q14_getting_expensive",
       "q14_too_expensive", "q15_competitors", "q15_other", "q16_most_often",
       "q17_brand"]
    + [f"q17_{a}" for a in Q17]
    + ["q18_main_reason", "q19_purchase_intent", "q20_one_change", "q21_age",
       "q22_city", "q23_state", "q24_zip", "q25_comments"]
)

# Hand-written profiles. mood: -1 unhappy, 0 neutral, 1 happy.
# stop_after: last section completed for partial responses (None = complete).
P = [
    dict(q1="In the past month", q2="Weekly or more", q3="About the same", mood=1,
         q4=[], q15=["CocoaCraft"], q16="Wonder Chocolates", age="35-44",
         city="Seattle", state="WA", zip="98103",
         q13="A dark chocolate bar with espresso nibs",
         q20="Honestly nothing, maybe more loyalty rewards.",
         q25="Love the sea salt caramel bar. Best in town!"),
    dict(q1="1-6 months ago", q2="2-3 times a month", q3="Somewhat less", mood=-1,
         q4=["Price went up / too expensive", "Smaller portion or package size"],
         q15=["SweetBar Co.", "Store brand / private label"], q16="SweetBar Co.",
         q18="Lower price", age="25-34",
         city="Portland", state="Oregon", zip="97214",
         q13="", q20="Bring back the old bar size. The new one is a ripoff.",
         q25="The price keeps going up and the bars keep getting smaller. Not cool."),
    dict(q1="7-12 months ago", q2="Monthly", q3="I have stopped buying Wonder Chocolates",
         mood=-1, q4=["Health or dietary reasons (sugar, allergens, vegan, etc.)",
                      "Switched to another brand"],
         q15=["PureLeaf Chocolate"], q16="PureLeaf Chocolate", q18="Healthier options",
         age="45-54", city="austin", state="tx", zip="78704",
         q13="Something vegan that actually tastes good",
         q20="Offer a low sugar or vegan line.",
         q25="I used to love Wonder but my doctor told me to cut sugar."),
    dict(q1="In the past month", q2="Weekly or more", q3="Somewhat more", mood=1,
         q4=[], q15=["Maison Truffe"], q16="Wonder Chocolates", age="55-64",
         city="Boston", state="MA", zip="2134",  # leading zero dropped
         q13="Custom gift boxes for corporate clients",
         q20="Faster shipping during the holidays",
         q25="Great gifts. My clients always rave about the truffles."),
    dict(q1="1-6 months ago", q2="Monthly", q3="Much less", mood=-1,
         q4=["Quality or taste got worse", "Products I like were discontinued"],
         q15=["CocoaCraft", "Maison Truffe"], q16="CocoaCraft", q18="Better taste",
         age="35-44", city="San Fransisco", state="CA", zip="94110",
         q13="The raspberry dark bar you discontinued!",
         q20="Bring back the raspberry dark bar and fix the recipe.",
         q25="The chocolate tastes waxy now. Did you change suppliers?"),
    dict(q1="13-24 months ago", q2="A few times a year", q3="I have stopped buying Wonder Chocolates",
         mood=-1, q4=["Hard to find in stores I visit"],
         q15=["Store brand / private label"], q16="Store brand / private label",
         q18="Easier to find", age="65+",
         city="Des Moines", state="IA", zip="50309-2210",
         q13="", q20="Sell it at Hy-Vee again.",
         q25="My grocery store stopped carrying it. Haven't seen it anywhere."),
    dict(q1="In the past month", q2="2-3 times a month", q3="About the same", mood=0,
         q4=[], q15=["SweetBar Co."], q16="Wonder Chocolates", age="18-24",
         city="Chicago", state="Illinois", zip="60614",
         q13="Matcha white chocolate",
         q20="Student discounts", q25="Pretty good, a little pricey for a student."),
    dict(q1="1-6 months ago", q2="Monthly", q3="Somewhat less", mood=0,
         q4=["Not enough new flavors or variety"],
         q15=["CocoaCraft", "PureLeaf Chocolate"], q16="CocoaCraft",
         q18="More variety / new flavors", age="25-34",
         city="Denver", state="CO", zip="8O205",  # letter O instead of zero
         q13="Chili and cinnamon dark chocolate",
         q20="New flavors more than once a year.",
         q25="It's fine but boring. Same five flavors forever."),
    dict(q1="In the past month", q2="Weekly or more", q3="Much more", mood=1,
         q4=[], q15=["None"], q16="", age="45-54",
         city="Atlanta", state="GA", zip="30309",
         q13="", q20="Keep doing what you're doing!",
         q25="Absolutely the best chocolate. My whole family is hooked."),
    dict(q1="7-12 months ago", q2="A few times a year", q3="Somewhat less", mood=-1,
         q4=["Online ordering or shipping problems", "Bad customer-service experience"],
         q15=["Maison Truffe"], q16="Maison Truffe", q18="Better for gifts",
         age="55-64", city="Phoenix", state="AZ", zip="85016",
         q13="", q20="Ship in insulated boxes so it doesn't melt.",
         q25="My order arrived melted and customer service never called back."),
    dict(q1="1-6 months ago", q2="2-3 times a month", q3="About the same", mood=0,
         q4=[], q15=["SweetBar Co.", "CocoaCraft"], q16="Wonder Chocolates",
         age="35-44", city="NY", state="New York City", zip="10027",  # swapped
         q13="Bigger family-size bags", q20="Bulk packs at Costco",
         q25="Good quality, nothing special about the packaging."),
    dict(q1="13-24 months ago", q2="Monthly", q3="Much less", mood=-1,
         q4=["Price went up / too expensive", "Switched to another brand"],
         q15=["SweetBar Co.", "Store brand / private label"],
         q16="Store brand / private label", q18="Lower price", age="Prefer not to say",
         city="Miami", state="FL", zip="33137",
         q13="", q20="Lower the prices. Period.",
         q25="Too expensive for what it is."),
    dict(q1="In the past month", q2="2-3 times a month", q3="Somewhat more", mood=1,
         q4=[], q15=["PureLeaf Chocolate"], q16="Wonder Chocolates", age="25-34",
         city="Minneapolis", state="MN", zip="55408",
         q13="Protein chocolate bar for after workouts",
         q20="A reduced-sugar dark bar", q25="Love the 85% dark. Keep it coming."),
    dict(q1="1-6 months ago", q2="A few times a year", q3="About the same", mood=0,
         q4=[], q15=["Maison Truffe", "CocoaCraft"], q16="Maison Truffe",
         q18="Better for gifts", age="65+",
         city="Nashvile", state="TN", zip="37203",
         q13="", q20="Prettier gift boxes",
         q25="Fine for myself, but I buy Maison Truffe for gifts."),
    dict(q1="7-12 months ago", q2="Monthly", q3="Somewhat less", mood=-1,
         q4=["Concerns about ethical sourcing or sustainability"],
         q15=["CocoaCraft", "PureLeaf Chocolate"], q16="PureLeaf Chocolate",
         q18="Stronger ethical / sustainability credentials", age="18-24",
         city="Burlington", state="VT", zip="",  # missing zip
         q13="Fair Trade certified bars",
         q20="Get Fair Trade certified and be transparent about cocoa farms.",
         q25="I want to know my chocolate wasn't made with child labor."),
    dict(q1="In the past month", q2="Weekly or more", q3="About the same", mood=1,
         q4=[], q15=["SweetBar Co."], q16="Wonder Chocolates", age="45-54",
         city="Columbus", state="OH", zip="90210",  # zip belongs to CA
         q13="Hot cocoa mix", q20="More seasonal flavors",
         q25="The holiday peppermint bark is amazing."),
    dict(q1="1-6 months ago", q2="2-3 times a month", q3="Much less", mood=-1,
         q4=["Eating less chocolate in general", "Price went up / too expensive"],
         q15=["Store brand / private label"], q16="Store brand / private label",
         q18="Lower price", age="35-44",
         city="Sacramento ", state="Calif.", zip="95818",
         q13="", q20="Smaller cheaper packs", q25="", stop_after=None),
    # Partial: quit after Section C
    dict(q1="In the past month", q2="Monthly", q3="Somewhat less", mood=0,
         q4=["Not enough new flavors or variety"], q15=[], q16="", age="",
         city="", state="", zip="", q13="", q20="", q25="", stop_after="C"),
    # Partial: quit after Section D, skipped to demographics? no: left blank
    dict(q1="7-12 months ago", q2="A few times a year", q3="About the same", mood=0,
         q4=[], q15=[], q16="", age="", city="", state="", zip="",
         q13="White chocolate with lemon", q20="", q25="", stop_after="D"),
    # Screened out at Q1
    dict(q1="More than 24 months ago", q2="", q3="", mood=0, q4=[], q15=[], q16="",
         age="", city="", state="", zip="", q13="", q20="", q25="", stop_after="A"),
]

CHANNELS = ["Grocery store / supermarket", "Specialty or gourmet shop",
            "Wonder Chocolates retail store", "Wonder Chocolates website",
            "Amazon or other online marketplace", "Convenience store / gas station",
            "Warehouse club (e.g., Costco)"]
OCCASIONS = ["Treat for myself", "Gift for someone else",
             "Holidays or special occasions", "Baking / cooking",
             "Sharing at work or at home"]
INTENT = ["Definitely will not", "Probably will not", "Might or might not",
          "Probably will", "Definitely will"]
CHANGE = ["Much worse", "Somewhat worse", "No change", "Somewhat better", "Much better"]


def likert(mood, spread=1):
    base = {-1: 2, 0: 3, 1: 4}[mood]
    return max(1, min(5, base + random.randint(-spread, spread)))


def row_for(i, p):
    r = {c: "" for c in COLUMNS}
    r["respondent_id"] = f"R{i:03d}"
    r["submitted_at"] = f"2026-10-{random.randint(1, 28):02d} {random.randint(8, 22):02d}:{random.randint(0, 59):02d}"
    r["q1_last_purchase"] = p["q1"]
    stop = p.get("stop_after")
    if stop == "A":
        return r
    mood = p["mood"]
    r["q2_chocolate_frequency"] = p["q2"]
    # Section B
    r["q3_purchase_change"] = p["q3"]
    r["q4_reasons_less"] = ";".join(p["q4"])
    r["q5_channels"] = ";".join(random.sample(CHANNELS, random.randint(1, 3)))
    r["q6_occasions"] = ";".join(random.sample(OCCASIONS, random.randint(1, 3)))
    # Section C
    for a in Q7:
        r[f"q7_{a}"] = "DK" if random.random() < 0.08 else likert(mood)
    if "Quality or taste got worse" in p["q4"]:
        r["q7_taste"] = r["q7_ingredient_quality"] = 1
    if "Price went up / too expensive" in p["q4"]:
        r["q7_price_value"] = random.choice([1, 2])
    r["q8_quality_change"] = CHANGE[likert(mood) - 1] if random.random() > 0.1 else "Don't know"
    r["q9_value_change"] = CHANGE[max(1, likert(mood) - 1) - 1]
    r["q10_nps"] = max(0, min(10, {-1: 3, 0: 7, 1: 9}[mood] + random.randint(-2, 1)))
    if stop == "C":
        return r
    # Section D
    for c in Q11:
        any_ = random.random() < 0.45
        r[f"q11_any_{c}"] = int(any_)
        r[f"q11_wonder_{c}"] = int(any_ and random.random() < (0.7 if mood > 0 else 0.35))
    for o in Q12:
        r[f"q12_{o}"] = random.randint(1, 5)
    if "Health" in ";".join(p["q4"]):
        r["q12_reduced_sugar_line"] = r["q12_vegan_line"] = 5
    if "ethical" in ";".join(p["q4"]):
        r["q12_fair_trade"] = 5
    r["q13_wish_product"] = p["q13"]
    cheap = random.choice([1, 1.5, 2])
    r["q14_too_cheap"] = cheap
    r["q14_bargain"] = cheap + random.choice([1, 1.5, 2])
    r["q14_getting_expensive"] = r["q14_bargain"] + random.choice([2, 3, 4])
    r["q14_too_expensive"] = r["q14_getting_expensive"] + random.choice([2, 3, 5])
    if stop == "D":
        return r
    # Section E
    r["q15_competitors"] = ";".join(p["q15"])
    if p["q15"] != ["None"]:
        r["q16_most_often"] = p["q16"]
        brand = p["q16"] if p["q16"] != "Wonder Chocolates" else p["q15"][0]
        r["q17_brand"] = brand
        for a in Q17:
            if random.random() < 0.07:
                r[f"q17_{a}"] = "Don't know"
            else:
                r[f"q17_{a}"] = COMPARE[max(0, min(4, 2 - mood + random.randint(-1, 1)))]
        r["q18_main_reason"] = p.get("q18", "")
    r["q19_purchase_intent"] = INTENT[max(0, min(4, mood + 2 + random.randint(-1, 0)))]
    if "stopped" in p["q3"]:
        r["q19_purchase_intent"] = random.choice(INTENT[:2])
    # Sections F, G
    r["q20_one_change"] = p["q20"]
    r["q21_age"] = p["age"]
    r["q22_city"], r["q23_state"], r["q24_zip"] = p["city"], p["state"], p["zip"]
    r["q25_comments"] = p["q25"]
    return r


with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=COLUMNS)
    w.writeheader()
    for i, p in enumerate(P, 1):
        w.writerow(row_for(i, p))
print(f"wrote {len(P)} rows, {len(COLUMNS)} columns to {OUT}")
