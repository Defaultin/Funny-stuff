"""
Given two arrays that represent the arrival and departure times of trains,
find the minimum number of platforms required so that no train waits.

Examples:
Input:
    arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00}
    dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
Explanation: There are at-most 3 trains at a time (time between 9:40 to 12:00).

Input:
    arr[] = {9:00, 9:40}
    dep[] = {9:10, 12:00}
Output: 1
Explanation: Only one platform is needed.
"""


def minimum_railway_platforms(arrival: list[int], departure: list[int]) -> int:
    platforms = max_platforms = 0
    events = sorted(
        [(time, "arrival") for time in arrival]
        + [(time, "departure") for time in departure],
        key=lambda x: x[0]
    )

    for _, event in events:
        if event == "arrival":
            platforms += 1
            max_platforms = max(max_platforms, platforms)
        else:
            platforms -= 1

    return max_platforms


if __name__ == "__main__":
    arrivals = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]
    result = minimum_railway_platforms(arrivals, departures)
    print(result)
