/******************************* 
 * Attention_Network_Task *
 *******************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.2.2.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'attention_network_task';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
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
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
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
flowScheduler.add(instrRoutineBegin());
flowScheduler.add(instrRoutineEachFrame());
flowScheduler.add(instrRoutineEnd());
flowScheduler.add(instr2RoutineBegin());
flowScheduler.add(instr2RoutineEachFrame());
flowScheduler.add(instr2RoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);




flowScheduler.add(EndRoutineBegin());
flowScheduler.add(EndRoutineEachFrame());
flowScheduler.add(EndRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'cond.xlsx', 'path': 'cond.xlsx'},
    {'name': 'stim/upper.png', 'path': 'stim/upper.png'},
    {'name': 'stim/congLeft.png', 'path': 'stim/congLeft.png'},
    {'name': 'stim/both.png', 'path': 'stim/both.png'},
    {'name': 'stim/centre.png', 'path': 'stim/centre.png'},
    {'name': 'stim/blank.png', 'path': 'stim/blank.png'},
    {'name': 'stim/lower.png', 'path': 'stim/lower.png'},
    {'name': 'stim/congRight.png', 'path': 'stim/congRight.png'},
    {'name': 'stim/incongLeft.png', 'path': 'stim/incongLeft.png'},
    {'name': 'stim/incongRight.png', 'path': 'stim/incongRight.png'},
    {'name': 'stim/neutralLeft.png', 'path': 'stim/neutralLeft.png'},
    {'name': 'stim/neutralRight.png', 'path': 'stim/neutralRight.png'},
    {'name': 'background.png', 'path': 'background.png'},
    {'name': 'stim/fix.png', 'path': 'stim/fix.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.2';
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
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var instrClock;
var background;
var startresp;
var inst1textbox;
var instr2Clock;
var background_2;
var startresp2;
var inst1textbox_2;
var fixationClock;
var background_3;
var durations;
var image;
var trial_counter_2;
var reminder;
var trialClock;
var background_4;
var cues;
var target;
var resp;
var fixationshort;
var trial_counter;
var reminder_2;
var feedbackClock;
var background_5;
var msg;
var correct_count;
var text;
var trial_counter_3;
var reminder_3;
var EndClock;
var background_6;
var inst1textbox_3;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "instr"
  instrClock = new util.Clock();
  background = new visual.ImageStim({
    win : psychoJS.window,
    name : 'background', units : undefined, 
    image : 'background.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 1.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  startresp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  inst1textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'inst1textbox',
    text: 'Welcome to this experiment.\n\nIn this task, you will be presented with a central arrow surrounded by arrows or blocks. The central arrow will point left or right.\n\nSometimes the flanking arrows will be pointing in the same direction as the central arrow, and sometimes the flanking arrows will point in the oppoiste direction to the central arrow.\n\neg. >>>>> or >><>>\n\nYour task is to respond to the direction of the central arrow.\n\nIf the central arrow points to the right, press the right arrow key and if the arrow points to the left, press the left arrow key.\n\nPress the space bar to continue.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1.1, 0.9],  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: 0.8,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  // Initialize components for Routine "instr2"
  instr2Clock = new util.Clock();
  background_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'background_2', units : undefined, 
    image : 'background.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 1.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  startresp2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  inst1textbox_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'inst1textbox_2',
    text: 'In this task, you must respond to the direction of the centre arrow using the arrow keys.\n\nFirst, a fixation cross will appear in the centre of the screen. The fixation is sometimes followed by blocks on the screen, which may or may not\ncue the location of the target stimulus. If the blocks appear after the fixation, it means that the target will appear shortly.\n\nIf the blocks appears either above OR below the fixation cross, the target will shortly appear in that cued location.\n\n\nPlace your index fingers on the left and right keys ready to start, and press the spacebar to proceed.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1.1, 0.9],  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: 0.8,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  background_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'background_3', units : undefined, 
    image : 'background.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 1.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Run 'Begin Experiment' code from fix_dur_code
  durations = [0.4, 0.45, 0.5, 0.55];
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : 'height', 
    image : 'stim/fix.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  trial_counter_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'trial_counter_2',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, (- 0.45)], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.1],  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: 0.8,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -3.0 
  });
  
  reminder = new visual.TextBox({
    win: psychoJS.window,
    name: 'reminder',
    text: 'Respond to the direction of the central arrow using the left and right keys on your keyboard.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.4], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1, 0.2],  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -4.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  background_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'background_4', units : undefined, 
    image : 'background.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 1.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  cues = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cues', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  target = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, pos : [0, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  fixationshort = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fixationshort', units : 'height', 
    image : 'stim/fix.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  trial_counter = new visual.TextBox({
    win: psychoJS.window,
    name: 'trial_counter',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, (- 0.45)], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.1],  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: 0.8,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -5.0 
  });
  
  reminder_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'reminder_2',
    text: 'Respond to the direction of the central arrow using the left and right keys on your keyboard.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.4], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1, 0.2],  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -6.0 
  });
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  background_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'background_5', units : undefined, 
    image : 'background.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 1.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Run 'Begin Experiment' code from fb_code
  msg = "";
  correct_count = 0;
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  trial_counter_3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'trial_counter_3',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, (- 0.45)], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.1],  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: 0.8,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -3.0 
  });
  
  reminder_3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'reminder_3',
    text: 'Respond to the direction of the central arrow using the left and right keys on your keyboard.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.4], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1, 0.2],  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -4.0 
  });
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  background_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'background_6', units : undefined, 
    image : 'background.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [2, 1.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  inst1textbox_3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'inst1textbox_3',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1.1, 0.9],  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: 0.8,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _startresp_allKeys;
var instrComponents;
function instrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instr' ---
    t = 0;
    instrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instr.started', globalClock.getTime());
    startresp.keys = undefined;
    startresp.rt = undefined;
    _startresp_allKeys = [];
    // keep track of which components have finished
    instrComponents = [];
    instrComponents.push(background);
    instrComponents.push(startresp);
    instrComponents.push(inst1textbox);
    
    for (const thisComponent of instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instr' ---
    // get current time
    t = instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *background* updates
    if (t >= 0.0 && background.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      background.tStart = t;  // (not accounting for frame time here)
      background.frameNStart = frameN;  // exact frame index
      
      background.setAutoDraw(true);
    }
    
    
    // *startresp* updates
    if (t >= 0.0 && startresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startresp.tStart = t;  // (not accounting for frame time here)
      startresp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startresp.clearEvents(); });
    }
    
    if (startresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = startresp.getKeys({keyList: ['space'], waitRelease: false});
      _startresp_allKeys = _startresp_allKeys.concat(theseKeys);
      if (_startresp_allKeys.length > 0) {
        startresp.keys = _startresp_allKeys[_startresp_allKeys.length - 1].name;  // just the last key pressed
        startresp.rt = _startresp_allKeys[_startresp_allKeys.length - 1].rt;
        startresp.duration = _startresp_allKeys[_startresp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *inst1textbox* updates
    if (t >= 0.0 && inst1textbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inst1textbox.tStart = t;  // (not accounting for frame time here)
      inst1textbox.frameNStart = frameN;  // exact frame index
      
      inst1textbox.setAutoDraw(true);
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
    for (const thisComponent of instrComponents)
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


function instrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instr' ---
    for (const thisComponent of instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instr.stopped', globalClock.getTime());
    startresp.stop();
    // the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _startresp2_allKeys;
var instr2Components;
function instr2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instr2' ---
    t = 0;
    instr2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instr2.started', globalClock.getTime());
    startresp2.keys = undefined;
    startresp2.rt = undefined;
    _startresp2_allKeys = [];
    // keep track of which components have finished
    instr2Components = [];
    instr2Components.push(background_2);
    instr2Components.push(startresp2);
    instr2Components.push(inst1textbox_2);
    
    for (const thisComponent of instr2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instr2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instr2' ---
    // get current time
    t = instr2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *background_2* updates
    if (t >= 0.0 && background_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      background_2.tStart = t;  // (not accounting for frame time here)
      background_2.frameNStart = frameN;  // exact frame index
      
      background_2.setAutoDraw(true);
    }
    
    
    // *startresp2* updates
    if (t >= 0.0 && startresp2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startresp2.tStart = t;  // (not accounting for frame time here)
      startresp2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startresp2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startresp2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startresp2.clearEvents(); });
    }
    
    if (startresp2.status === PsychoJS.Status.STARTED) {
      let theseKeys = startresp2.getKeys({keyList: ['space'], waitRelease: false});
      _startresp2_allKeys = _startresp2_allKeys.concat(theseKeys);
      if (_startresp2_allKeys.length > 0) {
        startresp2.keys = _startresp2_allKeys[_startresp2_allKeys.length - 1].name;  // just the last key pressed
        startresp2.rt = _startresp2_allKeys[_startresp2_allKeys.length - 1].rt;
        startresp2.duration = _startresp2_allKeys[_startresp2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *inst1textbox_2* updates
    if (t >= 0.0 && inst1textbox_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inst1textbox_2.tStart = t;  // (not accounting for frame time here)
      inst1textbox_2.frameNStart = frameN;  // exact frame index
      
      inst1textbox_2.setAutoDraw(true);
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
    for (const thisComponent of instr2Components)
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


function instr2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instr2' ---
    for (const thisComponent of instr2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instr2.stopped', globalClock.getTime());
    startresp2.stop();
    // the Routine "instr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'cond.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(fixationRoutineBegin(snapshot));
      trialsLoopScheduler.add(fixationRoutineEachFrame());
      trialsLoopScheduler.add(fixationRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
      trialsLoopScheduler.add(feedbackRoutineEachFrame());
      trialsLoopScheduler.add(feedbackRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
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


var fixDuration;
var fixationComponents;
function fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation' ---
    t = 0;
    fixationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('fixation.started', globalClock.getTime());
    // Run 'Begin Routine' code from fix_dur_code
    util.shuffle(durations);
    fixDuration = durations[0];
    
    trial_counter_2.setText((((trials.thisN + 1).toString() + "/") + trials.nTotal.toString()));
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(background_3);
    fixationComponents.push(image);
    fixationComponents.push(trial_counter_2);
    fixationComponents.push(reminder);
    
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function fixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation' ---
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *background_3* updates
    if (t >= 0.0 && background_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      background_3.tStart = t;  // (not accounting for frame time here)
      background_3.frameNStart = frameN;  // exact frame index
      
      background_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + fixDuration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (background_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      background_3.setAutoDraw(false);
    }
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + fixDuration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image.setAutoDraw(false);
    }
    
    // *trial_counter_2* updates
    if (t >= 0.0 && trial_counter_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_counter_2.tStart = t;  // (not accounting for frame time here)
      trial_counter_2.frameNStart = frameN;  // exact frame index
      
      trial_counter_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + fixDuration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial_counter_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_counter_2.setAutoDraw(false);
    }
    
    // *reminder* updates
    if (t >= 0.0 && reminder.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reminder.tStart = t;  // (not accounting for frame time here)
      reminder.frameNStart = frameN;  // exact frame index
      
      reminder.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + fixDuration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (reminder.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      reminder.setAutoDraw(false);
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
    for (const thisComponent of fixationComponents)
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


function fixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation' ---
    for (const thisComponent of fixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('fixation.stopped', globalClock.getTime());
    // Run 'End Routine' code from fix_dur_code
    psychoJS.experiment.addData("fixDuration", fixDuration);
    
    // the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _resp_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.200000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    cues.setImage(cue);
    target.setOri(targOrientation);
    target.setImage(tar);
    resp.keys = undefined;
    resp.rt = undefined;
    _resp_allKeys = [];
    trial_counter.setText((((trials.thisN + 1).toString() + "/") + trials.nTotal.toString()));
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(background_4);
    trialComponents.push(cues);
    trialComponents.push(target);
    trialComponents.push(resp);
    trialComponents.push(fixationshort);
    trialComponents.push(trial_counter);
    trialComponents.push(reminder_2);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *background_4* updates
    if (t >= 0.0 && background_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      background_4.tStart = t;  // (not accounting for frame time here)
      background_4.frameNStart = frameN;  // exact frame index
      
      background_4.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (background_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      background_4.setAutoDraw(false);
    }
    
    // *cues* updates
    if (t >= 0 && cues.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cues.tStart = t;  // (not accounting for frame time here)
      cues.frameNStart = frameN;  // exact frame index
      
      cues.setAutoDraw(true);
    }
    
    frameRemains = 0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cues.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cues.setAutoDraw(false);
    }
    
    // *target* updates
    if (t >= 0.5 && target.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target.tStart = t;  // (not accounting for frame time here)
      target.frameNStart = frameN;  // exact frame index
      
      target.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 1.7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (target.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      target.setAutoDraw(false);
    }
    
    // *resp* updates
    if (t >= 0.5 && resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp.tStart = t;  // (not accounting for frame time here)
      resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp.clearEvents(); });
    }
    
    frameRemains = 0.5 + 1.7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _resp_allKeys = _resp_allKeys.concat(theseKeys);
      if (_resp_allKeys.length > 0) {
        resp.keys = _resp_allKeys[0].name;  // just the first key pressed
        resp.rt = _resp_allKeys[0].rt;
        resp.duration = _resp_allKeys[0].duration;
        // was this correct?
        if (resp.keys == corrAns) {
            resp.corr = 1;
        } else {
            resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *fixationshort* updates
    if (t >= 0.0 && fixationshort.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixationshort.tStart = t;  // (not accounting for frame time here)
      fixationshort.frameNStart = frameN;  // exact frame index
      
      fixationshort.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixationshort.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixationshort.setAutoDraw(false);
    }
    
    // *trial_counter* updates
    if (t >= 0.0 && trial_counter.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_counter.tStart = t;  // (not accounting for frame time here)
      trial_counter.frameNStart = frameN;  // exact frame index
      
      trial_counter.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial_counter.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_counter.setAutoDraw(false);
    }
    
    // *reminder_2* updates
    if (t >= 0.0 && reminder_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reminder_2.tStart = t;  // (not accounting for frame time here)
      reminder_2.frameNStart = frameN;  // exact frame index
      
      reminder_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (reminder_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      reminder_2.setAutoDraw(false);
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
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (resp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         resp.corr = 1;  // correct non-response
      } else {
         resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp.corr, level);
    }
    psychoJS.experiment.addData('resp.keys', resp.keys);
    psychoJS.experiment.addData('resp.corr', resp.corr);
    if (typeof resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp.rt', resp.rt);
        psychoJS.experiment.addData('resp.duration', resp.duration);
        routineTimer.reset();
        }
    
    resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var fbcol;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('feedback.started', globalClock.getTime());
    // Run 'Begin Routine' code from fb_code
    msg = "Incorrect!";
    fbcol = "black";
    if (resp.corr) {
        msg = (("Correct! Your RT is : " + Number.parseInt((resp.rt * 1000)).toString()) + "ms");
        correct_count += 1;
        fbcol = "green";
    } else {
        if ((! resp.keys)) {
            msg = "Remember to respond!";
        }
    }
    
    text.setColor(new util.Color(fbcol));
    text.setText(msg);
    trial_counter_3.setText((((trials.thisN + 1).toString() + "/") + trials.nTotal.toString()));
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(background_5);
    feedbackComponents.push(text);
    feedbackComponents.push(trial_counter_3);
    feedbackComponents.push(reminder_3);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *background_5* updates
    if (t >= 0.0 && background_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      background_5.tStart = t;  // (not accounting for frame time here)
      background_5.frameNStart = frameN;  // exact frame index
      
      background_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (background_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      background_5.setAutoDraw(false);
    }
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    
    // *trial_counter_3* updates
    if (t >= 0.0 && trial_counter_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_counter_3.tStart = t;  // (not accounting for frame time here)
      trial_counter_3.frameNStart = frameN;  // exact frame index
      
      trial_counter_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial_counter_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_counter_3.setAutoDraw(false);
    }
    
    // *reminder_3* updates
    if (t >= 0.0 && reminder_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reminder_3.tStart = t;  // (not accounting for frame time here)
      reminder_3.frameNStart = frameN;  // exact frame index
      
      reminder_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (reminder_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      reminder_3.setAutoDraw(false);
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


function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var EndComponents;
function EndRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'End' ---
    t = 0;
    EndClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('End.started', globalClock.getTime());
    inst1textbox_3.setText((((("You scored " + correct_count.toString()) + "/") + trials.nTotal.toString()) + " correct!\n Wasn't that fun..."));
    // keep track of which components have finished
    EndComponents = [];
    EndComponents.push(background_6);
    EndComponents.push(inst1textbox_3);
    
    for (const thisComponent of EndComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'End' ---
    // get current time
    t = EndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *background_6* updates
    if (t >= 0.0 && background_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      background_6.tStart = t;  // (not accounting for frame time here)
      background_6.frameNStart = frameN;  // exact frame index
      
      background_6.setAutoDraw(true);
    }
    
    
    // *inst1textbox_3* updates
    if (t >= 0.0 && inst1textbox_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inst1textbox_3.tStart = t;  // (not accounting for frame time here)
      inst1textbox_3.frameNStart = frameN;  // exact frame index
      
      inst1textbox_3.setAutoDraw(true);
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
    for (const thisComponent of EndComponents)
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


function EndRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'End' ---
    for (const thisComponent of EndComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('End.stopped', globalClock.getTime());
    // the Routine "End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
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
