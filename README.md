# "Game Of Greed" Group Assignment

## Group Members

- Amani Musallam
- Faisal Al-Hawajreh
- Raghad Abdulhadi
- Suhaib Hasan Ahmed

It's worth mentioning that Faisal still absent since March 14th lab n didn't respond to any communication attempts to contribute to the work since.

### Game Objective

Players try to score 10000 points to win by randomly rolling 6 dices.

### Points Calculation

1. In case of having a sequence of 1 to 6, the returned score is 1500.
2. In case of having any three pairs, the returned score is 1500.
3. In case of having several occurrences of a number, the returned score includes a value as follows...
    |       Value      | Occurrences |   Points  |
    | ---------------- | ----------- | --------- |
    |        1         |      3      |   1000    |
    |        1         |      4      |   2000    |
    |        1         |      5      |   3000    |
    |        1         |      6      |   4000    |
    | Any other Number |      3      | num X 100 |
    | Any other Number |      4      | num X 200 |
    | Any other Number |      5      | num X 300 |
    | Any other Number |      6      | num X 400 |
4. In case of having one or two 1s, the returned score includes 1 occurrences X 100 points.
5. In case of having serverl 5s, the returned score includes 5 occurrences X 50 points.

### Stage 1 Works

- Dice Rolling
- Score Calculation
- Banking the Scores

### Stage 2 Works

- Code an interactive cli-based game to deal with given interaction cases
