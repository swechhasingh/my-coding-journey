from typing import List


def can_attend_all_appointments(intervals:List[List[int]]):
    intervals.sort(key=lambda x: x[0])
    i, start, end = 0, 0, 1
    while i < (len(intervals)-1):
        if intervals[i][end] > intervals[i+1][start]:
            return False
        i += 1

    return True

def main():
    print("Can attend all appointments: " + 
            str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " + 
            str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " + 
            str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()
