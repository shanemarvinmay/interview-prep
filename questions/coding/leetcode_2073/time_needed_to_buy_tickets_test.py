from time_needed_to_buy_tickets_solution import Solution

def test_time_required_to_buy():
    tickets = [2,3,2,3,2]
    solution = Solution()

    assert solution.timeRequiredToBuy(tickets, 2) == 8