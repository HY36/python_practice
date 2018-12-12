from collections import Counter
from functools import reduce
from operator import add


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
        words_morse = [''.join([morse_code[ord(i) - 97] for i in word]) for word in words]
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
        index_list = [i <= first_line or i <= second_line or i <= third_line for i in set_words]
        return [words[index] for index, _ in enumerate(words) if index_list[index]]

    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = reduce(add, zip([i for i in A if i % 2 == 0], [i for i in A if i % 2 == 1]))
        return list(result)

    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mountain_map = {value: index for index, value in enumerate(A)}
        max_key = max(mountain_map.keys())
        return mountain_map[max_key]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findWords(["Hello", "Alaska", "Dad", "Peace"]))
