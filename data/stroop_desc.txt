# Stroop - measuring reaction times to incongruent stimuli

These files are maintained by the Open Science Tools team.

## The experiment

In this task subjects must report the colour of the letters spelling each word, but letters themselves also spell a colour name and this may be the
same or different to the colour of the letters. Stroop (1935) reports that reaction times are slower the letters spell a colour that is incongruent
with the colour of the letters, indicating a compulsory automated reading of the word.

## Analysing your data

After you run the study, look in the data/ folder next to where the experiment was saved. There will be an xlsx file there that can be opened
with Microsoft Excel or similar spreadsheet package. Each row represents one condition (trial type) and each column is one variable of your experiment
or type of data collected.

Take the average of the resp.mean_rt column for the 3 congruent conditions and compare them with the 3 incongruent conditions. In most cases the
incongruent conditions will have larger reactions times.

## Notes

This version of the Stroop effect is a very simple experiment, good for explaining how the PsychoPy Builder interface works with minimal clutter.
You could (as a challenge) add practice trials and feedback if you liked...?!

## References

Stroop, J. R. (1935). Studies of interference in serial verbal reactions. Journal of Experimental Psychology, 18(6), 643-662.

Online optimisation by SLM (2022-01-20)
