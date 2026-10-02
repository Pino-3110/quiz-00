# Problem 00: AI Harm (10 points / 40 points)

Edit this file to solve problem 00. Problem 00 will not be auto-graded.

This question is most aligned to our first class, where we discussed motivations for this course along with the benefits and risks that modern AI methods are bringing to society.

## Problem 00 - Part A

Modern AI techniques stand to bring great benefits to society, but these benefits come with risks of causing harm to individuals, organizations, and societies. This is particularly true for deep learning algorithms, which are composed of several layers of linear and nonlinear processing. This makes deep learning algorithms exceptionally capable for detecting subtle patterns in data and making inferences therefrom, often achieving human-like or even super-human performance. However, the deep layers of linear and nonlinear processing which comprise deep learned algorithms also make it hard for those deploying them to ensure they behave as expected. Deep learning algorithms might learn the right results for the wrong reason, might appear to perform well initially and then degrade in performance when the input data drifts, and might have unintended biases towards producing particular results.

List five examples in recent years (2010 onward) where AI capabilities have causes harm to people, organizations, or society:

* Example 1: In 2020, Detroit police wrongfully arrested Robert Williams after a facial recognition system incorrectly matched his photo to a person suspected of stealing watches. This shows how an incorrect AI identification can contribute to an innocent person being arrested
* Example 2: Amazon developed an AI recruiting tool that learned from historical hiring data and was found to disadvantage women. This shows how biased patterns in training data can cause an AI system to give unfair results to qualified applicants.
* Example 3: A healthcare algorithm was found to be biased against black patients when identifying people who needed additional medical care. Because the system underestimated the needs of some patients, they could receive less medical attention than they deserved. This shows how bias in AI systems can negatively affect people's health.
* Example 4: In 2018, an Uber self-driving test vehicle was involved in a fatal crash after its automated driving system failed to properly recognize a pedestrian crossing the road. This shows how mistakes in an AI system's ability to recognize objects and make decisions can create serious safety risks.
* Example 5: In 2016, Microsoft's Tay chatbot produced inappropriate responses after interacting with users online. This showed that an AI system can learn undesirable patterns from user input if it does not have enough safeguards. It demonstrates the importance of controlling and monitoring the information an AI system learns from.

## Problem 00 - Part B

For one of the examples you chose, describe a best practice we have discussed so far that could have helped to prevent the negative outcomes. You do not need to know how to implement the best practice you reference in code here or guarantee that the best practice you would recommend would fix the problem completely.

One best practice that could have helped is double verification of a person's identity instead of relying only on facial recognition. If the facial recognition system gives a match, another method of verification could be used before taking action. This could help catch incorrect matches and reduce the chance of an innocent person being wrongly identified.

## Problem 00 - Part C

While the risks associated with AI are exacerbated by the prevalence of powerful deep architectures which started to gain popularity in the 2010s for image processing and in the 2020s for natural language processing, the risks of AI are not specific to deep neural networks. There are many other capabilities that would be considered AI by the Russell and Norvig definition that are not neural networks, and have been in use long before neural networks became popular.

List a time where an AI capability caused harm to an individual, organization, or society **before the year 2000**.

In 1987, computer-based program trading contributed to the stock market crash. Computers were programmed to automatically make trades when certain market conditions occurred and large amounts of automated trading contributed to the market problems during the crash.

Why does it make sense to describe this example as being caused by AI? Reference the Russell and Norvig definition of AI (*"AI agents are those which receive percepts from the environment and take actions"*).

This can be considered an AI capability because the computer system received information from the market and then took actions by automatically executing trades based on that information. This matches the Russell and Norvig definition of an AI agent because it receives percepts from its environment and takes actions.
