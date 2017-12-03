# BloomFilter
I considered the false positive probability to be 1.0E-6 so that it is as low as possible. Using the formula m = ceil((n * log(p)) / log(1.0 / (pow(2.0, log(2.0))))), I got n= 12110731 and k = 20. And got the following results:
Number of members in the set: 421167
Number of bits in the filter array: 12110731
Number of has functions used: 20.0
Number of items in the stream: 3148023
SpamCount: 2726852
False poisitve count: 421171
Percentage of false positives: 13.378904792
False Positive probability: 1.00004967703e-06

To decrease the number of hash functions, I tried a different probability value of 0.0004 and it gave m value of 6752403 and k = 11.0
Number of members in the set: 421167
Number of bits in the filter array: 6752403
Number of has functions used: 11.0
Number of items in the stream: 3148023
SpamCount: 2725620
False poisitve count: 422403
Percentage of false positives: 13.4180404654
False Positive probability: 0.000451621479239

So depending on the false probability needed, optimal k and n value can be chosen. According to the
testing, I found k=20 and n= 12110731 as optimal as they gave me the lowest false probability of 1.0E-6
and false positive percentage as 13.37% which is the lowest.
