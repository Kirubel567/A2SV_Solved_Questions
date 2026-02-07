class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = []
        counter = {}
        for i in range(len(cpdomains)): 
            count, domain = cpdomains[i].split(" ")
            domains = domain.split('.')  

            subDomain2 = domain
            mainDomain = domains[len(domains)-1]

            if len(domains) > 2: 
                subDomain1 = domains[len(domains)-2] + "." + domains[len(domains)-1]
                counter[subDomain1] = counter.get(subDomain1, 0) +int(count)

            #add them to the counter hashmain
            counter[mainDomain] = counter.get(mainDomain, 0)+ int(count)
            counter[subDomain2] = counter.get(subDomain2, 0) +int(count)

        for key in counter: 
            ans.append(str(counter[key])+" "+ key)
        return ans 


