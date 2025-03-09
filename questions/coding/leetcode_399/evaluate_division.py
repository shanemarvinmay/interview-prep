from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        vars = dict() # {var: val}
        
        for i, [numerator, denominator] in enumerate(equations):
            coef = values[i]
            if numerator not in vars and denominator not in vars:
                vars[denominator] = 1
                vars[numerator] = vars[denominator] * coef
            elif numerator not in vars:
                vars[numerator] = vars[denominator] * coef
            elif denominator not in vars:
                vars[denominator] = vars[numerator] / coef
        
        res = []
        for numerator, denominator in queries:
            if numerator not in vars or denominator not in vars:
                res.append(-1)
            else:
                res.append(vars[numerator] / vars[denominator])
        
        return res