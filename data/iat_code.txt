/**************** 
 * Openiat Test *
 ****************/

import { PsychoJS } from './lib/core-2020.1.js';
import * as core from './lib/core-2020.1.js';
import { TrialHandler } from './lib/data-2020.1.js';
import { Scheduler } from './lib/util-2020.1.js';
import * as util from './lib/util-2020.1.js';
import * as visual from './lib/visual-2020.1.js';
import * as sound from './lib/sound-2020.1.js';

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('black'),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'openIAT';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'order': ['random', 1, 2], 'session': '001', 'gender': ['male', 'female', 'other']};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const instruct_pagesLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(instruct_pagesLoopBegin, instruct_pagesLoopScheduler);
flowScheduler.add(instruct_pagesLoopScheduler);
flowScheduler.add(instruct_pagesLoopEnd);
const blocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(blocksLoopBegin, blocksLoopScheduler);
flowScheduler.add(blocksLoopScheduler);
flowScheduler.add(blocksLoopEnd);
flowScheduler.add(end_thanksRoutineBegin());
flowScheduler.add(end_thanksRoutineEachFrame());
flowScheduler.add(end_thanksRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'resources/pos_neg_train.xlsx', 'path': './resources/pos_neg_train.xlsx'},
    {'name': 'stimuli/black_1.jpg', 'path': './stimuli/black_1.jpg'},
    {'name': 'resources/cong_test.xlsx', 'path': './resources/cong_test.xlsx'},
    {'name': 'resources/incong_test.xlsx', 'path': './resources/incong_test.xlsx'},
    {'name': 'stimuli/white_4.jpg', 'path': './stimuli/white_4.jpg'},
    {'name': 'stimuli/blank.png', 'path': './stimuli/blank.png'},
    {'name': 'resources/blocks_order1.xlsx', 'path': './resources/blocks_order1.xlsx'},
    {'name': 'stimuli/white_5.jpg', 'path': './stimuli/white_5.jpg'},
    {'name': 'stimuli/black_3.jpg', 'path': './stimuli/black_3.jpg'},
    {'name': 'stimuli/black_2.jpg', 'path': './stimuli/black_2.jpg'},
    {'name': 'stimuli/white_3.jpg', 'path': './stimuli/white_3.jpg'},
    {'name': 'stimuli/black_4.jpg', 'path': './stimuli/black_4.jpg'},
    {'name': 'resources/cong_train.xlsx', 'path': './resources/cong_train.xlsx'},
    {'name': 'resources/incong_train.xlsx', 'path': './resources/incong_train.xlsx'},
    {'name': 'stimuli/white_2.jpg', 'path': './stimuli/white_2.jpg'},
    {'name': 'stimuli/white_1.jpg', 'path': './stimuli/white_1.jpg'},
    {'name': 'resources/instructs.xlsx', 'path': './resources/instructs.xlsx'},
    {'name': 'stimuli/black_5.jpg', 'path': './stimuli/black_5.jpg'},
    {'name': 'resources/blocks_order2.xlsx', 'path': './resources/blocks_order2.xlsx'}
  ]
});


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.0rc3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var instructionsClock;
var blocks_file;
var instructs_text;
var instruct_done;
var instr_done_button;
var instr_done_label;
var instr_done_touch;
var readyClock;
var main_ready_msg;
var button_L;
var ready_label_L;
var button_R;
var ready_label_R;
var ready_done_mouse;
var ready_done;
var trialClock;
var fixation;
var image_stim;
var text_stim;
var key_resp;
var touch_resp;
var button_left;
var trial_label_left;
var button_right;
var trial_label_right;
var feedbackClock;
var feedback_msg;
var end_thanksClock;
var thanks_text;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  if ((expInfo["order"] === "random")) {
      expInfo["order"] = (Math.floor((Math.random() * ((2 - 1) + 1))) + 1);
  }
  blocks_file = (("blocks_order" + expInfo["order"].toString()) + ".xlsx");
  
  instructs_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructs_text',
    text: 'default text',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  instruct_done = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instr_done_button = new visual.Rect ({
    win: psychoJS.window, name: 'instr_done_button', units : 'height', 
    width: [0.4, 0.1][0], height: [0.4, 0.1][1],
    ori: 0, pos: [0, (- 0.4)],
    lineWidth: 1, lineColor: new util.Color('darkgreen'),
    fillColor: new util.Color('lightgreen'),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  instr_done_label = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_done_label',
    text: 'Next...',
    font: 'Arial',
    units: 'height', 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('darkgreen'),  opacity: 1,
    depth: -4.0 
  });
  
  instr_done_touch = new core.Mouse({
    win: psychoJS.window,
  });
  instr_done_touch.mouseClock = new util.Clock();
  // Initialize components for Routine "ready"
  readyClock = new util.Clock();
  main_ready_msg = new visual.TextStim({
    win: psychoJS.window,
    name: 'main_ready_msg',
    text: 'Take note of the categories below\n \nPosition your index fingers \n \nPress the space bar (or one of the green buttons) to begin',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  button_L = new visual.Rect ({
    win: psychoJS.window, name: 'button_L', units : 'height', 
    width: [0.4, 0.2][0], height: [0.4, 0.2][1],
    ori: 0, pos: [(- 0.4), (- 0.3)],
    lineWidth: 1, lineColor: new util.Color('darkgreen'),
    fillColor: new util.Color('lightgreen'),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  ready_label_L = new visual.TextStim({
    win: psychoJS.window,
    name: 'ready_label_L',
    text: 'default text',
    font: 'Arial',
    units: 'height', 
    pos: [(- 0.4), (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('darkgreen'),  opacity: 1,
    depth: -2.0 
  });
  
  button_R = new visual.Rect ({
    win: psychoJS.window, name: 'button_R', units : 'height', 
    width: [0.4, 0.2][0], height: [0.4, 0.2][1],
    ori: 0, pos: [0.4, (- 0.3)],
    lineWidth: 1, lineColor: new util.Color('darkgreen'),
    fillColor: new util.Color('lightgreen'),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  ready_label_R = new visual.TextStim({
    win: psychoJS.window,
    name: 'ready_label_R',
    text: 'default text',
    font: 'Arial',
    units: 'height', 
    pos: [0.4, (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('darkgreen'),  opacity: 1,
    depth: -4.0 
  });
  
  ready_done_mouse = new core.Mouse({
    win: psychoJS.window,
  });
  ready_done_mouse.mouseClock = new util.Clock();
  ready_done = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation',
    text: '+',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  image_stim = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_stim', units : 'height', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  text_stim = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_stim',
    text: 'default text',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  touch_resp = new core.Mouse({
    win: psychoJS.window,
  });
  touch_resp.mouseClock = new util.Clock();
  button_left = new visual.Rect ({
    win: psychoJS.window, name: 'button_left', units : 'height', 
    width: [0.4, 0.2][0], height: [0.4, 0.2][1],
    ori: 0, pos: [(- 0.4), (- 0.3)],
    lineWidth: 1, lineColor: new util.Color('darkgreen'),
    fillColor: new util.Color('lightgreen'),
    opacity: 1, depth: -6, interpolate: true,
  });
  
  trial_label_left = new visual.TextStim({
    win: psychoJS.window,
    name: 'trial_label_left',
    text: 'default text',
    font: 'Arial',
    units: 'height', 
    pos: [(- 0.4), (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('darkgreen'),  opacity: 1,
    depth: -7.0 
  });
  
  button_right = new visual.Rect ({
    win: psychoJS.window, name: 'button_right', units : 'height', 
    width: [0.4, 0.2][0], height: [0.4, 0.2][1],
    ori: 0, pos: [0.4, (- 0.3)],
    lineWidth: 1, lineColor: new util.Color('darkgreen'),
    fillColor: new util.Color('lightgreen'),
    opacity: 1, depth: -8, interpolate: true,
  });
  
  trial_label_right = new visual.TextStim({
    win: psychoJS.window,
    name: 'trial_label_right',
    text: 'default text',
    font: 'Arial',
    units: 'height', 
    pos: [0.4, (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('darkgreen'),  opacity: 1,
    depth: -9.0 
  });
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  feedback_msg = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_msg',
    text: 'default text',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "end_thanks"
  end_thanksClock = new util.Clock();
  thanks_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'thanks_text',
    text: 'The End. \n \nThank you for your participation.',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var instruct_pages;
var currentLoop;
function instruct_pagesLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  instruct_pages = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'resources/instructs.xlsx',
    seed: undefined, name: 'instruct_pages'
  });
  psychoJS.experiment.addLoop(instruct_pages); // add the loop to the experiment
  currentLoop = instruct_pages;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisInstruct_page of instruct_pages) {
    const snapshot = instruct_pages.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(instructionsRoutineBegin(snapshot));
    thisScheduler.add(instructionsRoutineEachFrame(snapshot));
    thisScheduler.add(instructionsRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function instruct_pagesLoopEnd() {
  psychoJS.experiment.removeLoop(instruct_pages);

  return Scheduler.Event.NEXT;
}


var blocks;
function blocksLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  blocks = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: ('resources/' + blocks_file),
    seed: undefined, name: 'blocks'
  });
  psychoJS.experiment.addLoop(blocks); // add the loop to the experiment
  currentLoop = blocks;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisBlock of blocks) {
    const snapshot = blocks.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(readyRoutineBegin(snapshot));
    thisScheduler.add(readyRoutineEachFrame(snapshot));
    thisScheduler.add(readyRoutineEnd(snapshot));
    const trialsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(trialsLoopBegin, trialsLoopScheduler);
    thisScheduler.add(trialsLoopScheduler);
    thisScheduler.add(trialsLoopEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: ('resources/' + conds_file),
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    const snapshot = trials.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trialRoutineBegin(snapshot));
    thisScheduler.add(trialRoutineEachFrame(snapshot));
    thisScheduler.add(trialRoutineEnd(snapshot));
    thisScheduler.add(feedbackRoutineBegin(snapshot));
    thisScheduler.add(feedbackRoutineEachFrame(snapshot));
    thisScheduler.add(feedbackRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


function blocksLoopEnd() {
  psychoJS.experiment.removeLoop(blocks);

  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _instruct_done_allKeys;
var gotValidClick;
var instructionsComponents;
function instructionsRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'instructions'-------
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instructs_text.setText(instruct_text);
    instruct_done.keys = undefined;
    instruct_done.rt = undefined;
    _instruct_done_allKeys = [];
    // setup some python lists for storing info about the instr_done_touch
    instr_done_touch.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(instructs_text);
    instructionsComponents.push(instruct_done);
    instructionsComponents.push(instr_done_button);
    instructionsComponents.push(instr_done_label);
    instructionsComponents.push(instr_done_touch);
    
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
var prevButtonState;
function instructionsRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'instructions'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructs_text* updates
    if (t >= 0.0 && instructs_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructs_text.tStart = t;  // (not accounting for frame time here)
      instructs_text.frameNStart = frameN;  // exact frame index
      
      instructs_text.setAutoDraw(true);
    }

    
    // *instruct_done* updates
    if (t >= 0.0 && instruct_done.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruct_done.tStart = t;  // (not accounting for frame time here)
      instruct_done.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instruct_done.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instruct_done.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instruct_done.clearEvents(); });
    }

    if (instruct_done.status === PsychoJS.Status.STARTED) {
      let theseKeys = instruct_done.getKeys({keyList: ['space'], waitRelease: false});
      _instruct_done_allKeys = _instruct_done_allKeys.concat(theseKeys);
      if (_instruct_done_allKeys.length > 0) {
        instruct_done.keys = _instruct_done_allKeys[_instruct_done_allKeys.length - 1].name;  // just the last key pressed
        instruct_done.rt = _instruct_done_allKeys[_instruct_done_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *instr_done_button* updates
    if (t >= 0.0 && instr_done_button.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_done_button.tStart = t;  // (not accounting for frame time here)
      instr_done_button.frameNStart = frameN;  // exact frame index
      
      instr_done_button.setAutoDraw(true);
    }

    
    // *instr_done_label* updates
    if (t >= 0.0 && instr_done_label.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_done_label.tStart = t;  // (not accounting for frame time here)
      instr_done_label.frameNStart = frameN;  // exact frame index
      
      instr_done_label.setAutoDraw(true);
    }

    // *instr_done_touch* updates
    if (t >= 0.0 && instr_done_touch.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr_done_touch.tStart = t;  // (not accounting for frame time here)
      instr_done_touch.frameNStart = frameN;  // exact frame index
      
      instr_done_touch.status = PsychoJS.Status.STARTED;
      instr_done_touch.mouseClock.reset();
      prevButtonState = instr_done_touch.getPressed();  // if button is down already this ISN'T a new click
      }
    if (instr_done_touch.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = instr_done_touch.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [instr_done_button]) {
            if (obj.contains(instr_done_touch)) {
              gotValidClick = true;
              instr_done_touch.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'instructions'-------
    for (const thisComponent of instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    const xys = instr_done_touch.getPos();
    const buttons = instr_done_touch.getPressed();
    psychoJS.experiment.addData('instr_done_touch.x', xys[0]);
    psychoJS.experiment.addData('instr_done_touch.y', xys[1]);
    psychoJS.experiment.addData('instr_done_touch.leftButton', buttons[0]);
    psychoJS.experiment.addData('instr_done_touch.midButton', buttons[1]);
    psychoJS.experiment.addData('instr_done_touch.rightButton', buttons[2]);
    if (instr_done_touch.clicked_name.length > 0) {
      psychoJS.experiment.addData('instr_done_touch.clicked_name', instr_done_touch.clicked_name[0]);}
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _ready_done_allKeys;
var readyComponents;
function readyRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'ready'-------
    t = 0;
    readyClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    ready_label_L.setText(label_left);
    ready_label_R.setText(label_right);
    // setup some python lists for storing info about the ready_done_mouse
    ready_done_mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    ready_done.keys = undefined;
    ready_done.rt = undefined;
    _ready_done_allKeys = [];
    // keep track of which components have finished
    readyComponents = [];
    readyComponents.push(main_ready_msg);
    readyComponents.push(button_L);
    readyComponents.push(ready_label_L);
    readyComponents.push(button_R);
    readyComponents.push(ready_label_R);
    readyComponents.push(ready_done_mouse);
    readyComponents.push(ready_done);
    
    for (const thisComponent of readyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function readyRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'ready'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = readyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *main_ready_msg* updates
    if (t >= 0.0 && main_ready_msg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      main_ready_msg.tStart = t;  // (not accounting for frame time here)
      main_ready_msg.frameNStart = frameN;  // exact frame index
      
      main_ready_msg.setAutoDraw(true);
    }

    
    // *button_L* updates
    if (t >= 0.0 && button_L.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_L.tStart = t;  // (not accounting for frame time here)
      button_L.frameNStart = frameN;  // exact frame index
      
      button_L.setAutoDraw(true);
    }

    
    // *ready_label_L* updates
    if (t >= 0.0 && ready_label_L.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ready_label_L.tStart = t;  // (not accounting for frame time here)
      ready_label_L.frameNStart = frameN;  // exact frame index
      
      ready_label_L.setAutoDraw(true);
    }

    
    // *button_R* updates
    if (t >= 0.0 && button_R.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_R.tStart = t;  // (not accounting for frame time here)
      button_R.frameNStart = frameN;  // exact frame index
      
      button_R.setAutoDraw(true);
    }

    
    // *ready_label_R* updates
    if (t >= 0.0 && ready_label_R.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ready_label_R.tStart = t;  // (not accounting for frame time here)
      ready_label_R.frameNStart = frameN;  // exact frame index
      
      ready_label_R.setAutoDraw(true);
    }

    // *ready_done_mouse* updates
    if (t >= 0.0 && ready_done_mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ready_done_mouse.tStart = t;  // (not accounting for frame time here)
      ready_done_mouse.frameNStart = frameN;  // exact frame index
      
      ready_done_mouse.status = PsychoJS.Status.STARTED;
      ready_done_mouse.mouseClock.reset();
      prevButtonState = ready_done_mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (ready_done_mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = ready_done_mouse.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [button_L, button_R]) {
            if (obj.contains(ready_done_mouse)) {
              gotValidClick = true;
              ready_done_mouse.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *ready_done* updates
    if (t >= 0.0 && ready_done.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ready_done.tStart = t;  // (not accounting for frame time here)
      ready_done.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { ready_done.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { ready_done.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { ready_done.clearEvents(); });
    }

    if (ready_done.status === PsychoJS.Status.STARTED) {
      let theseKeys = ready_done.getKeys({keyList: ['space'], waitRelease: false});
      _ready_done_allKeys = _ready_done_allKeys.concat(theseKeys);
      if (_ready_done_allKeys.length > 0) {
        ready_done.keys = _ready_done_allKeys[_ready_done_allKeys.length - 1].name;  // just the last key pressed
        ready_done.rt = _ready_done_allKeys[_ready_done_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of readyComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function readyRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'ready'-------
    for (const thisComponent of readyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // store data for thisExp (ExperimentHandler)
    // the Routine "ready" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var trialComponents;
function trialRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    image_stim.setImage(stimImage);
    text_stim.setText(stimWord);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // setup some python lists for storing info about the touch_resp
    // current position of the mouse:
    touch_resp.x = [];
    touch_resp.y = [];
    touch_resp.leftButton = [];
    touch_resp.midButton = [];
    touch_resp.rightButton = [];
    touch_resp.time = [];
    touch_resp.clicked_name = [];
    gotValidClick = false; // until a click is received
    trial_label_left.setText(label_left);
    trial_label_right.setText(label_right);
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(fixation);
    trialComponents.push(image_stim);
    trialComponents.push(text_stim);
    trialComponents.push(key_resp);
    trialComponents.push(touch_resp);
    trialComponents.push(button_left);
    trialComponents.push(trial_label_left);
    trialComponents.push(button_right);
    trialComponents.push(trial_label_right);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function trialRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation* updates
    if (t >= 0.0 && fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation.tStart = t;  // (not accounting for frame time here)
      fixation.frameNStart = frameN;  // exact frame index
      
      fixation.setAutoDraw(true);
    }

    frameRemains = 0.5  - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation.setAutoDraw(false);
    }
    
    // *image_stim* updates
    if (t >= 0.5 && image_stim.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_stim.tStart = t;  // (not accounting for frame time here)
      image_stim.frameNStart = frameN;  // exact frame index
      
      image_stim.setAutoDraw(true);
    }

    
    // *text_stim* updates
    if (t >= 0.5 && text_stim.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_stim.tStart = t;  // (not accounting for frame time here)
      text_stim.frameNStart = frameN;  // exact frame index
      
      text_stim.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.5 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['a', 'l'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp.keys == CorrAns) {
            key_resp.corr = 1;
        } else {
            key_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *touch_resp* updates
    if (t >= 0.5 && touch_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      touch_resp.tStart = t;  // (not accounting for frame time here)
      touch_resp.frameNStart = frameN;  // exact frame index
      
      touch_resp.status = PsychoJS.Status.STARTED;
      touch_resp.mouseClock.reset();
      prevButtonState = touch_resp.getPressed();  // if button is down already this ISN'T a new click
      }
    if (touch_resp.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = touch_resp.getPressed();
      if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = buttons;
        if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          const xys = touch_resp.getPos();
          touch_resp.x.push(xys[0]);
          touch_resp.y.push(xys[1]);
          touch_resp.leftButton.push(buttons[0]);
          touch_resp.midButton.push(buttons[1]);
          touch_resp.rightButton.push(buttons[2]);
          touch_resp.time.push(touch_resp.mouseClock.getTime());
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [button_left, button_right]) {
            if (obj.contains(touch_resp)) {
              gotValidClick = true;
              touch_resp.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *button_left* updates
    if (t >= 0.5 && button_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_left.tStart = t;  // (not accounting for frame time here)
      button_left.frameNStart = frameN;  // exact frame index
      
      button_left.setAutoDraw(true);
    }

    
    // *trial_label_left* updates
    if (t >= 0.5 && trial_label_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_label_left.tStart = t;  // (not accounting for frame time here)
      trial_label_left.frameNStart = frameN;  // exact frame index
      
      trial_label_left.setAutoDraw(true);
    }

    
    // *button_right* updates
    if (t >= 0.5 && button_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button_right.tStart = t;  // (not accounting for frame time here)
      button_right.frameNStart = frameN;  // exact frame index
      
      button_right.setAutoDraw(true);
    }

    
    // *trial_label_right* updates
    if (t >= 0.5 && trial_label_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_label_right.tStart = t;  // (not accounting for frame time here)
      trial_label_right.frameNStart = frameN;  // exact frame index
      
      trial_label_right.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var corr;
var rt;
function trialRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'trial'-------
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (key_resp.keys === undefined) {
      if (['None','none',undefined].includes(CorrAns)) {
         key_resp.corr = 1;  // correct non-response
      } else {
         key_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    psychoJS.experiment.addData('key_resp.corr', key_resp.corr);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // store data for thisExp (ExperimentHandler)
    if (touch_resp.x) {  psychoJS.experiment.addData('touch_resp.x', touch_resp.x[0])};
    if (touch_resp.y) {  psychoJS.experiment.addData('touch_resp.y', touch_resp.y[0])};
    if (touch_resp.leftButton) {  psychoJS.experiment.addData('touch_resp.leftButton', touch_resp.leftButton[0])};
    if (touch_resp.midButton) {  psychoJS.experiment.addData('touch_resp.midButton', touch_resp.midButton[0])};
    if (touch_resp.rightButton) {  psychoJS.experiment.addData('touch_resp.rightButton', touch_resp.rightButton[0])};
    if (touch_resp.time) {  psychoJS.experiment.addData('touch_resp.time', touch_resp.time[0])};
    if (touch_resp.clicked_name) {  psychoJS.experiment.addData('touch_resp.clicked_name', touch_resp.clicked_name[0])};
    
    // check if correct (either mouse or keyboard)
    if (key_resp.keys !== undefined) {
        corr = key_resp.corr;
        rt = key_resp.rt;
    } else {
        rt = touch_resp.time[0];  // annoyingly mouse is a list of rts
        if ((touch_resp.clicked_name[0].includes('left') && CorrAns=='a') ||
            (touch_resp.clicked_name[0].includes('right') && CorrAns=='l')) {
            corr = 1;
        } else {
            corr = 0;
        }
    }
    
    psychoJS.experiment.addData('rt',  rt);
    psychoJS.experiment.addData('corr', corr);
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var msg;
var feedbackComponents;
function feedbackRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'feedback'-------
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    
    if (corr==0) {
        msg="oops";
    } else {
        msg="+"
    }
    
    feedback_msg.setText(msg);
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(feedback_msg);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function feedbackRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_msg* updates
    if (t >= 0.0 && feedback_msg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_msg.tStart = t;  // (not accounting for frame time here)
      feedback_msg.frameNStart = frameN;  // exact frame index
      
      feedback_msg.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_msg.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_msg.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'feedback'-------
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var end_thanksComponents;
function end_thanksRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'end_thanks'-------
    t = 0;
    end_thanksClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    end_thanksComponents = [];
    end_thanksComponents.push(thanks_text);
    
    for (const thisComponent of end_thanksComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function end_thanksRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'end_thanks'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = end_thanksClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *thanks_text* updates
    if (t >= 0.0 && thanks_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      thanks_text.tStart = t;  // (not accounting for frame time here)
      thanks_text.frameNStart = frameN;  // exact frame index
      
      thanks_text.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of end_thanksComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_thanksRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'end_thanks'-------
    for (const thisComponent of end_thanksComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "end_thanks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
