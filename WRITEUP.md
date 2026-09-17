# HW0 writeup

**Name:** Oscar Reza Bautista
**Date:** 2026-09-10

Replace every placeholder below with your answer. Every number you give comes from a script in this repo; say which one.

## Part 1. Basic rating statistics

Code: `human_part1.py`. One or two sentences per answer, with the numbers.

**(a) How many ratings, users, and movies are there, and how are ratings distributed across 1–5 stars?**

There are 100,000 ratings, 943 users, and ratings are distributed: 6,110 (1 star), 
11,370 (2 stars), 27145 (3 stars), 34,174 (4 stars), and 21,201 (5 stars).

**(b) What is the median number of ratings per user, and how many users have 100 or more ratings?**

The median number of ratings per user is 65. 

**(c) Which 10 movies have the most ratings?**

The 10 movies with the most ratings are:

 Legends of the Fall (1994)

George of the Jungle (1997)

         Heavy Metal (1981)

          GoodFellas (1990)

           Breakdown (1997)

       Marvin's Room (1996)

               Evita (1996)

           GoldenEye (1995)

            In & Out (1997)

      Cable Guy, The (1996)

**(d) Among movies with at least 20 ratings, which 10 have the highest mean rating?**

The top 10 movies with the highest mean rating and at least 20 ratings are Jack (1996) with 4.49 mean rating and 112 ratings,
Everyone Says I Love You (1996) with 4.47 mean rating and 298 ratings, Cinema Paradiso (1988) with 4.47 mean rating and 118 ratings,
Matese Falcon The (1941) with 4.46 mean rating and 243 ratings, The Hounted World of Edward D Wood Jr (1995) with 4.45 mean rating
and 67 ratings, What's Eating Gilber Grape (1993) with 4.45 mean rating and 283 ratings, It Happened One Night (1934) with 4.39
mean rating and 209 ratings, Mighty Aphrodite (1995) with 4.39 mean rating and 267 ratings, Legends of the Fall (1994) with 4.36
mean rating and 583 ratings, and Clockwork Orange (1971) with 4.34 and 125 ratings.

**Anything you got stuck on (what you tried, where it broke), or "none":**

I hadn't work with pandas GroupBy in a while, so I spent some time going through the docs.

## Part 2. The best movie

Code: `human_part2.py`.

**My rule:**

The best movies should have between 65 and 148 total ratings to be considered. The best movies are then those with the highest average rating.

**One rule I considered and rejected, and why:** 

I considered doing some sort of weighted average, but it seemed to complicated and might risk making incorrect assumptions on the data.

**Top 10 under my rule:**
                                          title       rating

                                    Jack (1996)     4.491071

                         Cinema Paradiso (1988)     4.466102

Haunted World of Edward D. Wood Jr., The (1995)     4.447761

                     Clockwork Orange, A (1971)     4.344000

                              Annie Hall (1977)     4.333333

                      Pump Up the Volume (1990)     4.259542

                            My Fair Lady (1964)     4.210145

                               Notorious (1946)     4.200000

                                Ridicule (1996)     4.198529

               In the Name of the Father (1993)     4.196429

**Why my rule, in at most 150 words. Name one thing it gains and one thing it loses:**

This rule considers the median and 75th percentile for total ratings count. Filtering out the rest of the values helps eliminate movies with relatively too few or relatively too many ratings, such that those in the extremes do not skew the perception of how well it was rated. However, a problem with this approach is that those movies with extreme number of ratings will always be left out of the consideration. 

## Part 3. The most ___ movie

Code: `human_part3.py`.

**My adjective:** Romantic

**My definition** (one sentence, precise enough that a classmate could code it)**:** If a movie is labeled as romantic and is well rated, then it is a very romantic movie.

**One definition I considered and rejected, and why:** More romantic movies have higher ratings than less romantic movies. I rejected this definition because a movie from another genre might be well rated and have no relationship to the romantic genre.

**Top 5 under my definition:**

                   title  mean_rating

  Cinema Paradiso (1988)     4.466102

       Annie Hall (1977)     4.333333

     My Fair Lady (1964)     4.210145

        Notorious (1946)     4.200000

Somewhere in Time (1980)     4.102273

**What your definition captures, what it misses, and where "___-ness" lives in this data — the
genre labels, what the crowd did, or the words in the titles. At most 150 words:**

It captures how much people like a movie that is labelled as romantic, likely suggesting that if they chose to watch it with the intention of watching a very romantic movie and they liked it a lot, then the movie is actually romantic. A problem with this definition is that it assumes a rating to a given romantic movie defines how romantic the movie is, however, there might be people who liked a romantic movie because of reasons unrelated to the fact that it is from this genre.

## Part 4. Claude's answers

Claude answers the same three questions in `claude_answers_1_2_3.py`, without seeing your code
or your answers.

**Did its numbers for Part 1 match yours? If not, which, and what did you find?**

XXXX

## Part 5. Comparing the best movie

**Claude's rule:**

XXXX

**Read what Claude wrote about its rule. Does it anywhere admit the rule was a choice, and that a different rule was possible? Or does it give its answer as simply the answer? Quote the sentence that decides it:**

XXXX

**Your Part 2 top 10 and Claude's Part 2 top 10 — not the Part 1(d) lists. Where do they differ, and why?**

XXXX

**Better for what purpose? Name a situation where your rule is the right one and a situation where Claude's is. At most 150 words. You may conclude yours, its, or neither:**

XXXX

## Part 6. Comparing the most ___ movie

**Claude's definition:**

XXXX

**Is Claude's film in your top 5?**

XXXX

**What Claude's definition sees that yours does not, and the reverse. At most 150 words:**

XXXX

## Working with Claude

**What you asked Claude for during Parts 1–3** (debugging and installing only — say what you
got stuck on)**:**

XXXX

**Something Claude said that you could not verify, and why. Or "none," and how you checked:**

XXXX

**What you would do differently next time, in 3–5 sentences:**

XXXX

**Where did this assignment slow you down for a reason that was its fault, not yours? Point at
the step. Or "nowhere." One or two sentences:**

XXXX

**Hours spent:** XXXX

**Anyone who helped you, or "no one":** XXXX
