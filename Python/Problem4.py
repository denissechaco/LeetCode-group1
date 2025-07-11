class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        # Dictionary to store results we've already calculated
        memo = {}

        # This function returns True if text[i:] matches pattern[j:]
        def match(i, j):
            # If we already solved this subproblem, return the result
            if (i, j) in memo:
                return memo[(i, j)]

            # If we reached the end of the pattern
            if j == len(pattern):
                # It's a match only if we also reached the end of the text
                result = i == len(text)

            else:
                #Check if the current characters match:
                #  They match if they are the same or if the pattern has '.', which matches any character
                first_match = (
                    i < len(text)
                    and (text[i] == pattern[j] or pattern[j] == '.')
                )

                # If the next character in the pattern is '*'
                if (j + 1) < len(pattern) and pattern[j + 1] == '*':
                    # Two options:
                    # 1. Skip this part of the pattern (x*) — move j by 2
                    # 2. If first characters match, try to match more of the text — move i by 1
                    result = match(i, j + 2) or (first_match and match(i + 1, j))
                else:
                    # If there is no '*', continue matching next characters
                    result = first_match and match(i + 1, j + 1)

            # Save the result so we don’t repeat the same work
            memo[(i, j)] = result
            return result

        # Start the matching process from the beginning of both strings
        return match(0, 0)
