from collections import Counter
from functools import reduce, lru_cache
from operator import add, xor
from typing import Iterator, List, Dict
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
        result = set()
        for i in A:
            if i in result:
                return i
            else:
                result.add(i)

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
                if last == 0:
                    result.extend(list(range(last + 1, index + 1)))
                else:
                    for i in range(last, index):
                        result.append(list(range(last, index + 1)))
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
        distance = {tuple(value): sqrt(
            pow(value[0], 2) + pow(value[1], 2)) for index, value in enumerate(points)}
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

    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        result = []
        even_value = sum(i for i in A if i % 2 == 0)
        even_set = {key for key, value in enumerate(A) if value % 2 == 0}
        for query in queries:
            val = query[0]
            index = query[1]
            if (A[index] + val) % 2 == 0:
                if index not in even_set:
                    even_value += (A[index] + val)
                    even_set.add(index)
                else:
                    even_value += val
            else:
                if index in even_set:
                    even_value -= A[index]
                    even_set.discard(index)
            A[index] += val
            result.append(even_value)
        return result

    def smallestRangeI(self, A: List[int], K: int) -> int:
        d_value = max(A) - min(A)
        k_value = 2 * K
        if d_value <= k_value:
            return 0
        return d_value - k_value

    def diStringMatch(self, S: str) -> List[int]:
        result = []
        choice_list = range(len(S) + 1)
        right_index = -1
        left_index = 0
        for i in S:
            if i == 'D':
                result.append(choice_list[right_index])
                right_index -= 1
            else:
                result.append(choice_list[left_index])
                left_index += 1
        result.append(choice_list[left_index])
        return result

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums2) & set(nums1))

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_map: Dict[str, str] = dict()
        for domains in cpdomains:
            count, domain = domains.split(' ')
            domain_key = domain.split('.')
            if len(domain_key) == 3:
                parent_domain = domain_key[1] + '.' + domain_key[2]
                domain_map[domain] = count
            else:
                parent_domain = domain_key[0] + '.' + domain_key[1]
            top_domain = domain_key[-1]
            try:
                domain_map[parent_domain] = str(int(domain_map[parent_domain]) + int(count))
            except KeyError:
                domain_map[parent_domain] = count
            try:
                domain_map[top_domain] = str(int(domain_map[top_domain]) + int(count))
            except KeyError:
                domain_map[top_domain] = count
        return [value + ' ' + key for key, value in domain_map.items() if key != '']

    def calPoints(self, ops: List[str]) -> int:
        result = 0
        points: List[int] = []
        for i in ops:
            if i == 'C':
                result -= int(points[-1])
                points.pop(-1)
            elif i == 'D':
                tmp_point = 2 * points[-1]
                result += tmp_point
                points.append(tmp_point)
            elif i == '+':
                tmp_point = points[-1] + points[-2]
                result += tmp_point
                points.append(tmp_point)
            else:
                tmp_point = int(i)
                result += tmp_point
                points.append(tmp_point)
        return result

    def removeOuterParentheses(self, S: str) -> str:
        left = 0
        right = 0
        result = ''
        position = 0
        for index, s in enumerate(S):
            if s == '(':
                left += 1
            else:
                right += 1
            if left == right:
                result += S[position+1:index]
                left , right = 0, 0
                position = index+1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
    # print(solution.shortestToChar('loveleetcode', 'e'))
    # print(solution.shortestToChar('aaba', 'b'))
    # print(solution.shortestToChar('baaa', 'b'))
    # print(solution.shortestToChar('aaab', 'b'))
