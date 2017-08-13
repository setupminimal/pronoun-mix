"A module to randomize pronouns in stories."

from __future__ import print_function

import markdown # For transforming the story
import codecs # For UTF-8

import sys
import random

def error(s):
    "Output an error"
    sys.stderr.write(s+"\n")
    sys.stderr.flush()

# The following flag determines if we want the whole webpage, or just the Javascript
jsFlag = "--just-js" in sys.argv
sys.argv = [x for x in sys.argv if x != "--just-js"]

with codecs.open(sys.argv[1], mode="r", encoding="utf-8") as f:
    text = f.read() # Read in the story's text


text = text.split("\n-----\n") # Find our section
if len(text) == 2:
    story = text[0] # The story part
    info = text[1]  # The pronoun specification part
else:
    error("Could not parse your story file.")
    error("Are you sure that you have a single '-----' on it's own line, with blank lines around it, separating your main text from the information I need to parse your pronouns?")
    sys.exit(1)

# Info is formatted like this:
# IDS: names separated by whitespace
# pronoun option records

info = info.split("\n") # Get each line
info = [x for x in info if x.strip() != ""] # Ignore empty lines

if not info[0].startswith("IDs: "):
    error("There's a problem with your info section.")
    error("Do you have a line starting with 'IDs: ' to let me know what prefixes you used for each character/group?")
    sys.exit(2)

ids = info[0].split()[1:] # Get all the character IDS
pronounGroups = [line.split() for line in info[1:]] # ... and then the sets of pronouns

groupLengths = [len(g) for g in pronounGroups]
if max(groupLengths) != min(groupLengths):
    error("There's a problem with your pronoun section.")
    error("Not all of the lists are the same length.")
    error("Could you please check that your pronoun definitions are correct?")
    sys.exit(3)

# Begin actual replacement section.


# This part is scary and complicated looking. Don't worry, it's just
# creating the Javascript that does the actual replacement in the webpage.
JAVASCRIPT = """pronounGroups = GROUPS;
      ids = IDS;
      
 $(function() {
for (id = 0; id < ids.length; id++) {
        num = Math.floor(Math.random() * (pronounGroups.length - 1))
        pronouns = pronounGroups[num];
        wrong = pronounGroups[(num + 5117) % pronounGroups.length]
        
        for (orig = 0; orig < pronounGroups.length; orig++) {
          for (i = 0; i < pronouns.length; i++) {
            console.log("Replacing "+ids[id]+pronounGroups[orig][i]+" with "+pronouns[i]); 
            $("body").children().each(function() {$(this).html(function (index, old) {return old.replace(new RegExp("!"+ids[id]+pronounGroups[orig][i], 'g'), wrong[i]).replace(new RegExp(ids[id]+pronounGroups[orig][i], 'g'), pronouns[i])});})
          }
        }
}
      });""".replace("IDS", str(ids).replace("u'", "'").replace('u"', '"')).replace("GROUPS", str(pronounGroups).replace("u'", "'").replace('u"', '"'))

TEMPLATE = u"""<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>TITLE</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script>
      JAVASCRIPT
    </script>
  </head>
  <body id="body"><div>
    STORY</div>
  </body>
</html>
""".replace("TITLE", story.split("\n")[0]).replace("STORY", markdown.markdown(story)).replace("JAVASCRIPT", JAVASCRIPT).encode("ascii", "xmlcharrefreplace")

if len(sys.argv) == 3:
    with open(sys.argv[2], "w") as f:
        f.write(TEMPLATE if not jsFlag else JAVASCRIPT)
else:
    print(TEMPLATE if not jsFlag else JAVASCRIPT)
