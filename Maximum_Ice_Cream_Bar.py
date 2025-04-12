class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        min_cost = min(costs)
        max_cost = max(costs)
        range_of_elements = max_cost - min_cost + 1
        
        count = [0] * range_of_elements
        
        for cost in costs:
            count[cost - min_cost] += 1
        
        sorted_costs = []
        for i in range(range_of_elements):
            sorted_costs.extend([i + min_cost] * count[i])
        
        total_cost = 0
        num_ice_creams = 0
        for cost in sorted_costs:
            total_cost += cost
            if total_cost > coins:
                break
            num_ice_creams += 1
        
        return num_ice_creams
