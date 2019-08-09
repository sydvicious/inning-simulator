# inning-simulator

This inning simulator takes lines of text as input. The lines contain a set of comma-separated
strings indicating various events, and this simulator will track the events and the results of
those events.

The various play types:

* out - batter is out; all other runners advance one base unless this is the final out.
* k - batter is out; all other runners don't advance
* 1b - all runners advance one base; batter advances to first
* 2b - all runners advance two bases; batter advances to second
* 3b - all runners advance three bases (score); batter advances to third
* hr - all runners and batters score; bases left empty
* e - all runners advance one base; better advances to first
* bb - batter advances to first; all runners advance if forced
* hpb - batter advances to first; all runners advance if forced

You can also input blank lines, and lines leading with "#" for comments, to make test files
easier to write.

Output for each input line shall consist of the string:

    "Bases: xxx, Outs: n, Runs: m"
    
where each x is a "0" for base empty, and a "1" for base occupied, and the order is 3rd base,
2nd base, and first base; n is the number of outs after the event, and m is the number of
runs scored during the event.

Sample:

1b,2b,2b -> Bases: 010, Outs: 0, Runs: 2

# System requirements

Both the script and the unit tests will run with straight python 2.7 or 3.4 with
no additional packages are required.

# Invocation

From a command-line with python installed, run:

```shell script
./inning-simulator [files]
```

or:

```shell script
python inning-simulator [files]
```

If no files are given, the script reads lines from standard input. Otherwise, the script reads
each argument as a file, and outputs the results.

# Unit tests

To invoke the unit tests, run:

```shell script
./test_inning_simulator.py
```

or:

```shell script
python test_inning_simulator.py
```

I have also included a text file, tests.txt, which list every possible base/out state.
This does not test correctness, but it does run through every possible scenario. The unit
tests test all of the logic.

To run with this test file, type:

```shell script
./inning-simulator tests.txt
```

or

```shell script
pythong inning-simulator tests.txt
```