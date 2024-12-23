"""
There are n gas stations along a circular route,
where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i]
of gas to travel from the ith station to its next (i + 1)th station.
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost,
return the starting gas station's index if you can travel around
the circuit once in the clockwise direction, otherwise return -1.

If there exists a solution, it is guaranteed to be unique.

Examples:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at index 0:
Travel to 1: gas = 1, cost = 3, tank = 0 + (1 - 3) = -2 (not enough gas)

Start at index 1:
Travel to 2: gas = 2, cost = 4, tank = 0 + (2 - 4) = -2 (not enough gas)

Start at index 2:
Travel to 3: gas = 3, cost = 5, tank = 0 + (3 - 5) = -2 (not enough gas)

Start at index 3:
Travel to 4: gas = 4, cost = 1, tank = 0 + (4 - 1) = 3
Travel to 0: gas = 5, cost = 2, tank = 3 + (5 - 2) = 6
Travel to 1: gas = 1, cost = 3, tank = 6 + (1 - 3) = 4
Travel to 2: gas = 2, cost = 4, tank = 4 + (2 - 4) = 2
Travel to 3: gas = 3, cost = 5, tank = 2 + (3 - 5) = 0 (enough gas)

Therefore, return 3 as the starting index.
"""


def gas_station(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    tank = start_station = 0
    for station in range(start_station, len(gas)):
        tank = tank + (gas[station] - cost[station])

        if tank < 0:
            tank = 0
            start_station = station + 1

    return start_station


if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(gas_station(gas, cost))
