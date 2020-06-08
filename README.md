#CHALLENGE
A plain of flowers could be attacked by a parasite, which infects the flowers and causes them to fade (lose their
flowers). The Faded flowers are removed from the plain and new flowers are planted in their place. After a
while, these flowers could potentially become infected by the parasite.
The environment can be shaped using the following rules:
1. An infected area becomes Faded the following year.
2. A Faded area becomes Healthy the following year.
3. An infected area passes on the infection onto its neighbours to the North, South, East and West the
following year, if the latter are currently Healthy.
Write a computer program uses the rules above to simulate the changes in the plain of flowers over a number
of generations.
Input specification:
The state of the plain of flowers is represented by a grid of 25 letters. For example:
HHHHH
HHIHH
HHFFH
HHHHH
HHHHH
where H symbolises the healthy areas, I symbolises the infected areas and F symbolises the fading areas. The
initial state of the plain of flowers should be read from the keyboard or from a text file, together with the
number of generations for which the simulation will run.
Output specification:
A grid of 25 letters (as above) that reflects the state of the plain of flowers after the amount of generations you
have specified as input.
