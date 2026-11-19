import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = pd.read_csv("data/compas-scores-two-years.csv")
    sns.set_theme(style="whitegrid")


    plt.figure(figsize=(11, 7))
    sns.boxplot(data=df, x="race", y="decile_score")
    plt.title("COMPAS Risk Score in Different Racial Groups")
    plt.xlabel("Race")
    plt.ylabel("COMPAS Decile Score")
    plt.savefig("visualizations/risk_scores_by_race.png")
    plt.close()

    recidiv = df.groupby("race")["two_year_recid"].mean()

    plt.figure(figsize=(11, 7))
    recidiv.sort_values().plot(kind="bar")
    plt.title("2 years of Recidivism Rate")
    plt.xlabel("race")
    plt.ylabel("Two Year Proportion")
    plt.savefig("visualizations/recidivism_by_race.png")
    plt.close()

    age = df.groupby("age_cat")["two_year_recid"].mean()

    plt.figure(figsize=(10, 9))
    age.plot(kind="bar")
    plt.title("2 year recidivisim by age")
    plt.xlabel("Age")
    plt.ylabel("Age Propotion")
    plt.savefig("visualizations/recidivism_by_age.png")
    plt.close()


    print("\nMissing values are:")
    print(df.isna().sum().sum())

    print("\nRecidivism by age: ")
    print((df.groupby("age_cat")["two_year_recid"].mean() * 100).round(2))


    print("\nRecidivism by race: ")
    print((df.groupby("race")["two_year_recid"].mean() * 100).round(2))

    print("\nMean score by race: ")
    print((df.groupby("race")["decile_score"].mean().round(2)))

if __name__ == "__main__":
    main()



