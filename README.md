# File Namer
A script for renaming my microscope images based on my method of naming microscope images.
Generally I name the first image taken of a given sample at a given magnification as follows:
`<growth id>_<sample number>_<Top | Bottom>_<magnification>.jpg`. 
All subsequent images, until the next one that obeys that format, are taken of the same sample at the same magnification
(to remove the need for naming each image on-the-fly, allowing me to take a lot of images quickly).

The next image that obeys the format represents the next sample or magnification, and then the next bunch are at that magnification, etc.

## The goal:
For each image whose name matches the given format (I call this the "leader" file), append a `_1` before the file extension.
For each subsequent image of the same sample/at the same magnification, 
rename it to the same as the leader of that series but with the next number appended (i.e. `_2`, `_3`, ... ).

~~As a test, running this program on the contents of `to_rename` should produce the same files as are in `2022-02-14`
(same name and contents, possibly different metadata)~~

**EDIT:** the above directories have been deleted, but it didn't work anyway because copying and renaming directory via cp changed the modification time.
In the future, run without renaming directory (perhaps copying files one by one via `cp namer\ samples/* to_rename/` would have worked?).

Otherwise, I know it seems to work in the way it is supposed to.

## Usage:
`python namer.py "./to_rename/"`
