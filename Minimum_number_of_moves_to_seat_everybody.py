class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        t_moves = 0
        for i in range(len(seats)):
            t_moves += abs(seats[i] - students[i])
        return t_moves
