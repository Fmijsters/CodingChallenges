const snares = new Array(6);
function setup() {
    createCanvas(displayWidth, displayHeight);
    background(121);
    
    for (var i = 0; i < snares.length; i++) {
    	let y = 300 + (40 * (i+1));
    	snares[i] = [0,y,displayWidth,y];
    }
    console.log(displayWidth);
    loadJSON("chords.txt","json",createChords);
}

function createChords(chordList){
	console.log(chordList)
}

function draw() {
	stroke(255)
    for (var i = 0; i < snares.length; i++) {
    	let x1 = snares[i][0];
    	let y1 = snares[i][1];
    	let x2 = snares[i][2];
    	let y2 = snares[i][3];
    	line(x1,y1,x2,y2)
    }
}   