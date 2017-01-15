## What?
[WikiCreole](http://wikicreole.org) is a markup language for wikis. This very wiki site uses it. It lets you mark links, bold or italic text, headings, lists, etc.  using simple conventions. Parser is the part of a wiki engine that takes this text and turns it into HTML with real, working links and nicely styled content.

While practically every wiki engine uses its own variation of markup, WikiCreole is a collection of the most commonly used elements -- the base of wiki markups. You can extend it, adding additional elements as you need them.

The file `creole.py` is a parser for WikiCreole written in Python, to be used in all sorts of Python applications. It was initially written for [MoinMoin](http://moinmo.in) wiki engine, but can be easily used with almost anything.

## How?
I think the easiest way to use the parser is to start with the example application, and modify and extend it to fit one's particular needs.

You need to provide an "emit" method for every kind of element that can be
encountered in the parsed wiki text. The method should return the text for
that element. The example emits HTML -- it's fairly usable, except for the
link code -- you should replace it with one that better fits your particular wiki engine.

## How much?
Free. Initially the module had to be licensed under GPL, since MoinMoin's code, from which it comes, uses that license. But all the authors agreed to also release it under a less restrictive (for the programmers, not for the freedom of software) BSD-like license.
