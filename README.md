Prounoun Mix
============

This is a program that will take a Markdown file, and turn it into a webpage that randomizes all the characters pronouns every time someone views the page. It works like this. Say you have a Character named Bob. Instead of writing "Bob wrote his name in the sand", write "Bob wrote b-his name in the sand" or "Bob wrote b-her name in the sand", or any other grammatical pronoun with a character-specific prefix.

Then, at the bottom of your file, include a section like this:

```
-----

IDs: a- b- v-
he him his He Him His he's He's
she her her She Her Her she's She's
they them their They Them Their they're They're
ve vim ver Ve Vim Ver ve's Ve's
e em es e em es em's em's
fae faer faer's Fae Faer Faer's fae's Fae's
```

Put a line with five dashes, followed by a blank line, followed by the different character ids for all your characters. Then, on the remaining lines, put all the pronoun options that you want available. Note that the sets of pronouns should go in the same order on each line.

Now all you need to do is run the tool! (Note: If the following seems impossible and/or scary, please feel free to contact me at @setupminimal on Twitter, or via setupminimal@gmail.com for assistence)

Installation
------------

You will need `python` installed, as well as the `markdown` library. You can get `markdown` through `pip`, and `pip` and `python` from https://python.org.

Next, you need to download `pronounMix.py`. You can click on "Clone or download" up above, and select the ZIP option, then just unZIP it. Or you can use `git clone https://github.com/setupminimal/pronoun-mix` if you are comfortable with git.

Then, just run `python pronounMix.py StoryFile.md OutputFile.html` in a terminal.

`OutputFile.html` should then be a fully-functional, if bare, webpage. You can host it on your website, send it to a friend, fax it to Alaska, whatever tickles your fancy.

Use on Other Webpages
---------------------

If you give the `--just-js` option on the command line, the script will just generate the JavaScript that you need to inject into your webpage to randomize pronouns on the entire page.

Problems
--------

If you have problems or suggestions, please feel free to go open an issue! I'd love to see this being used.

License
-------

This work is released under a GPL v3 license - you can modify, redistribute, and use this work, as long as all derivative works have the same protections.