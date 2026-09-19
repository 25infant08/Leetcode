class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite) 
        fav_counter = [0] * n 
        for f in favorite:
            fav_counter[f] += 1
        root_employees = deque(emp for emp, fav_count in enumerate(fav_counter) if fav_count == 0)
        chain_lengths = [1] * n
        while root_employees: 
            root_emp = root_employees.popleft() 
            root_fav = favorite[root_emp]
            chain_lengths[root_fav] = chain_lengths[root_emp] + 1 
            fav_counter[root_fav] -= 1 
            if fav_counter[root_fav] == 0:
                root_employees.append(root_fav)
        max_cycle = 0 
        sum_groups = 0 
        for start_emp, fav_count in enumerate(fav_counter):
            if fav_count == 0: continue 
            fav_counter[start_emp] = 0 
            cycle_len = 1
            cur_emp = favorite[start_emp]
            while cur_emp != start_emp: 
                fav_counter[cur_emp] = 0  
                cycle_len += 1
                cur_emp = favorite[cur_emp]
            if cycle_len == 2: 
                sum_groups += chain_lengths[start_emp] + chain_lengths[favorite[start_emp]]
            else: 
                max_cycle = max(max_cycle, cycle_len)
        return max(max_cycle, sum_groups) 