# splay
Searches User Specified Term in Given or Current dir (Recursively), and Plays all Matching Terms in MPV player.
### Dependencies:
Python3+, mpv Player
### Installation:
`git clone https://github.com/electrodragon/splay.git`
### Usage:
This Searches for files in current directory recursively.

`splay searchterm1 searchterm2 searchterm3`

This Searches for files in provided directories recursively.

`splay --dir=/path/to/dir --dir=/path/to/other/dir SearchTerm`
### Options:
`--no-video` Same as MPV Player

`--shuffle` Shuffles found files

`--gs` Grand Search

- File: "Hello (Official Video) - Adele.mp4"
- File: "Hello (Official Video) - Lyrics.mp4"
- File: "Hello (Official Video).mp4"

`splay 'helo' --gs` Will Find all above

To Find Uniques:

`splay 'helo adele' --gs` Will Find "Hello (Official Video) - Adele.mp4"

### Examples:
`splay ''` Plays all 

`splay '' --shuffle --no-video` Plays all as Shuffled, without showing video !

`splay lyric` plays files containing word lyric (Case insensitive).

`splay --dir=~/Songs ''` Plays all files in given Directory.

`splay --dir='~/Best Songs' mp3` plays files in given dir having 'mp3' in their name.

`splay --dir=~/Best\ Songs mp3` alternative way of above.
