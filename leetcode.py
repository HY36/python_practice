from collections import Counter
from functools import reduce, lru_cache
from operator import add, xor
from typing import Iterator
from math import sqrt, pow


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        union = set(J) & set(S)
        count_S = Counter(S)
        return sum([count_S[i] for i in union])

    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_dict = dict()
        for email in emails:
            email_local, email_domain = email.split("@")
            if email_domain not in email_dict:
                email_dict[email_domain] = [email_local]
            else:
                email_dict[email_domain].append(email_local)

        for key, value in email_dict.items():
            temp = []
            for local in value:
                local = local.split('+')[0].replace('.', '')
                temp.append(local)
            email_dict[key] = len(set(temp))
        return sum([i for i in email_dict.values()])

    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return [i for i in A if i % 2 == 0] + [i for i in A if i % 2 == 1]

    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        bool_dict = {True: 1, False: 0}
        return [[bool_dict[not i] for i in line[::-1]] for line in A]

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # return bin(x ^ y).count('1')
        return len([i for i in '{:b}'.format(x ^ y) if i == '1'])

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        init = [0, 0]
        for step in moves:
            if step == 'U':
                init[1] += 1
            elif step == 'D':
                init[1] -= 1
            elif step == 'R':
                init[0] += 1
            else:
                init[0] -= 1
        result = True if init == [0, 0] else False
        return result

    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        words_morse = [''.join([morse_code[ord(i) - 97]
                                for i in word]) for word in words]
        return len(set(words_morse))

    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        negative = {'1': '0', '0': '1'}
        bin_num = '{:b}'.format(num)
        complement = ''.join([negative[i] for i in bin_num])
        return int(complement, 2)

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        dividing_numbers = []
        for i in range(left, right + 1):
            str_num = str(i)
            if '0' in str_num:
                continue
            result = {i % int(j) for j in str_num}
            if len(result) == 1 and 0 in result:
                dividing_numbers.append(i)
        return dividing_numbers

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_line = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        second_line = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        third_line = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        set_words = [set(i.lower()) for i in words]
        index_list = [i <= first_line or i <=
                      second_line or i <= third_line for i in set_words]
        return [words[index] for index, _ in enumerate(words) if index_list[index]]

    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = reduce(add, zip([i for i in A if i %
                                  2 == 0], [i for i in A if i % 2 == 1]))
        return list(result)

    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mountain_map = {value: index for index, value in enumerate(A)}
        max_key = max(mountain_map.keys())
        return mountain_map[max_key]

    def canWinNim(self, n):
        """
        :type n: int
        :rtype
        """
        pass

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum([(ord(v) - 64) * (26 ** i) for i, v in enumerate(s[::-1])])

    def transpose(self, A: Iterator[Iterator[int]]):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        pass

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        for index, word in enumerate(s):
            s[index] = word[::-1]
        return ' '.join(s)

    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = dict()
        n_len = len(A) / 2
        for n in A:
            if n in count:
                count[n] += 1
                if count[n] == n_len:
                    return n
            else:
                count[n] = 1

    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        front = -1
        last = 0
        result = []
        for index, value in enumerate(S):
            if value == C:
                last = index
                if front == -1:
                    if last == 0:
                        result.append(0)
                    else:
                        result.extend(list(range(last + 1))[::-1])
                else:
                    for i in range(front + 1, last + 1):
                        result.append(min(i - front, last - i))
                front = index
            elif index + 1 == len(S):
                for i in range(last, index):
                    result.append(min(i - last + 1, index - i + 1))

        return result

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(xor, nums)

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        distance = {tuple(value): sqrt(pow(value[0], 2) + pow(value[1], 2)) for index, value in enumerate(points)}
        result = zip(distance.values(), distance.keys())
        result = sorted(result)
        return [i[1] for i in result[:K]]

    @lru_cache()
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        if len(num) == 1:
            return int(num)
        else:
            num = reduce(add, map(int, num))
            return self.addDigits(num)

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pass

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        words_length = []
        tmp = []
        for w in S:
            tmp.append(widths[ord(w) - 97])
            if sum(tmp[:-1]) + tmp[-1] > 100:
                words_length.append(tmp[:-1])
                del tmp[:-1]
            elif sum(tmp[:-1]) + tmp[-1] == 100:
                words_length.append(tmp[:])
                del tmp[:]
            else:
                pass
        last_length = sum(tmp) if tmp else sum(words_length[-1])
        line_length = len(words_length) if not tmp else len(words_length) + 1
        return line_length, last_length

    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = [i ** 2 for i in A]
        result.sort()
        return result

    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        pass

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return sum(nums[0::2])

    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = bin(n).replace('0b', '')
        for index, value in enumerate(nums):
            if index + 1 == len(nums):
                return True
            elif value == nums[index + 1]:
                return False


if __name__ == '__main__':
    solution = Solution()
    # print(solution.shortestToChar('loveleetcode', 'e'))
    # print(solution.shortestToChar('aaba', 'b'))
    # print(solution.shortestToChar('baaa', 'b'))
    # print(solution.shortestToChar('aaab', 'b'))
    # print(solution.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
    print(solution.hasAlternatingBits(11))
