making this readme since someone on twitter asked for it

It is not very well documented since I was not planning on working on it for more than a day. If you want to try using it
, I run it as a using vscode's build in notebook thing, you can do the special comment #%% to create a section and run sections that way.

The main file is trees.py, it makes a 'coordinator' object, and the member function newbBranch() is used to create an object.
objects in the tree's purview are in a dictionary, keyed by their parent object( object '1.2.3' is the third child of the second child of the first object)

new branch takes the parent's name, a string or int for the child name, 
a starting position
(tuple of three numbers representing x, y, and angle),
and an 'options' object which has all of the various parameters used in generating the object,
as well as a function which creates a new options object to be used for any sub-branches that the object decides to grow off the main branch.
Also contains a reference to a generator function (in generators.py) which is used to populate the object's vertices
the options class is in branchconfig.py

if you want to mess around with it, easiest way is to create a new options object, change the settings to whatever you want,
and change the argument of newBranch in trees.py. the default settings should make a pretty normal looking tree, I have changed
it significantly since I made that tweet so the trees should be a bit less sparsely populated

I'm not a very experienced programmer so dont judge me lol

