/******************************** 
 * Word_Superiority_Effect *
 ********************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.2.2.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'word_superiority_effect';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'what is your first language?': '',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
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
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);


flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'conditions.xlsx', 'path': 'conditions.xlsx'},
    {'name': 'background.jpg', 'path': 'background.jpg'},
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


var instructionsClock;
var background;
var instruct_txt;
var start_resp;
var start;
var start_mouse;
var trialClock;
var background_2;
var fixation;
var word;
var key_resp;
var question;
var lefttxt;
var righttxt;
var word_accuracies;
var nonword_accuracies;
var word_rts;
var nonword_rts;
var mouse;
var letter;
var trialcount;
var endClock;
var background_3;
var fbtxt;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  background = new visual.ImageStim({
    win : psychoJS.window,
    name : 'background', units : undefined, 
    image : 'background.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [3, 3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  instruct_txt = new visual.TextBox({
    win: psychoJS.window,
    name: 'instruct_txt',
    text: 'In this task you will be shown a series of words. After each word is presented you will be asked if that word contained a particular letter. Use the left and right arrow keys on the keyboard or click/touch the onscreen buttons to answer the question:\n\nLEFT = Yes\nRIGHT = No\n\n',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  start_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  start = new visual.TextBox({
    win: psychoJS.window,
    name: 'start',
    text: 'START',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, (- 0.4)], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.3, 0.1],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: '#5f9ea0', borderColor: 'black',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -3.0 
  });
  
  start_mouse = new core.Mouse({
    win: psychoJS.window,
  });
  start_mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  background_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'background_2', units : undefined, 
    image : 'background.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [3, 3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  fixation = new visual.TextBox({
    win: psychoJS.window,
    name: 'fixation',
    text: '+',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  word = new visual.TextBox({
    win: psychoJS.window,
    name: 'word',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    letterHeight: 0.2,
    lineSpacing: 1.0,
    size: [0.7, 0.5],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  question = new visual.TextBox({
    win: psychoJS.window,
    name: 'question',
    text: 'Did the word contain the letter:',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.3], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
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
  
  lefttxt = new visual.TextBox({
    win: psychoJS.window,
    name: 'lefttxt',
    text: 'YES',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [(- 0.3), (- 0.4)], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.3, 0.1],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: '#5f9ea0', borderColor: 'black',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -5.0 
  });
  
  righttxt = new visual.TextBox({
    win: psychoJS.window,
    name: 'righttxt',
    text: 'NO',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0.3, (- 0.4)], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.3, 0.1],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: '#5f9ea0', borderColor: 'black',
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
  
  // Run 'Begin Experiment' code from track_score
  word_accuracies = [];
  nonword_accuracies = [];
  word_rts = [];
  nonword_rts = [];
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  letter = new visual.TextBox({
    win: psychoJS.window,
    name: 'letter',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    letterHeight: 0.2,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -9.0 
  });
  
  trialcount = new visual.TextBox({
    win: psychoJS.window,
    name: 'trialcount',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.45], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -10.0 
  });
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  background_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'background_3', units : undefined, 
    image : 'background.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [3, 3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  fbtxt = new visual.TextBox({
    win: psychoJS.window,
    name: 'fbtxt',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1, 1],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _start_resp_allKeys;
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
    psychoJS.experiment.addData('instructions.started', globalClock.getTime());
    start_resp.keys = undefined;
    start_resp.rt = undefined;
    _start_resp_allKeys = [];
    // setup some python lists for storing info about the start_mouse
    // current position of the mouse:
    start_mouse.x = [];
    start_mouse.y = [];
    start_mouse.leftButton = [];
    start_mouse.midButton = [];
    start_mouse.rightButton = [];
    start_mouse.time = [];
    start_mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(background);
    instructionsComponents.push(instruct_txt);
    instructionsComponents.push(start_resp);
    instructionsComponents.push(start);
    instructionsComponents.push(start_mouse);
    
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions' ---
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *background* updates
    if (t >= 0.0 && background.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      background.tStart = t;  // (not accounting for frame time here)
      background.frameNStart = frameN;  // exact frame index
      
      background.setAutoDraw(true);
    }
    
    
    // *instruct_txt* updates
    if (t >= 0.0 && instruct_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruct_txt.tStart = t;  // (not accounting for frame time here)
      instruct_txt.frameNStart = frameN;  // exact frame index
      
      instruct_txt.setAutoDraw(true);
    }
    
    
    // *start_resp* updates
    if (t >= 0.0 && start_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_resp.tStart = t;  // (not accounting for frame time here)
      start_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { start_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { start_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { start_resp.clearEvents(); });
    }
    
    if (start_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = start_resp.getKeys({keyList: ['space'], waitRelease: false});
      _start_resp_allKeys = _start_resp_allKeys.concat(theseKeys);
      if (_start_resp_allKeys.length > 0) {
        start_resp.keys = _start_resp_allKeys[_start_resp_allKeys.length - 1].name;  // just the last key pressed
        start_resp.rt = _start_resp_allKeys[_start_resp_allKeys.length - 1].rt;
        start_resp.duration = _start_resp_allKeys[_start_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *start* updates
    if (t >= 1 && start.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start.tStart = t;  // (not accounting for frame time here)
      start.frameNStart = frameN;  // exact frame index
      
      start.setAutoDraw(true);
    }
    
    // *start_mouse* updates
    if (t >= 1 && start_mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_mouse.tStart = t;  // (not accounting for frame time here)
      start_mouse.frameNStart = frameN;  // exact frame index
      
      start_mouse.status = PsychoJS.Status.STARTED;
      start_mouse.mouseClock.reset();
      prevButtonState = start_mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (start_mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = start_mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [start]) {
            if (obj.contains(start_mouse)) {
              gotValidClick = true;
              start_mouse.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = start_mouse.getPos();
          start_mouse.x.push(_mouseXYs[0]);
          start_mouse.y.push(_mouseXYs[1]);
          start_mouse.leftButton.push(_mouseButtons[0]);
          start_mouse.midButton.push(_mouseButtons[1]);
          start_mouse.rightButton.push(_mouseButtons[2]);
          start_mouse.time.push(start_mouse.mouseClock.getTime());
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
    psychoJS.experiment.addData('instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(start_resp.corr, level);
    }
    psychoJS.experiment.addData('start_resp.keys', start_resp.keys);
    if (typeof start_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('start_resp.rt', start_resp.rt);
        psychoJS.experiment.addData('start_resp.duration', start_resp.duration);
        routineTimer.reset();
        }
    
    start_resp.stop();
    // store data for psychoJS.experiment (ExperimentHandler)
    if (start_mouse.x) {  psychoJS.experiment.addData('start_mouse.x', start_mouse.x[0])};
    if (start_mouse.y) {  psychoJS.experiment.addData('start_mouse.y', start_mouse.y[0])};
    if (start_mouse.leftButton) {  psychoJS.experiment.addData('start_mouse.leftButton', start_mouse.leftButton[0])};
    if (start_mouse.midButton) {  psychoJS.experiment.addData('start_mouse.midButton', start_mouse.midButton[0])};
    if (start_mouse.rightButton) {  psychoJS.experiment.addData('start_mouse.rightButton', start_mouse.rightButton[0])};
    if (start_mouse.time) {  psychoJS.experiment.addData('start_mouse.time', start_mouse.time[0])};
    if (start_mouse.clicked_name) {  psychoJS.experiment.addData('start_mouse.clicked_name', start_mouse.clicked_name[0])};
    
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
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
      trialList: 'conditions.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
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


var _key_resp_allKeys;
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
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    word.setText(this_word);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    letter.setText(critical_letter);
    trialcount.setText(((trials.thisN.toString() + "/") + trials.nTotal.toString()));
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(background_2);
    trialComponents.push(fixation);
    trialComponents.push(word);
    trialComponents.push(key_resp);
    trialComponents.push(question);
    trialComponents.push(lefttxt);
    trialComponents.push(righttxt);
    trialComponents.push(mouse);
    trialComponents.push(letter);
    trialComponents.push(trialcount);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *background_2* updates
    if (t >= 0.0 && background_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      background_2.tStart = t;  // (not accounting for frame time here)
      background_2.frameNStart = frameN;  // exact frame index
      
      background_2.setAutoDraw(true);
    }
    
    
    // *fixation* updates
    if (t >= 0.0 && fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation.tStart = t;  // (not accounting for frame time here)
      fixation.frameNStart = frameN;  // exact frame index
      
      fixation.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation.setAutoDraw(false);
    }
    
    // *word* updates
    if (t >= 0.5 && word.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      word.tStart = t;  // (not accounting for frame time here)
      word.frameNStart = frameN;  // exact frame index
      
      word.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (word.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      word.setAutoDraw(false);
    }
    
    // *key_resp* updates
    if (t >= 1 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp.keys == corr_ans) {
            key_resp.corr = 1;
        } else {
            key_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *question* updates
    if (t >= 1 && question.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question.tStart = t;  // (not accounting for frame time here)
      question.frameNStart = frameN;  // exact frame index
      
      question.setAutoDraw(true);
    }
    
    
    // *lefttxt* updates
    if (t >= 1 && lefttxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      lefttxt.tStart = t;  // (not accounting for frame time here)
      lefttxt.frameNStart = frameN;  // exact frame index
      
      lefttxt.setAutoDraw(true);
    }
    
    
    // *righttxt* updates
    if (t >= 1 && righttxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      righttxt.tStart = t;  // (not accounting for frame time here)
      righttxt.frameNStart = frameN;  // exact frame index
      
      righttxt.setAutoDraw(true);
    }
    
    // *mouse* updates
    if (t >= 1 && mouse.status === PsychoJS.Status.NOT_STARTED) {
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
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [lefttxt, righttxt]) {
            if (obj.contains(mouse)) {
              gotValidClick = true;
              mouse.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { 
            _mouseXYs = mouse.getPos();
            mouse.x.push(_mouseXYs[0]);
            mouse.y.push(_mouseXYs[1]);
            mouse.leftButton.push(_mouseButtons[0]);
            mouse.midButton.push(_mouseButtons[1]);
            mouse.rightButton.push(_mouseButtons[2]);
            mouse.time.push(mouse.mouseClock.getTime());
          }
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    
    // *letter* updates
    if (t >= 1 && letter.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      letter.tStart = t;  // (not accounting for frame time here)
      letter.frameNStart = frameN;  // exact frame index
      
      letter.setAutoDraw(true);
    }
    
    
    // *trialcount* updates
    if (t >= 0 && trialcount.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialcount.tStart = t;  // (not accounting for frame time here)
      trialcount.frameNStart = frameN;  // exact frame index
      
      trialcount.setAutoDraw(true);
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


var correct;
var rt;
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
    if (key_resp.keys === undefined) {
      if (['None','none',undefined].includes(corr_ans)) {
         key_resp.corr = 1;  // correct non-response
      } else {
         key_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    psychoJS.experiment.addData('key_resp.corr', key_resp.corr);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // Run 'End Routine' code from track_score
    if ((condition === "word")) {
        if (key_resp.keys) {
            word_accuracies.push(key_resp.corr);
            word_rts.push(key_resp.rt);
        } else {
            if ((("lefttxt" === mouse.clicked_name[0]) && (corr_ans === "left"))) {
                word_accuracies.push(1);
            } else {
                if ((("righttxt" === mouse.clicked_name[0]) && (corr_ans === "right"))) {
                    word_accuracies.push(1);
                } else {
                    word_accuracies.push(0);
                }
            }
            word_rts.push(mouse.time);
        }
        correct = nonword_accuracies.slice((- 1))[0];
        rt = nonword_rts.slice((- 1))[0];
    } else {
        if ((condition === "nonword")) {
            if (key_resp.keys) {
                nonword_accuracies.push(key_resp.corr);
                nonword_rts.push(key_resp.rt);
            } else {
                if ((("lefttxt" === mouse.clicked_name[0]) && (corr_ans === "left"))) {
                    nonword_accuracies.push(1);
                } else {
                    if ((("righttxt" === mouse.clicked_name[0]) && (corr_ans === "right"))) {
                        nonword_accuracies.push(1);
                    } else {
                        nonword_accuracies.push(0);
                    }
                }
                nonword_rts.push(mouse.time);
            }
            correct = nonword_accuracies.slice((- 1))[0];
            rt = nonword_rts.slice((- 1))[0];
        }
    }
    psychoJS.experiment.addData("correct", correct);
    psychoJS.experiment.addData("rt", rt);
    
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse.x) {  psychoJS.experiment.addData('mouse.x', mouse.x[0])};
    if (mouse.y) {  psychoJS.experiment.addData('mouse.y', mouse.y[0])};
    if (mouse.leftButton) {  psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton[0])};
    if (mouse.midButton) {  psychoJS.experiment.addData('mouse.midButton', mouse.midButton[0])};
    if (mouse.rightButton) {  psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton[0])};
    if (mouse.time) {  psychoJS.experiment.addData('mouse.time', mouse.time[0])};
    if (mouse.clicked_name) {  psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name[0])};
    
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var word_acc;
var nonword_acc;
var word_rt;
var nonword_rt;
var feedback;
var endComponents;
function endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end' ---
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('end.started', globalClock.getTime());
    // Run 'Begin Routine' code from calculate
    word_acc = util.average(word_accuracies);
    nonword_acc = util.average(nonword_accuracies);
    word_rt = util.average(word_rts);
    nonword_rt = util.average(nonword_rts);
    psychoJS.experiment.addData("word_average_acc", word_acc);
    psychoJS.experiment.addData("nonword_average_acc", nonword_acc);
    psychoJS.experiment.addData("word_average_re", word_rt);
    psychoJS.experiment.addData("nonword_average_rt", nonword_rt);
    feedback = "";
    if (((word_acc > nonword_acc) && (word_rt < nonword_rt))) {
        feedback = "You showed a word superiority effect!";
    }
    if (((word_acc > nonword_acc) && (! (word_rt < nonword_rt)))) {
        feedback = "You were more accurate for words versus non words, but you were faster for non words.";
    }
    if (((word_rt < nonword_rt) && (! (word_acc < nonword_acc)))) {
        feedback = "You were faster for words versus non words, but you were more accurate for non words.";
    }
    if (((word_acc < nonword_acc) && (word_rt > nonword_rt))) {
        feedback = "You showed the opposite of a word superiority effect - you were faster and more accurate for non words!";
    }
    feedback += "\n Word accuracy: ";
    feedback += Number.parseInt((word_acc * 100)).toString();
    feedback += "%";
    feedback += "\n Word response time: ";
    feedback += Number.parseInt((word_rt * 1000)).toString();
    feedback += "ms";
    feedback += "\n Non word accuracy: ";
    feedback += Number.parseInt((nonword_acc * 100)).toString();
    feedback += "%";
    feedback += "\n Non word response time: ";
    feedback += Number.parseInt((nonword_rt * 1000)).toString();
    feedback += "ms";
    
    fbtxt.setText(feedback);
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(background_3);
    endComponents.push(fbtxt);
    
    for (const thisComponent of endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end' ---
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *background_3* updates
    if (t >= 0.0 && background_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      background_3.tStart = t;  // (not accounting for frame time here)
      background_3.frameNStart = frameN;  // exact frame index
      
      background_3.setAutoDraw(true);
    }
    
    
    // *fbtxt* updates
    if (t >= 0.0 && fbtxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fbtxt.tStart = t;  // (not accounting for frame time here)
      fbtxt.frameNStart = frameN;  // exact frame index
      
      fbtxt.setAutoDraw(true);
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
    for (const thisComponent of endComponents)
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


function endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end' ---
    for (const thisComponent of endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('end.stopped', globalClock.getTime());
    // the Routine "end" was not non-slip safe, so reset the non-slip timer
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
