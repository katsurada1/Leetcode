# time: O(n * m)
# space: O(n)

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            local, domain = email.split('@')
            tmp = ""
            for char in local:
                if char == ".":
                    continue
                elif char == "+":
                    break
                else:
                    tmp += char
            result.add(tmp + "@" + domain)
        return len(result) 
