Created by Daniel Tyler

This work is free to use and distribute under the terms listed under the GNU general license.

A simple implementation of a genetic algorithm to solve the traveling salesman problem.
Technically this isn't a complete implementation of the traditional genetic algorithm as an offspring of two permutations simply joins the total population, rather than replacing it's parents.
Therefor this does not constantly produce a new "best result" as a parent can be the current best result with none of it, or other's children being the new "best".

Also currently every member of the population is bred with every other member creating n^2 members which are all then evaluated for their fitness wherein the top n (technically sqrt(unique(n^2))) are kept.
Therefor it is possible for the population to stagnate due to possibly better genes being phased out because they were present in the culled portion of the population.