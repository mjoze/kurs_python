"""Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
 Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"""


def solution(string,markers):
    pass


markers = ['#', '!']
string = "apples, pears # and bananas\ngrapes\nbananas !apples"
x = string.replace(' ','')
print(x)
print(string)
b = string[:string.index('#')]
print(b)