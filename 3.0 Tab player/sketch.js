const snares = new Array(6);
var chordList = null;
const dropTime = 2083;
const pause= 5000;
var audio = new Audio('Taylor Swift - You Belong With Me.mp3');
var play = false;
function setup() {
    createCanvas(displayWidth, 800);
    background(121);
    
    for (var i = 0; i < snares.length; i++) {
    	let y = 300 + (40 * (i+1));
    	snares[i] = [0,y,displayWidth,y];
    }
    loadJSON("chords.txt","json",createChords);

}
function startaudio(){
	play = true;
}

function createChords(chordListJson){
	chordList = new Array(chordListJson.chords.length);
	setTimeout(startaudio,pause);
	for (var i = 0; i <chordList.length; i++) {
		let chord = new Chord(chordListJson.chords[i].chord,chordListJson.chords[i].time);
		chordList[i] = chord;
		setTimeout(function() {
    		addForce(chord);
		}, pause + (chord.time * 1000) - dropTime)
	}
}

function addForce(chord){
	chord.move = true;
}

function draw() {
	background(121);
	stroke(255)
	if (play) {
		audio.play()
		play = false;
	}
	if (chordList!==null) {
    	for (var i = 0; i < chordList.length; i++) { 
    		if (chordList[i].move) {
    			chordList[i].update()
    		}
    		chordList[i].show()
    	}
    }
}   