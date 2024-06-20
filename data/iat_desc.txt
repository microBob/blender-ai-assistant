Open IAT
==================

This is a version of the Implicit Association Test made in PsychoPy that can
run online or on a local PsychoPy installation.

It provides the classic black/white versus positive/negative version of the IAT
but it's designed so that you can update to use your own stimuli as needed.

Credits
-----------------

The IAT was originally developed by Greenwald et al (1998).

This PsychoPy version was originally developed by Robin Scaife on the Leverhulme Trust "Bias and Blame"
project 2014. Additional coding by Tom Stafford with thanks to Lily Fitzgibbon for advice.

Updated by Jon Peirce to support online studies in 2019.

References
-----------------

Greenwald, Anthony G.; McGhee, Debbie E.; Schwartz, Jordan L.K. (1998),
"Measuring Individual Differences in Implicit Cognition: The Implicit Association Test",
Journal of Personality and Social Psychology, 74 (6): 1464–1480, CiteSeerX 10.1.1.489.4611,
doi:10.1037/0022-3514.74.6.1464, PMID 9654756

J. Peirce, J.R. Gray, S. Simpson, M. MacAskill, R. Höchenberger, H. Sogo, E. Kastman, J.K. Lindeløv. (2019),
"PsychoPy2: Experiments in Behavior Made Easy", Behav Res Methods 51: 195. https://doi.org/10.3758/s13428-018-01193-y

Customizing the task for other versions
--------------------------------------------

The implementation here uses a spreadsheet files to define the block orders being
used. You can see the block_order xlsx files and the conditions files for each block
(cong_train.xlsx, cong_test.xlsx etc.) in the *resources* folder.

To change the stimuli for your own task you can simply change the lines in the
conditions files to set what is considered a congruent or incongruent train/test
condition.
