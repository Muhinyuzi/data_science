
# First we'll import the re module, which is where python stores regular expression libraries.
import re
# There are several main processing functions in re that you might use. The first, match() checks for a match
# that is at the beginning of the string and returns a boolean. Similarly, search(), checks for a match
# anywhere in the string, and returns a boolean.
# Lets create some text for an example
text = "This is a good day."
# Now, lets see if it's a good day or not:
if re.search("good", text): # the first parameter here is the pattern
    print("Wonderful!")
else:
    print("Alas :(")
# In addition to checking for conditionals, we can segment a string. The work that regex does here is called
# tokenizing, where the string is separated into substrings based on patterns. Tokenizing is a core activity
# in natural language processing, which we won't talk much about here but that you will study in the future
# The findall() and split() functions will parse the string for us and return chunks. Lets try and example
text = "Amy works diligently. Amy gets good grades. Our student Amy is succesful."
# This is a bit of a fabricated example, but lets split this on all instances of Amy
re.split("Amy", text)
['',
 ' works diligently. ',
 ' gets good grades. Our student ',
 ' is succesful.']
# You'll notice that split has returned an empty string, followed by a number of statements about Amy, all as
# elements of a list. If we wanted to count how many times we have talked about Amy, we could use findall()
re.findall("Amy", text)
['Amy', 'Amy', 'Amy']
# Ok, so we've seen that .search() looks for some pattern and returns a boolean, that .split() will use a
# pattern for creating a list of substrings, and that .findall() will look for a pattern and pull out all
# occurences.
# Now that we know how the python regex API works, lets talk about more complex patterns. The regex
# specification standard defines a markup language to describe patterns in text. Lets start with anchors.
# Anchors specify the start and/or the end of the string that you are trying to match. The caret character ^
# means start and the dollar sign character $ means end. If you put ^ before a string, it means that the text
# the regex processor retrieves must start with the string you specify. For ending, you have to put the $
# character after the string, it means that the text Regex retrieves must end with the string you specify.
# Here's an example
text = "Amy works diligently. Amy gets good grades. Our student Amy is succesful."
# Lets see if this begins with Amy
print(re.search("^Amy",text))
# Notice that re.search() actually returned to us a new object, called re.Match object. An re.Match object
# always has a boolean value of True, as something was found, so you can always evaluate it in an if statement
# as we did earlier. The rendering of the match object also tells you what pattern was matched, in this case
# the word Amy, and the location the match was in, as the span.
#Patterns and Character Classes
# Let's talk more about patterns and start with character classes. Let's create a string of a single learners'
# grades over a semester in one course across all of their assignments
grades="ACAAAABCBCBAA"
# If we want to answer the question "How many B's were in the grade list?" we would just use B
print(re.findall("B",grades))
# If we wanted to count the number of A's or B's in the list, we can't use "AB" since this is used to match
# all A's followed immediately by a B. Instead, we put the characters A and B inside square brackets
print(re.findall("[AB]",grades))
# This is called the set operator. You can also include a range of characters, which are ordered
# alphanumerically. For instance, if we want to refer to all lower case letters we could use [a-z] Lets build
# a simple regex to parse out all instances where this student receive an A followed by a B or a C
print(re.findall("[A][B-C]",grades))
# Notice how the [AB] pattern describes a set of possible characters which could be either (A OR B), while the
# [A][B-C] pattern denoted two sets of characters which must have been matched back to back. You can write
# this pattern by using the pipe operator, which means OR
print(re.findall("AB|AC",grades))
# We can use the caret with the set operator to negate our results. For instance, if we want to parse out only
# the grades which were not A's
print(re.findall("[^A]",grades))
# Note this carefully - the caret was previously matched to the beginning of a string as an anchor point, but
# inside of the set operator the caret, and the other special characters we will be talking about, lose their
# meaning. This can be a bit confusing. What do you think the result would be of this?
print(re.findall("^[^A]",grades))
# It's an empty list, because the regex says that we want to match any value at the beginning of the string
# which is not an A. Our string though starts with an A, so there is no match found. And remember when you are
# using the set operator you are doing character-based matching. So you are matching individual characters in
# an OR method.
#Quantifiers
# Ok, so we've talked about anchors and matching to the beginning and end of patterns. And we've talked about
# characters and using sets with the [] notation. We've also talked about character negation, and how the pipe
# | character allows us to or operations. Lets move on to quantifiers.
# Quantifiers are the number of times you want a pattern to be matched in order to match. The most basic
# quantifier is expressed as e{m,n}, where e is the expression or character we are matching, m is the minimum
# number of times you want it to matched, and n is the maximum number of times the item could be matched.
# Let's use these grades as an example. How many times has this student been on a back-to-back A's streak?
print(re.findall("A{2,10}",grades)) # we'll use 2 as our min, but ten as our max
# So we see that there were two streaks, one where the student had four A's, and one where they had only two
# A's
# We might try and do this using single values and just repeating the pattern
print(re.findall("A{1,1}A{1,1}",grades))
# As you can see, this is different than the first example. The first pattern is looking for any combination
# of two A's up to ten A's in a row. So it sees four A's as a single streak. The second pattern is looking for
# two A's back to back, so it sees two A's followed immediately by two more A's. We say that the regex
# processor begins at the start of the string and consumes variables which match patterns as it does.
# It's important to note that the regex quantifier syntax does not allow you to deviate from the {m,n}
# pattern. In particular, if you have an extra space in between the braces you'll get an empty result
print(re.findall("A{2, 2}",grades))
# And as we have already seen, if we don't include a quantifier then the default is {1,1}
print(re.findall("AA",grades))
# Oh, and if you just have one number in the braces, it's considered to be both m and n
print(re.findall("A{2}",grades))
# Using this, we could find a decreasing trend in a student's grades
print(re.findall("A{1,10}B{1,10}C{1,10}",grades))
# Now, that's a bit of a hack, because we included a maximum that was just arbitrarily large. There are three
# other quantifiers that are used as short hand, an asterix * to match 0 or more times, a question mark ? to
# match one or more times, or a + plus sign to match one or more times. Lets look at a more complex example,
# and load some data scraped from wikipedia
with open("datasets/ferpa.txt","r") as file:
    # we'll read that into a variable called wiki
    wiki=file.read()
# and lets print that variable out to the screen
print(wiki)
# Scanning through this document one of the things we notice is that the headers all have the words [edit]
# behind them, followed by a newline character. So if we wanted to get a list of all of the headers in this
# article we could do so using re.findall
print(re.findall("[a-zA-Z]{1,100}\[edit\]",wiki))
# Ok, that didn't quite work. It got all of the headers, but only the last word of the header, and it really
# was quite clunky. Lets iteratively improve this. First, we can use \w to match any letter, including digits
# and numbers.
print(re.findall("[\w]{1,100}\[edit\]",wiki))
# This is something new. \w is a metacharacter, and indicates a special pattern of any letter or digit. There
# are actually a number of different metacharacters listed in the documentation. For instance, \s matches any
# whitespace character.
# Next, there are three other quantifiers we can use which shorten up the curly brace syntax. We can use an
# asterix * to match 0 or more times, so let's try that.
print(re.findall("[\w]*\[edit\]",wiki))
# Now that we have shortened the regex, let's improve it a little bit. We can add in a spaces using the space
# character
print(re.findall("[\w ]*\[edit\]",wiki))
# Ok, so this gets us the list of section titles in the wikipedia page! You can now create a list of titles by
# iterating through this and applying another regex
for title in re.findall("[\w ]*\[edit\]",wiki):
    # Now we will take that intermediate result and split on the square bracket [ just taking the first result
    print(re.split("[\[]",title)[0])
# Ok, this works, but it's a bit of a pain. To this point we have been talking about a regex as a single
# pattern which is matched. But, you can actually match different patterns, called groups, at the same time,
# and then refer to the groups you want. To group patterns together you use parentheses, which is actually
# pretty natural. Lets rewrite our findall using groups
print(re.findall("([\w ]*)(\[edit\])",wiki))
# Nice - we see that the python re module breaks out the result by group. We can actually refer to groups by
# number as well with the match objects that are returned. But, how do we get back a list of match objects?
# Thus far we've seen that findall() returns strings, and search() and match() return individual Match
# objects. But what do we do if we want a list of Match objects? In this case, we use the function finditer()
for item in re.finditer("([\w ]*)(\[edit\])",wiki):
    print(item.groups())
# We see here that the groups() method returns a tuple of the group. We can get an individual group using
# group(number), where group(0) is the whole match, and each other number is the portion of the match we are
# interested in. In this case, we want group(1)
for item in re.finditer("([\w ]*)(\[edit\])",wiki):
    print(item.group(1))
# One more piece to regex groups that I rarely use but is a good idea is labeling or naming groups. In the
# previous example I showed you how you can use the position of the group. But giving them a label and looking
# at the results as a dictionary is pretty useful. For that we use the syntax (?P<name>), where the parethesis
# starts the group, the ?P indicates that this is an extension to basic regexes, and <name> is the dictionary
# key we want to use wrapped in <>.
for item in re.finditer("(?P<title>[\w ]*)(?P<edit_link>\[edit\])",wiki):
    # We can get the dictionary returned for the item with .groupdict()
    print(item.groupdict()['title'])
# Of course, we can print out the whole dictionary for the item too, and see that the [edit] string is still
# in there. Here's the dictionary kept for the last match
print(item.groupdict())
# Ok, we have seen how we can match individual character patterns with [], how we can group matches together
# using (), and how we can use quantifiers such as *, ?, or m{n} to describe patterns. Something I glossed
# over in the previous example was the \w, which standards for any word character. There are a number of
# short hands which are used with regexes for different kinds of characters, including:
# a . for any single character which is not a newline
# a \d for any digit
# and \s for any whitespace character, like spaces and tabs
# There are more, and a full list can be found in the python documentation for regexes
#Look-ahead and Look-behind
# One more concept to be familiar with is called "look ahead" and "look behind" matching. In this case, the
# pattern being given to the regex engine is for text either before or after the text we are trying to
# isolate. For example, in our headers we want to isolate text which  comes before the [edit] rendering, but
# we actually don't care about the [edit] text itself. Thus far we have been throwing the [edit] away, but if
# we want to use them to match but don't want to capture them we could put them in a group and use look ahead
# instead with ?= syntax
for item in re.finditer("(?P<title>[\w ]+)(?=\[edit\])",wiki):
    # What this regex says is match two groups, the first will be named and called title, will have any amount
    # of whitespace or regular word characters, the second will be the characters [edit] but we don't actually
    # want this edit put in our output match objects
    print(item)
#Example: Wikipedia Data
# Let's look at some more wikipedia data. Here's some data on universities in the US which are buddhist-based
with open("datasets/buddhist.txt","r") as file:
    # we'll read that into a variable called wiki
    wiki=file.read()
# and lets print that variable out to the screen
print(wiki)
# We can see that each university follows a fairly similar pattern, with the name followed by an – then the
# words "located in" followed by the city and state
# I'll actually use this example to show you the verbose mode of python regexes. The verbose mode allows you
# to write multi-line regexes and increases readability. For this mode, we have to explicitly indicate all
# whitespace characters, either by prepending them with a \ or by using the \s special value. However, this
# means we can write our regex a bit more like code, and can even include comments with #
pattern="""
(?P<title>.*)        #the university title
(–\ located\ in\ )   #an indicator of the location
(?P<city>\w*)        #city the university is in
(,\ )                #separator for the state
(?P<state>\w*)       #the state the city is located in"""
# Now when we call finditer() we just pass the re.VERBOSE flag as the last parameter, this makes it much
# easier to understand large regexes!
for item in re.finditer(pattern,wiki,re.VERBOSE):
    # We can get the dictionary returned for the item with .groupdict()
    print(item.groupdict())
#Example: New York Times and Hashtags
# Here's another example from the New York Times which covers health tweets on news items. This data came from
# the UC Irvine Machine Learning Repository which is a great source of different kinds of data
with open("datasets/nytimeshealth.txt","r") as file:
    # We'll read everything into a variable and take a look at it
    health=file.read()
health
# So here we can see there are tweets with fields separated by pipes |. Lets try and get a list of all of the
# hashtags that are included in this data. A hashtag begins with a pound sign (or hash mark) and continues
# until some whitespace is found
# So lets create a pattern. We want to include the hash sign first, then any number of alphanumeric
# characters. And we end when we see some whitespace
pattern = '#[\w\d]*(?=\s)'
# Notice that the ending is a look ahead. We're not actually interested in matching whitespace in the return
# value. Also notice that I use an asterix * instead of the plus + for the matching of alphabetical characters
# or digits, because a + would require at least one of each
# Lets searchg and display all of the hashtags
print(re.findall(pattern, health))
# We can see here that there were lots of ebola related tweeks in this particular dataset.
