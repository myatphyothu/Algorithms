
# the following algorithm has runtime complexity of O(n^2)
def longest_palindrome(s):

    def expand_from_middle(s, left, right):
        if s is None or left > right:
            return 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1

    start  = 0
    end = 0

    for i, c in enumerate(s):
        len_x = expand_from_middle(s, i, i)
        len_y = expand_from_middle(s, i, i + 1)
        len_z = max(len_x, len_y)
        if len_z > end - start:
            start = i - ((len_z - 1) // 2)
            end = i + (len_z // 2)

    return s[start:end + 1]


# Manacher's Algorithm
# runtime complexity O(n)
def manacher_longest_palindrome(s):
    # insert extract characters
    filler = '#'
    new_s = ''.join([filler] + [c + filler for c in s])

    n = len(new_s)
    p = [0] * n

    center = right = 0
    longest_length = 0
    longest_center = 0

    for i, c in enumerate(new_s):
        mirror = center - (i - center)
        if i < right:
            p[i] = min(p[mirror], right - i)

        end = i + (p[i] + 1)
        start = i - (p[i] + 1)

        while start >= 0 and end < n and new_s[start] == new_s[end]:
            end += 1
            start -= 1
            p[i] += 1

        if p[i] >= longest_length:
            longest_center = i
            longest_length = p[i]

        if i + p[i] > right:
            center = i
            right = i + p[i]


    return new_s[longest_center - longest_length : longest_center + longest_length].replace(filler, '')


if __name__ == '__main__':
    data = ['dabbae', 'racecar', 'bb']

    for s in data:
        # lp = longest_palindrome(s)
        lp = manacher_longest_palindrome(s)
        print(f'{s} ==> {lp}')



