# Hidden Markov Models
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

According to tradition, algae can be leveraged to weather prediction.  If we hang them outside in a rain-protected area, the algae tends to absorb moisture. We could therefore observe the the condition of the algae, which could be:
- Soggy (0)
- Damp (1)
- Dryish (2)
- Dry (3)

and the real weather condidtions could be :
- Sunny Day (0)
- Cloudy Day (1)
- Rainy Day (2)

Let's say that we want to forecast the weather from the condition of algae. Observing for four continous days the algae, it is turned out that are [Soggy(day 1), Damp (day 2), Drush (day 3) and Dry (today)]. Given that we have no information about the real weather conditions, which is the most probable sequence of weather until today?

Hidden Markow Models and Viterbi algorithm could give the answer.

The initial probabilities are (π) :

| __Sun__ | __Cloud__ | __Rain__ |
|-------------|------------|------------|
 0.6     | 0.25 | 0.25

Transition probabilits are (α) :

| | __Sun__ | __Cloud__ | __Rain__ |
|-------------|------------|------------|------------|
| __Sun__ | 0.5     | 0.25 | 0.25
| __Cloud__ | 0.375 | 0.125     | 0.25
| __Rain__ |   0.125     | 0.675 | 0.375

and emission probabilities (b) are given by 

| | __Dry__ | __Dryish__ | __Damp__ | __Soggy__ |
|-------------|------------|------------|------------|------------|
| __Sun__ | 0.6     | 0.2 | 0.15 | 0.05
| __Cloud__ | 0.25 | 0.25   | 0.25 | 0.25
| __Rain__ |   0.05     | 0.1 | 0.35 | 0.5

Observable and hidden states are depicted in the following graph.

![image](https://user-images.githubusercontent.com/25617530/70395600-e149eb80-1a08-11ea-8659-815189140dbc.png)



## Viterbi algorihtm
The Viterbi algorithm is a dynamic programming algorithm for finding the most likely sequence of hidden states—called the Viterbi path—that results in a sequence of observed events, especially in the context of Markov information sources and hidden Markov models (HMM).

The algorithm has found universal application in decoding the convolutional codes used in both CDMA and GSM digital cellular, dial-up modems, satellite, deep-space communications, and 802.11 wireless LANs. It is now also commonly used in speech recognition, speech synthesis, diarization, keyword spotting, computational linguistics, and bioinformatics. For example, in speech-to-text (speech recognition), the acoustic signal is treated as the observed sequence of events, and a string of text is considered to be the "hidden cause" of the acoustic signal. The Viterbi algorithm finds the most likely string of text given the acoustic signal.

More information [Wikipedia](https://en.wikipedia.org/wiki/Viterbi_algorithm).

