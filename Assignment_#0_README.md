#A MarkDown File

##[PARAGRAPHS AND LINE BREAKS][1]  
>A paragraph is simply one or more consecutive lines of text,
separated by one or more blank lines.
(A blank line is any line that looks like a blank line — a line containing nothing but spaces or tabs is considered blank.) 
Normal paragraphs should not be indented with spaces or tabs.
The implication of the “one or more consecutive lines of text” rule is that Markdown supports “hard-wrapped” text paragraphs.
This differs significantly from most other text-to-HTML formatters 
(including Movable Type’s “Convert Line Breaks” option) 
which translate every line break character in a paragraph into a <br /> tag.
When you do want to insert a <br /> break tag using Markdown, 
you end a line with two or more spaces, then type return.
Yes, this takes a tad more effort to create a <br />,
but a simplistic “every line break is a <br />” rule wouldn’t work for Markdown. 
Markdown’s email-style blockquoting and multi-paragraph list items work best — and look better — 
when you format them with hard breaks.



##Block
> **Note:** Something here line1,  
line2............................    


somethingelse
> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
[From here](http://daringfireball.net/projects/markdown/syntax#blockquote)

##Picture
![cmd-markdown-logo](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/6-001s05.jpg)

##List
*   Red
*   Green
*   Blue

##Table

Column1     | Column2
-------- | ---
1.2 |  **vector**
*abc*    | 23
5     | md

##Code

```c
#include <stdio.h>
main()
{
  printf("Hello World!\n");
}
```
##Title
##SubTitle_1
##SubTitle_2
###SubSubTitle_2.1
###SubSubTitle_2.2
or
This is an H1
=============

This is an H2
-------------

 
---
***
===



[1]: http://daringfireball.net/projects/markdown/syntax

