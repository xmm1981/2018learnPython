# @Time : 2020/11/25 12:26 
# @Author : xmm1981

# ^ $  模式
# import re
# # line = "xmm123"
# line = "bobby123"
# # regex_str = "^x.*"
# regex_str = "^x.*3$"
# if re.match(regex_str, line):
#     print("yes")

# ？？？？   非贪婪模式
# import re
# line = "booooobaaoooooobbbbbby123"
# regex_str = ".*?(b.*b).*"
# match_obj = re.match(regex_str, line)
# if match_obj:
#     print(match_obj.group(1))

# +    {x}   非贪婪模式
import re
line = "booooobaaoooooobbabaaaaaaaby123"
regex_str = ".*(b.{2-5}b).*"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))