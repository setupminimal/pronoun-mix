"A module to randomize pronouns in stories."

import sys
import random

def error(s):
    sys.stderr.write(s+"\n")
    sys.stderr.flush()

with open(sys.argv[1], "r") as f:
    text = f.read()


text = text.split("\n-----\n")
if len(text) == 2:
    story = text[0]
    info = text[1]
else:
    error("Could not parse your story file.")
    error("Are you sure that you have a single '-----' on it's own line, with blank lines around it, separating your main text from the information I need to parse your pronouns?")
    sys.exit(1)

# Info is formatted like this:
# IDS: names separated by whitespace
# pronoun option records

info = info.split("\n")
info = [x for x in info if x.strip() != ""]

if not info[0].startswith("IDs: "):
    error("There's a problem with your info section.")
    error("Do you have a line starting with 'IDs: ' to let me know what prefixes you used for each character/group?")
    sys.exit(2)

ids = info[0].split()[1:]
pronounGroups = [line.split() for line in info[1:]]

groupLengths = [len(g) for g in pronounGroups]
if max(groupLengths) != min(groupLengths):
    error("There's a problem with your pronoun section.")
    error("Not all of the lists are the same length.")
    error("Could you please check that your pronoun definitions are correct?")
    sys.exit(3)

# Begin actual replacement section.

wrongReplacements = {}
replacements = {}
for id in ids:
    pronouns = random.choice(pronounGroups)
    wrongs = random.choice([x for x in pronounGroups if x != pronouns])
    error("Using '"+pronouns[0]+"' pronouns for "+id+".")
    error("  ... and '"+wrongs[0]+"' pronouns when someone misgenders "+(id if len(pronouns) < 2 else pronouns[1])+".")
    for origional in pronounGroups:
        for (orig, noun) in zip(origional, pronouns):
            replacements[id+orig] = noun
        for (orig, wrong) in zip(origional, wrongs):
            wrongReplacements["!"+id+orig] = wrong

# Perform replacements

for key, value in wrongReplacements.items():
    story = story.replace(key, value)
for key, value in replacements.items():
    story = story.replace(key, value)

if len(sys.argv) == 3:
    with open(sys.argv[2], "w") as f:
        f.write(story)
else:
    print(story)
