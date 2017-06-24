1. Create a folder called data in the folder where you put the current python file.
2. Paste the IRIS train and test data into it.
3. Run the code.
4. Two new files called accuracy.txt and tree_diagram.txt will appear.

Description:
I referred to the decision tree tutorial here to implement the given tree.
http://www.patricklamle.com/Tutorials/Decision%20tree%20python/tuto_decision%20tree.html
The bulk of the work is done in the build_tree method which forms a basis recursive function creating a structure
called the TreeStructure which has different attributes needed through the process for display of the decision rule,
display of the probabilities and numbers on either branch of the tree and for use in classification of test terms.
The tricky logic is to create a backtracked pointer that loops through all possible values of a column and considers
each of them a candidate for threshold value around which lists are split. To consider the optimal candidate, information
gain is calculated and the one with the most gain is chosen as a child tree for further decision rule splits. Once a best
split is found, its values are stored in (_best) variables.
