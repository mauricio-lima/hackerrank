Regex_Pattern = r'^[A-Za-z]*s$'	 
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
