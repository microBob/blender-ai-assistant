The Choice Reaction Time Task
======================================================

Reaction times have been studies for over 100 years and a staple of scientific study in psychology. A commonly used procedure is to study reaction time involves measuring reaction times to a choice of stimuli.

The task
--------------

In a choice reaction time task, participants must make a decision related to the stimulus (such as what shape it is) and respond accordingly. 
E.g., participants must click left if the stimulus is blue and right if the stimulus is red.

In this case, participants must click or press **c** if the stimulus is a cross, **v** for a square, or **b** for a plus.

This demo experiment has 9 practice trials and 18 experimental trials. After each practice trial, a window will appear displaying several pieces of information (to demonstrate how you could make use of responses in later routines):
* The full duration of the trial
* The RT that will appear in the datafile
* The type of response that was detected
* Whether or not the response was correct

Participants can respond in any of three ways:
* Using the appropriate keyboard keys
* Clicking on the appropriate button with the mouse
* Pressing on the appropriate button, if using a touchscreen

It's worth looking at how the response is recorded in the datafile differs according to which input was used!

=======
In a choice reaction time task, participants must observe the stimulus and then make a decision about it before responding. 
In this version, the stimulus can either be a cross, a plus, or a square. The participant must decide which has appeared, and respond with the appropriate key/button.


Analysis
--------------
All times are reported with regard to the beginning of the Routine. If you wish to analyse the data created by this experiment, the target initiation time (onsetTime) should be subtracted from the reported RT (the time a response has been made - i.e. keyResp.rt or mouseResp.time). This is already calculated (see trialRespTimes in data output). The accuracy of keyboard (keyResp.corr) and mouse clicks (correctMouseResp) are also saved. See relevant column headers in data output.

=======

Extensions
--------------

See if you can modify this task so that randomization of the ISI is handled within a code component, rather than using a set ISI from the excel conditions file.

References
--------------

Deary, I. J., Liewald, D., & Nissan, J. (2011). A free, easy-to-use, computer-based simple and four-choice reaction time programme: the Deary-Liewald reaction time task. Behavior research methods, 43(1), 258-268.



This version created by JAP 2021-10-28, original by DB. Online optimisation by SLM 2022-01-07
=======

