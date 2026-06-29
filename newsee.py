 # ============================================================
# Google Play Store Analysis - Bubble Chart Project
# ============================================================

# ============================
# Step 1: Import Libraries
# ============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from zoneinfo import ZoneInfo


# ============================
# Step 2: Load Datasets
# ============================

play_store_data = pd.read_csv(
    r"C:\Users\Vansh Sharma\Downloads\Play Store Data (1).csv"
)

review = pd.read_csv(
    r"C:\Users\Vansh Sharma\Downloads\User Reviews (1).csv"
)


print("Datasets Loaded Successfully")



# ============================
# Step 3: Explore Dataset
# ============================

print("\nPlay Store Shape:", play_store_data.shape)
print("Reviews Shape:", review.shape)

print("\nPlay Store Info")
print(play_store_data.info())

print("\nReviews Info")
print(review.info())



# ============================
# Step 4: Clean Play Store Data
# ============================

play_store_data = play_store_data.drop_duplicates(
    subset="App"
)

play_store_data["Rating"] = pd.to_numeric(
    play_store_data["Rating"],
    errors="coerce"
)

play_store_data["Reviews"] = pd.to_numeric(
    play_store_data["Reviews"],
    errors="coerce"
)


play_store_data["Installs"] = (
    play_store_data["Installs"]
    .astype(str)
    .str.replace(",", "")
    .str.replace("+","")
)

play_store_data["Installs"] = pd.to_numeric(
    play_store_data["Installs"],
    errors="coerce"
)


play_store_data["Price"] = (
    play_store_data["Price"]
    .astype(str)
    .str.replace("$","")
)

play_store_data["Price"] = pd.to_numeric(
    play_store_data["Price"],
    errors="coerce"
)



# ============================
# Step 5: Convert Size into MB
# ============================

def convert_size(size):

    if pd.isna(size):
        return np.nan

    size = str(size)

    if size.endswith("M"):
        return float(size[:-1])

    elif size.endswith("k"):
        return float(size[:-1]) / 1024

    return np.nan



play_store_data["Size_MB"] = (
    play_store_data["Size"]
    .apply(convert_size)
)


play_store_data = play_store_data.dropna(
    subset=[
        "Rating",
        "Reviews",
        "Installs",
        "Size_MB"
    ]
)



# ============================
# Step 6: Clean Reviews Data
# ============================


review = review[
    [
        "App",
        "Sentiment_Subjectivity"
    ]
]


review["Sentiment_Subjectivity"] = pd.to_numeric(
    review["Sentiment_Subjectivity"],
    errors="coerce"
)


review = review.dropna(
    subset=["Sentiment_Subjectivity"]
)


review = (
    review
    .groupby("App",as_index=False)
    ["Sentiment_Subjectivity"]
    .mean()
)



# ============================
# Step 7: Merge Data
# ============================


merged_data = pd.merge(
    play_store_data,
    review,
    on="App",
    how="inner"
)


print(
    "\nMerged Dataset:",
    merged_data.shape
)



# ============================
# Step 8: Business Filters
# ============================


required_categories = [
    "GAME",
    "BEAUTY",
    "BUSINESS",
    "COMICS",
    "COMMUNICATION",
    "DATING",
    "ENTERTAINMENT",
    "SOCIAL",
    "EVENTS"
]


filtered_data = merged_data[
    (merged_data["Rating"] > 3.5) &
    (merged_data["Reviews"] > 500) &
    (merged_data["Installs"] > 50000) &
    (merged_data["Sentiment_Subjectivity"] > 0.5) &
    (~merged_data["App"]
     .str.contains("S",case=False,na=False)) &
    (merged_data["Category"]
     .isin(required_categories))
].copy()



print(
    "\nFiltered Dataset:",
    filtered_data.shape
)



# ============================
# Step 9: Translate Categories
# ============================


translation = {

    "BEAUTY":"सौंदर्य",
    "BUSINESS":"வணிகம்",
    "DATING":"Partnersuche"

}



filtered_data["Category_Display"] = (
    filtered_data["Category"]
    .map(lambda x: translation.get(x,x))
)



# ============================
# Step 10: IST Time Check
# ============================


current_time = datetime.now(
    ZoneInfo("Asia/Kolkata")
).time()


start_time = datetime.strptime(
    "17:00",
    "%H:%M"
).time()


end_time = datetime.strptime(
    "19:00",
    "%H:%M"
).time()



print(
    "\nCurrent IST Time:",
    current_time.strftime("%I:%M:%S %p")
)



# ============================
# Step 11: Bubble Chart
# ============================


if start_time <= current_time <= end_time:


    plt.figure(
        figsize=(15,8),
        dpi=120
    )


    colors = {

        "GAME":"pink",
        "सौंदर्य":"gold",
        "வணிகம்":"green",
        "COMICS":"orange",
        "COMMUNICATION":"blue",
        "Partnersuche":"red",
        "ENTERTAINMENT":"purple",
        "SOCIAL":"cyan",
        "EVENTS":"gray"

    }



    for category in filtered_data["Category_Display"].unique():

        temp = filtered_data[
            filtered_data["Category_Display"]
            == category
        ]


        plt.scatter(

            temp["Size_MB"],

            temp["Rating"],

            s=np.sqrt(
                temp["Installs"]
            ),

            c=colors.get(
                category,
                "black"
            ),

            alpha=0.6,

            edgecolor="black",

            label=category
        )



    plt.title(
        "Bubble Chart: App Size vs Rating",
        fontsize=16,
        fontweight="bold"
    )


    plt.xlabel(
        "App Size (MB)"
    )


    plt.ylabel(
        "Average Rating"
    )


    plt.grid(
        True,
        linestyle="--",
        alpha=0.5
    )


    plt.legend(
        title="Category",
        bbox_to_anchor=(1.02,1),
        loc="upper left"
    )


    plt.tight_layout()

    plt.show()



else:

    print(
        "Bubble chart available only between 5 PM and 7 PM IST"
    )



# ============================
# Step 12: Conclusion
# ============================


print(
"""
Project Completed Successfully.

The Bubble Chart shows:
- App Size vs Rating
- Bubble size = Installs
- Color = Category

All business rules applied.
"""
)


print(
    filtered_data["Category"].unique()
)