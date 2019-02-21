2/20/2019 <br />
<br />
5143_Shell_Project <br />
#### Group Members

- Daniel Bowen
- Sun Shenglin

 <br />
 #### Overview:
 
Implementation of basic shell with the following list of commands. All commands work.   <br />
<br />
 #### Instructions

- All flags are to be passed to the calling command in the following format: (command) (flags) (parameters).
- When piping, assume that the output will be in the (parameters) location.
- Flags can be passed altogether or as several separate dashes, but must be before the parameters.
- All -n flags are to be immediately followed by a number contatenated like "-n10".
<br />
 ***Commands***:

|   command       |   description            | Author      |    Notes                             |
|:---------------:|:------------------------:|:-----------:|:-----------------------------------: |
| cat             | concatenates files       | Daniel      |                                      |
| cd              | changes directory        | Daniel      |                                      |
| chmod           | changes permissions      | Daniel      |                                      |
| cp              | copies file              | Daniel      |                                      |
| exit            | exits shell              | Daniel      |                                      |
| grep            | finds all keywords       | Daniel      |                                      |
| head            | prints top lines         | Daniel      |                                      |
| history         | prints cmd history       | Daniel      | -c flag will clear the .history.txt  |
| less            | pages through file       | Daniel      |                                      |
| ls              | lists all files          | Sun & Daniel| Only works on current directory      |
| mv              | moves a file or dir      | Daniel      |                                      |
| mkdir           | makes a direcotry        | Daniel      |                                      |
| rm              | removes file or dir      | Daniel      |                                      |
| rmdir           | removes empty dir        | Daniel      |                                      |
| sort            | sorts alphebetical       | Daniel      | Sorts by capital letter then lower   |
| tail            | prints bottom lines      | Daniel      |                                      |
| touch           | makes empty file         | Daniel      |                                      |
| wc              | prnts words,lines,chars  | Daniel      |                                      |
| who             | displays users logged in | Daniel      |                                      |
| pwd             | prints current work dir  | Daniel      |                                      |
|  |              |output from cmd to another| Daniel      |                                      |
|  >              | output cmd to file       | Daniel      |                                      |
|  >>             | append cmd output to file| Daniel      |                                      |

References: Printing of tabular format for ls heavily influenced by https://codereview.stackexchange.com/questions/188353/vertically-print-a-list-of-strings-to-stdout-into-3-columns-with-column-lengths
