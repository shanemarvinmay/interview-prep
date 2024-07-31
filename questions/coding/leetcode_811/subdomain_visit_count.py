from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        output = []
        domain_count = dict()
        # Counting domains
        for cpdomain in cpdomains:
            # Getting count.
            num, domain = cpdomain.split(' ')
            num = int(num)
            # Adding count for full domain.
            if domain not in domain_count:
                domain_count[domain] = 0
            domain_count[domain] += num
            # Getting subdomains
            for i in range(len(domain)-1, -1, -1):
                if domain[i] != '.':
                    continue
                sub_domain = domain[i+1:]
                if sub_domain not in domain_count:
                    domain_count[sub_domain] = 0
                domain_count[sub_domain] += num

        for domain, count in domain_count.items():
            output.append(f'{count} {domain}')
        
        return output
      