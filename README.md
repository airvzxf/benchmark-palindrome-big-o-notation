# Benchmark: Palindrome algorithm and the Big(o)-notation.

Create the Palindrome algorithm with two version one which iterate all characters in the string and other which run the
half of the string. The goal is runs the benchmarks to see if the cost of the cpu performance and memory is the same as
O(n) vs O(n/2) when the size of the string is small and when is huge.



## Benchmark.

The first parameter is the number of characters, every benchmark which was ran, contains the alphabet (repeated n times)
then some space and then the reversed alphabet (repeated n times); the first one contains 53 characters then the second
has 52,001 characters that means there are 1,000 alphabet, one space and 1,000 reversed alphabet.

**Example:**

abc...xyz[space]zyx...cba


**Table of sizes:**

| Characters | = | No. of palindrome phrase |
| --- | --- | --- |
| 53 | = | 1 |
| 52,001 | = | 1,000 |
| 5,200,001 | = | 100,000 |
| 52,000,001 | = | 1,000,000 |
| 520,000,001 | = | 10,000,000 |
| 5,200,000,001 | = | 100,000,000 |



### Results:

53 Half is True: 0.000006<br>
53 Full is True: 0.000007

53 Half is True: 0.000005<br>
53 Full is True: 0.000007

53 Half is True: 0.000005<br>
53 Full is True: 0.000007

53 Half is True: 0.000005<br>
53 Full is True: 0.000007

53 Half is True: 0.000005<br>
53 Full is True: 0.000008

---

52001 Half is True: 0.002020<br>
52001 Full is True: 0.004069

52001 Half is True: 0.001856<br>
52001 Full is True: 0.003751

52001 Half is True: 0.004421<br>
52001 Full is True: 0.006802

52001 Half is True: 0.001960<br>
52001 Full is True: 0.003854

52001 Half is True: 0.001895<br>
52001 Full is True: 0.003887

---

5200001 Half is True: 0.196587<br>
5200001 Full is True: 0.379283

5200001 Half is True: 0.189253<br>
5200001 Full is True: 0.370748

5200001 Half is True: 0.191807<br>
5200001 Full is True: 0.371390

5200001 Half is True: 0.201436<br>
5200001 Full is True: 0.378666

5200001 Half is True: 0.191569<br>
5200001 Full is True: 0.372320

---

52000001 Half is True: 1.920629<br>
52000001 Full is True: 3.749065

52000001 Half is True: 1.970417<br>
52000001 Full is True: 3.691760

52000001 Half is True: 1.906109<br>
52000001 Full is True: 3.738383

52000001 Half is True: 1.927747<br>
52000001 Full is True: 3.755065

52000001 Half is True: 1.903009<br>
52000001 Full is True: 3.690557

---

520000001 Half is True: 19.401331<br>
520000001 Full is True: 38.161828

520000001 Half is True: 19.302548<br>
520000001 Full is True: 37.110522

520000001 Half is True: 19.211547<br>
520000001 Full is True: 37.067184

520000001 Half is True: 19.366211<br>
520000001 Full is True: 37.851146

520000001 Half is True: 19.510006<br>
520000001 Full is True: 37.594283

---

5200000001 Half is True: 212.034519<br>
5200000001 Full is True: 424.296307

5200000001 Half is True: 208.479333<br>
5200000001 Full is True: 417.322248

5200000001 Half is True: 214.985591<br>
5200000001 Full is True: 428.589914

5200000001 Half is True: 211.458170<br>
5200000001 Full is True: 423.816508

5200000001 Half is True: 215.475284<br>
5200000001 Full is True: 424.831080



### Total time and usage.

I executed the command `time ./venv/bin/python __main__.py` that runs all the palindrome files from tiny to immense.

2nd round.<br>
real    7m47.762s<br>
user    11m29.988s<br>
sys     0m7.345s

3rd round.<br>
real    7m58.994s<br>
user    11m47.706s<br>
sys     0m7.073s

4th round.<br>
real    7m55.116s<br>
user    11m39.775s<br>
sys     0m7.178s

5th round.<br>
real    7m55.789s<br>
user    11m45.110s<br>
sys     0m7.219s
