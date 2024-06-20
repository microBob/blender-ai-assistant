/****************** 
 * Choicertt Test *
 ******************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.1.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'choiceRTT';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([1, 1, 1]),
  units: 'height',
  waitBlanking: true
});
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
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
const PracticeLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(PracticeLoopLoopBegin(PracticeLoopLoopScheduler));
flowScheduler.add(PracticeLoopLoopScheduler);
flowScheduler.add(PracticeLoopLoopEnd);
flowScheduler.add(mainTrial_instructRoutineBegin());
flowScheduler.add(mainTrial_instructRoutineEachFrame());
flowScheduler.add(mainTrial_instructRoutineEnd());
const ExptLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(ExptLoopLoopBegin(ExptLoopLoopScheduler));
flowScheduler.add(ExptLoopLoopScheduler);
flowScheduler.add(ExptLoopLoopEnd);
flowScheduler.add(end_messageRoutineBegin());
flowScheduler.add(end_messageRoutineEachFrame());
flowScheduler.add(end_messageRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'RTtimeConditions.xlsx', 'path': 'RTtimeConditions.xlsx'},
    {'name': 'images/target_cross.jpg', 'path': 'images/target_cross.jpg'},
    {'name': 'images/target_plus.jpg', 'path': 'images/target_plus.jpg'},
    {'name': 'images/target_square.jpg', 'path': 'images/target_square.jpg'},
    {'name': 'RTtimeConditions.xlsx', 'path': 'RTtimeConditions.xlsx'},
    {'name': 'images/target_cross.jpg', 'path': 'images/target_cross.jpg'},
    {'name': 'images/target_plus.jpg', 'path': 'images/target_plus.jpg'},
    {'name': 'images/target_square.jpg', 'path': 'images/target_square.jpg'},
    {'name': 'images/response_square.jpg', 'path': 'images/response_square.jpg'},
    {'name': 'images/response_plus.jpg', 'path': 'images/response_plus.jpg'},
    {'name': 'images/response_cross.jpg', 'path': 'images/response_cross.jpg'},
    {'name': 'images/grey_square.jpg', 'path': 'images/grey_square.jpg'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'images/response_ready.jpg', 'path': 'images/response_ready.jpg'},
    {'name': 'images/target_I.jpg', 'path': 'images/target_I.jpg'},
    {'name': 'images/target_plus.jpg', 'path': 'images/target_plus.jpg'},
    {'name': 'images/target_square.jpg', 'path': 'images/target_square.jpg'},
    {'name': 'images/target_T.jpg', 'path': 'images/target_T.jpg'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.1.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);


  return Scheduler.Event.NEXT;
}


var instructionsClock;
var instr;
var startInst;
var startMouse;
var intro_square;
var intro_plus;
var intro_cross;
var trialClock;
var rightright_tile;
var right_tile;
var left_tile;
var leftleft_tile;
var square_button;
var plus_button;
var cross_button;
var targetImage;
var keyResp;
var mouseResp;
var trial_feedbackClock;
var text_fb;
var moveOnKeys;
var moveOnMouse;
var mainTrial_instructClock;
var main_trial_instruct;
var key_resp;
var mouse;
var ready_button;
var end_messageClock;
var end_text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr',
    text: 'In this task you will make a decision as to which shape you have seen.\n\nPress C or click cross for a cross\nPress V or click square for a square\nPress B or click plus for a plus\n\nFirst, we will have a quick practice.\n\nPush space bar or click / touch one of the buttons to begin.',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0.1], height: 0.035,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  startInst = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  startMouse = new core.Mouse({
    win: psychoJS.window,
  });
  startMouse.mouseClock = new util.Clock();
  intro_square = new visual.ImageStim({
    win : psychoJS.window,
    name : 'intro_square', units : undefined, 
    image : 'images/response_square.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, (- 0.25)], size : [0.2, 0.1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  intro_plus = new visual.ImageStim({
    win : psychoJS.window,
    name : 'intro_plus', units : undefined, 
    image : 'images/response_plus.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.25)], size : [0.2, 0.1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  intro_cross = new visual.ImageStim({
    win : psychoJS.window,
    name : 'intro_cross', units : undefined, 
    image : 'images/response_cross.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.25)], size : [0.2, 0.1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  rightright_tile = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rightright_tile', units : undefined, 
    image : 'images/grey_square.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.375, 0], size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  right_tile = new visual.ImageStim({
    win : psychoJS.window,
    name : 'right_tile', units : undefined, 
    image : 'images/grey_square.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.125, 0], size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  left_tile = new visual.ImageStim({
    win : psychoJS.window,
    name : 'left_tile', units : undefined, 
    image : 'images/grey_square.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.125), 0], size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  leftleft_tile = new visual.ImageStim({
    win : psychoJS.window,
    name : 'leftleft_tile', units : undefined, 
    image : 'images/grey_square.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.375), 0], size : [0.22, 0.22],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  square_button = new visual.ImageStim({
    win : psychoJS.window,
    name : 'square_button', units : undefined, 
    image : 'images/response_square.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, (- 0.25)], size : [0.2, 0.1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  plus_button = new visual.ImageStim({
    win : psychoJS.window,
    name : 'plus_button', units : undefined, 
    image : 'images/response_plus.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.25, (- 0.25)], size : [0.2, 0.1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  cross_button = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cross_button', units : undefined, 
    image : 'images/response_cross.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [(- 0.25), (- 0.25)], size : [0.2, 0.1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  targetImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'targetImage', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -8.0 
  });
  keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mouseResp = new core.Mouse({
    win: psychoJS.window,
  });
  mouseResp.mouseClock = new util.Clock();
  // Initialize components for Routine "trial_feedback"
  trial_feedbackClock = new util.Clock();
  text_fb = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_fb',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  moveOnKeys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  moveOnMouse = new core.Mouse({
    win: psychoJS.window,
  });
  moveOnMouse.mouseClock = new util.Clock();
  // Initialize components for Routine "mainTrial_instruct"
  mainTrial_instructClock = new util.Clock();
  main_trial_instruct = new visual.TextStim({
    win: psychoJS.window,
    name: 'main_trial_instruct',
    text: 'Well done, that’s the practice over!\n\nNow for the main experiment.\n\nClick / tap / press space to continue!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  ready_button = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ready_button', units : undefined, 
    image : 'images/response_ready.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, (- 0.25)], size : [0.2, 0.1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  // Initialize components for Routine "end_message"
  end_messageClock = new util.Clock();
  end_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_text',
    text: 'That’s the experiment finished!\n\nThanks for your time. You’ve earned a cup of tea.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _startInst_allKeys;
var gotValidClick;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions' ---
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    startInst.keys = undefined;
    startInst.rt = undefined;
    _startInst_allKeys = [];
    // setup some python lists for storing info about the startMouse
    gotValidClick = false; // until a click is received
    startMouse.mouseClock.reset();
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(instr);
    instructionsComponents.push(startInst);
    instructionsComponents.push(startMouse);
    instructionsComponents.push(intro_square);
    instructionsComponents.push(intro_plus);
    instructionsComponents.push(intro_cross);
    
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
function instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions' ---
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr* updates
    if (t >= 0.0 && instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr.tStart = t;  // (not accounting for frame time here)
      instr.frameNStart = frameN;  // exact frame index
      
      instr.setAutoDraw(true);
    }

    
    // *startInst* updates
    if (t >= 0.0 && startInst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startInst.tStart = t;  // (not accounting for frame time here)
      startInst.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startInst.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startInst.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startInst.clearEvents(); });
    }

    if (startInst.status === PsychoJS.Status.STARTED) {
      let theseKeys = startInst.getKeys({keyList: [], waitRelease: false});
      _startInst_allKeys = _startInst_allKeys.concat(theseKeys);
      if (_startInst_allKeys.length > 0) {
        startInst.keys = _startInst_allKeys[_startInst_allKeys.length - 1].name;  // just the last key pressed
        startInst.rt = _startInst_allKeys[_startInst_allKeys.length - 1].rt;
        startInst.duration = _startInst_allKeys[_startInst_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *startMouse* updates
    if (t >= 0.0 && startMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startMouse.tStart = t;  // (not accounting for frame time here)
      startMouse.frameNStart = frameN;  // exact frame index
      
      startMouse.status = PsychoJS.Status.STARTED;
      prevButtonState = startMouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (startMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = startMouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    
    // *intro_square* updates
    if (t >= 0 && intro_square.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_square.tStart = t;  // (not accounting for frame time here)
      intro_square.frameNStart = frameN;  // exact frame index
      
      intro_square.setAutoDraw(true);
    }

    
    // *intro_plus* updates
    if (t >= 0 && intro_plus.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_plus.tStart = t;  // (not accounting for frame time here)
      intro_plus.frameNStart = frameN;  // exact frame index
      
      intro_plus.setAutoDraw(true);
    }

    
    // *intro_cross* updates
    if (t >= 0 && intro_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_cross.tStart = t;  // (not accounting for frame time here)
      intro_cross.frameNStart = frameN;  // exact frame index
      
      intro_cross.setAutoDraw(true);
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


function instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions' ---
    for (const thisComponent of instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    startInst.stop();
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var PracticeLoop;
function PracticeLoopLoopBegin(PracticeLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    PracticeLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'RTtimeConditions.xlsx',
      seed: undefined, name: 'PracticeLoop'
    });
    psychoJS.experiment.addLoop(PracticeLoop); // add the loop to the experiment
    currentLoop = PracticeLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPracticeLoop of PracticeLoop) {
      snapshot = PracticeLoop.getSnapshot();
      PracticeLoopLoopScheduler.add(importConditions(snapshot));
      PracticeLoopLoopScheduler.add(trialRoutineBegin(snapshot));
      PracticeLoopLoopScheduler.add(trialRoutineEachFrame());
      PracticeLoopLoopScheduler.add(trialRoutineEnd(snapshot));
      PracticeLoopLoopScheduler.add(trial_feedbackRoutineBegin(snapshot));
      PracticeLoopLoopScheduler.add(trial_feedbackRoutineEachFrame());
      PracticeLoopLoopScheduler.add(trial_feedbackRoutineEnd(snapshot));
      PracticeLoopLoopScheduler.add(PracticeLoopLoopEndIteration(PracticeLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function PracticeLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(PracticeLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function PracticeLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var ExptLoop;
function ExptLoopLoopBegin(ExptLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    ExptLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'RTtimeConditions.xlsx',
      seed: undefined, name: 'ExptLoop'
    });
    psychoJS.experiment.addLoop(ExptLoop); // add the loop to the experiment
    currentLoop = ExptLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisExptLoop of ExptLoop) {
      snapshot = ExptLoop.getSnapshot();
      ExptLoopLoopScheduler.add(importConditions(snapshot));
      ExptLoopLoopScheduler.add(trialRoutineBegin(snapshot));
      ExptLoopLoopScheduler.add(trialRoutineEachFrame());
      ExptLoopLoopScheduler.add(trialRoutineEnd(snapshot));
      ExptLoopLoopScheduler.add(ExptLoopLoopEndIteration(ExptLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function ExptLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(ExptLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function ExptLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var positionList;
var targetX;
var corrAns;
var corrButton;
var corrButtonName;
var _keyResp_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from setStimuli
    positionList = [(- 0.375), (- 0.125), 0.125, 0.375];
    util.shuffle(positionList);
    targetX = positionList[0];
    if ((thisImage === "images/target_square.jpg")) {
        corrAns = "v";
        corrButton = square_button;
        corrButtonName = "square_button";
    } else {
        if ((thisImage === "images/target_cross.jpg")) {
            corrAns = "c";
            corrButton = cross_button;
            corrButtonName = "cross_button";
        } else {
            if ((thisImage === "images/target_plus.jpg")) {
                corrAns = "b";
                corrButton = plus_button;
                corrButtonName = "plus_button";
            }
        }
    }
    
    targetImage.setPos([targetX, 0]);
    targetImage.setImage(thisImage);
    keyResp.keys = undefined;
    keyResp.rt = undefined;
    _keyResp_allKeys = [];
    // setup some python lists for storing info about the mouseResp
    // current position of the mouse:
    mouseResp.x = [];
    mouseResp.y = [];
    mouseResp.leftButton = [];
    mouseResp.midButton = [];
    mouseResp.rightButton = [];
    mouseResp.time = [];
    mouseResp.clicked_name = [];
    gotValidClick = false; // until a click is received
    mouseResp.mouseClock.reset();
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(rightright_tile);
    trialComponents.push(right_tile);
    trialComponents.push(left_tile);
    trialComponents.push(leftleft_tile);
    trialComponents.push(square_button);
    trialComponents.push(plus_button);
    trialComponents.push(cross_button);
    trialComponents.push(targetImage);
    trialComponents.push(keyResp);
    trialComponents.push(mouseResp);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
var _mouseXYs;
function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rightright_tile* updates
    if (t >= 0.5 && rightright_tile.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rightright_tile.tStart = t;  // (not accounting for frame time here)
      rightright_tile.frameNStart = frameN;  // exact frame index
      
      rightright_tile.setAutoDraw(true);
    }

    
    // *right_tile* updates
    if (t >= 0.5 && right_tile.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right_tile.tStart = t;  // (not accounting for frame time here)
      right_tile.frameNStart = frameN;  // exact frame index
      
      right_tile.setAutoDraw(true);
    }

    
    // *left_tile* updates
    if (t >= 0.5 && left_tile.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      left_tile.tStart = t;  // (not accounting for frame time here)
      left_tile.frameNStart = frameN;  // exact frame index
      
      left_tile.setAutoDraw(true);
    }

    
    // *leftleft_tile* updates
    if (t >= 0.5 && leftleft_tile.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      leftleft_tile.tStart = t;  // (not accounting for frame time here)
      leftleft_tile.frameNStart = frameN;  // exact frame index
      
      leftleft_tile.setAutoDraw(true);
    }

    
    // *square_button* updates
    if (t >= 0 && square_button.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      square_button.tStart = t;  // (not accounting for frame time here)
      square_button.frameNStart = frameN;  // exact frame index
      
      square_button.setAutoDraw(true);
    }

    
    // *plus_button* updates
    if (t >= 0 && plus_button.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      plus_button.tStart = t;  // (not accounting for frame time here)
      plus_button.frameNStart = frameN;  // exact frame index
      
      plus_button.setAutoDraw(true);
    }

    
    // *cross_button* updates
    if (t >= 0 && cross_button.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cross_button.tStart = t;  // (not accounting for frame time here)
      cross_button.frameNStart = frameN;  // exact frame index
      
      cross_button.setAutoDraw(true);
    }

    
    // *targetImage* updates
    if (t >= onsetTime && targetImage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      targetImage.tStart = t;  // (not accounting for frame time here)
      targetImage.frameNStart = frameN;  // exact frame index
      
      targetImage.setAutoDraw(true);
    }

    frameRemains = onsetTime + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (targetImage.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      targetImage.setAutoDraw(false);
    }
    
    // *keyResp* updates
    if (t >= 0 && keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyResp.tStart = t;  // (not accounting for frame time here)
      keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      keyResp.clock.reset();
      keyResp.start();
      keyResp.clearEvents();
    }

    if (keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyResp.getKeys({keyList: ['b', 'c', 'v'], waitRelease: false});
      _keyResp_allKeys = _keyResp_allKeys.concat(theseKeys);
      if (_keyResp_allKeys.length > 0) {
        keyResp.keys = _keyResp_allKeys[_keyResp_allKeys.length - 1].name;  // just the last key pressed
        keyResp.rt = _keyResp_allKeys[_keyResp_allKeys.length - 1].rt;
        keyResp.duration = _keyResp_allKeys[_keyResp_allKeys.length - 1].duration;
        // was this correct?
        if (keyResp.keys == corrAns) {
            keyResp.corr = 1;
        } else {
            keyResp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *mouseResp* updates
    if (t >= 0 && mouseResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouseResp.tStart = t;  // (not accounting for frame time here)
      mouseResp.frameNStart = frameN;  // exact frame index
      
      mouseResp.status = PsychoJS.Status.STARTED;
      prevButtonState = mouseResp.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouseResp.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouseResp.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [square_button, plus_button, cross_button]) {
            if (obj.contains(mouseResp)) {
              gotValidClick = true;
              mouseResp.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouseResp.getPos();
          mouseResp.x.push(_mouseXYs[0]);
          mouseResp.y.push(_mouseXYs[1]);
          mouseResp.leftButton.push(_mouseButtons[0]);
          mouseResp.midButton.push(_mouseButtons[1]);
          mouseResp.rightButton.push(_mouseButtons[2]);
          mouseResp.time.push(mouseResp.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
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


var thisRoutineDuration;
var thisRespType;
var thisRecRT;
var thisAcc;
function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (keyResp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         keyResp.corr = 1;  // correct non-response
      } else {
         keyResp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(keyResp.corr, level);
    }
    psychoJS.experiment.addData('keyResp.keys', keyResp.keys);
    psychoJS.experiment.addData('keyResp.corr', keyResp.corr);
    if (typeof keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyResp.rt', keyResp.rt);
        psychoJS.experiment.addData('keyResp.duration', keyResp.duration);
        routineTimer.reset();
        }
    
    keyResp.stop();
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouseResp.x) {  psychoJS.experiment.addData('mouseResp.x', mouseResp.x[0])};
    if (mouseResp.y) {  psychoJS.experiment.addData('mouseResp.y', mouseResp.y[0])};
    if (mouseResp.leftButton) {  psychoJS.experiment.addData('mouseResp.leftButton', mouseResp.leftButton[0])};
    if (mouseResp.midButton) {  psychoJS.experiment.addData('mouseResp.midButton', mouseResp.midButton[0])};
    if (mouseResp.rightButton) {  psychoJS.experiment.addData('mouseResp.rightButton', mouseResp.rightButton[0])};
    if (mouseResp.time) {  psychoJS.experiment.addData('mouseResp.time', mouseResp.time[0])};
    if (mouseResp.clicked_name) {  psychoJS.experiment.addData('mouseResp.clicked_name', mouseResp.clicked_name[0])};
    
    // Run 'End Routine' code from recordRTandAccuracy
    thisRoutineDuration = t;
    if (keyResp.keys) {
        thisRespType = "keyboard";
        thisRecRT = (keyResp.rt - onsetTime);
        if ((keyResp.corr === 1)) {
            thisAcc = "correct";
        } else {
            thisAcc = "incorrect";
        }
    } else {
        thisRespType = "mouse";
        thisRecRT = (mouseResp.time[0] - onsetTime);
        if ((mouseResp.clicked_name[0] === corrButtonName)) {
            thisAcc = "correct";
            psychoJS.experiment.addData("correctMouseResp", 1);
        } else {
            thisAcc = "incorrect";
            psychoJS.experiment.addData("correctMouseResp", 0);
        }
    }
    psychoJS.experiment.addData("trialRespTimes", thisRecRT);
    
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _moveOnKeys_allKeys;
var trial_feedbackComponents;
function trial_feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial_feedback' ---
    t = 0;
    trial_feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_fb.setText((((((((("The duration of the last routine was: " + util.round(thisRoutineDuration, 3).toString()) + " \nThe last recorded RT was: ") + util.round(thisRecRT, 3).toString()) + " \nThe response type was: ") + thisRespType) + " \nThe response was: ") + thisAcc) + " \n\nPress or click to continue."));
    moveOnKeys.keys = undefined;
    moveOnKeys.rt = undefined;
    _moveOnKeys_allKeys = [];
    // setup some python lists for storing info about the moveOnMouse
    gotValidClick = false; // until a click is received
    moveOnMouse.mouseClock.reset();
    // keep track of which components have finished
    trial_feedbackComponents = [];
    trial_feedbackComponents.push(text_fb);
    trial_feedbackComponents.push(moveOnKeys);
    trial_feedbackComponents.push(moveOnMouse);
    
    for (const thisComponent of trial_feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trial_feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial_feedback' ---
    // get current time
    t = trial_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_fb* updates
    if (t >= 0.0 && text_fb.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_fb.tStart = t;  // (not accounting for frame time here)
      text_fb.frameNStart = frameN;  // exact frame index
      
      text_fb.setAutoDraw(true);
    }

    
    // *moveOnKeys* updates
    if (t >= 0.0 && moveOnKeys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      moveOnKeys.tStart = t;  // (not accounting for frame time here)
      moveOnKeys.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { moveOnKeys.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { moveOnKeys.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { moveOnKeys.clearEvents(); });
    }

    if (moveOnKeys.status === PsychoJS.Status.STARTED) {
      let theseKeys = moveOnKeys.getKeys({keyList: ['c', 'v', 'b', 'space'], waitRelease: false});
      _moveOnKeys_allKeys = _moveOnKeys_allKeys.concat(theseKeys);
      if (_moveOnKeys_allKeys.length > 0) {
        moveOnKeys.keys = _moveOnKeys_allKeys[_moveOnKeys_allKeys.length - 1].name;  // just the last key pressed
        moveOnKeys.rt = _moveOnKeys_allKeys[_moveOnKeys_allKeys.length - 1].rt;
        moveOnKeys.duration = _moveOnKeys_allKeys[_moveOnKeys_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *moveOnMouse* updates
    if (t >= 0.0 && moveOnMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      moveOnMouse.tStart = t;  // (not accounting for frame time here)
      moveOnMouse.frameNStart = frameN;  // exact frame index
      
      moveOnMouse.status = PsychoJS.Status.STARTED;
      prevButtonState = moveOnMouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (moveOnMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = moveOnMouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // end routine on response
          continueRoutine = false;
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
    for (const thisComponent of trial_feedbackComponents)
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


function trial_feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial_feedback' ---
    for (const thisComponent of trial_feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(moveOnKeys.corr, level);
    }
    psychoJS.experiment.addData('moveOnKeys.keys', moveOnKeys.keys);
    if (typeof moveOnKeys.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('moveOnKeys.rt', moveOnKeys.rt);
        psychoJS.experiment.addData('moveOnKeys.duration', moveOnKeys.duration);
        routineTimer.reset();
        }
    
    moveOnKeys.stop();
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "trial_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_allKeys;
var mainTrial_instructComponents;
function mainTrial_instructRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'mainTrial_instruct' ---
    t = 0;
    mainTrial_instructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // setup some python lists for storing info about the mouse
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    mainTrial_instructComponents = [];
    mainTrial_instructComponents.push(main_trial_instruct);
    mainTrial_instructComponents.push(key_resp);
    mainTrial_instructComponents.push(mouse);
    mainTrial_instructComponents.push(ready_button);
    
    for (const thisComponent of mainTrial_instructComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function mainTrial_instructRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'mainTrial_instruct' ---
    // get current time
    t = mainTrial_instructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *main_trial_instruct* updates
    if (t >= 0.5 && main_trial_instruct.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      main_trial_instruct.tStart = t;  // (not accounting for frame time here)
      main_trial_instruct.frameNStart = frameN;  // exact frame index
      
      main_trial_instruct.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['y', 'n', 'left', 'right', 'space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    
    // *ready_button* updates
    if (t >= 1 && ready_button.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ready_button.tStart = t;  // (not accounting for frame time here)
      ready_button.frameNStart = frameN;  // exact frame index
      
      ready_button.setAutoDraw(true);
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
    for (const thisComponent of mainTrial_instructComponents)
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


function mainTrial_instructRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'mainTrial_instruct' ---
    for (const thisComponent of mainTrial_instructComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse.getPos();
    _mouseButtons = mouse.getPressed();
    psychoJS.experiment.addData('mouse.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse.rightButton', _mouseButtons[2]);
    // the Routine "mainTrial_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var end_messageComponents;
function end_messageRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end_message' ---
    t = 0;
    end_messageClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    end_messageComponents = [];
    end_messageComponents.push(end_text);
    
    for (const thisComponent of end_messageComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function end_messageRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end_message' ---
    // get current time
    t = end_messageClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_text* updates
    if (t >= 0.5 && end_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_text.tStart = t;  // (not accounting for frame time here)
      end_text.frameNStart = frameN;  // exact frame index
      
      end_text.setAutoDraw(true);
    }

    frameRemains = 0.5 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_text.setAutoDraw(false);
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
    for (const thisComponent of end_messageComponents)
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


function end_messageRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end_message' ---
    for (const thisComponent of end_messageComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
