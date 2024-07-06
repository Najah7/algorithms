# Dynamic Programming(DP)

## Definition
Dynamic Programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions. The next time the same subproblem occurs, instead of recomputing its solution, one simply looks up the previously computed solution, thereby saving computation time.

## key points
- Optimal Substructure: A problem has an optimal substructure if an optimal solution can be constructed from optimal solutions of its subproblems.
- Overlapping Subproblems: A problem has overlapping subproblems if it can be broken down into subproblems which are reused several times.

## Approaches
- **Memoization**: It's a top-down approach. It stores the results of expensive function calls and returns tfhe cached result when the same inputs occur again.
- **Tabulation**: It's a bottom-up approach. It stores the result of a subproblem in a table and uses it to find the solution of the bigger problem.

## Top-down vs Bottom-up

| | Top-down | Bottom-up |
| --- | --- | --- |
| Easyness | Easy to come up with solution as it is extension of divide and conquer | Hard to come up with solution|
| Runtime | Slow | Fast |
| Space | stack space require  | no stack space required |
| When to use | Need a quick solution | Need an efficient solution |

## Note
- Dynamic Programming is optimized Divide and Conquer.
