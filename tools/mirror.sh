#!/bin/sh

array=(
0001-the-draft-version-to-use-to-get-answer-from-numbers.patch
0002-add-permutations-for-calculation.patch
0003-add-data-from-arguments.patch
0004-the-draft-version-of-6-3.py-but-there-is-a-bug.patch
0005-refine-the-code-to-find-the-answer-with-steps-displa.patch
0006-add-TODO-items-for-6-3.py.patch
0007-add-draft-recursive-sample-for-8-1-8-3-and-8-4-examp.patch
0008-refine-8-1-8-3-8-4-algorithm-with-stack-solution-and.patch
0009-add-8-2-8-5-flow-with-recursive-solution.patch
0010-add-the-solution-for-coins-and-8-quuens.patch
0011-add-basic-sort-methods.patch
0012-add-some-solution-about-math-questions.patch
0013-add-bit-related-test-solution.patch
0014-add-bit-solutions.patch
)

for i in "${array[@]}" 
do                     
	filename=$i           
	committime=`/c/Python34/python.exe ../tools/getGitDate.py ../prog/programming/$filename`
	echo $committime
  git am ../prog/programming/$filename                            	
  git commit --amend --reset-author --no-edit --date="$committime"	
  echo $filename "done"
done                   
