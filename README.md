# Hands-on-with-python-regex-log-parsing-

Some of the basic regex used in Python are: -
SYMBOL	                DESCRIPTION
.	            dot matches any character except newline
\w	          matches any word character i.e letters, alphanumeric, digits and underscore ( _ )
\W	          matches non word characters
\d	          matches a single digit
\D	          matches a single character that is not a digit
\s	          matches any white-spaces character like \n, \t, spaces
\S	          matches single non white space character
[abc]	        matches single character in the set i.e either match a, b or c
[^abc]	      match a single character other than a, b and c
[a-z]	        match a single character in the range a to z.
[a-zA-Z]	    match a single character in the range a-z or A-Z
[0-9]	        match a single character in the range 0-9
[a-z0-9]      match a single character in the range a-z or 0-9 (alpha-numeric match)
^	            match start at beginning of the string
$	            match start at end of the string
+	            matches one or more of the preceding character (greedy match).
*	            matches zero or more of the preceding character (greedy match).
