let cols, rows;
const scale = 20;
const w = 1200;
const h = 800;
let flying = 0;
let side = 0;
let angle = 0;
var landscape = [];
var heli;

function setup() {
    createCanvas(800, 800, WEBGL);
    cols = w / scale;
    rows = h / scale;
    landscape = new Array(cols);
    heli = loadModel("uh60.obj",true);
}

function draw() {
    if (keyIsDown(LEFT_ARROW)) {
        side = side - 0.1;
        console.log(side)
    }
    if (keyIsDown(RIGHT_ARROW)) {
        side = side + 0.1;
        console.log(side)
    }
    if (keyIsDown(UP_ARROW)) {
        // if (angle < 1.0) {
        angle = angle + 0.04
        // }
    }
    if (keyIsDown(DOWN_ARROW)) {
        // if (angle > -0.6) {
        angle = angle - 0.04
        // }
    }
    // flying -= 0.01;
    flying = 0;
    let yoff = flying;
    let highest = 0;
    for (let y = 0; y < rows; y++) {
        let xoff = side;
        let xArray = [rows];
        for (let x = 0; x < cols; x++) {
            let noise2 = map(noise(xoff, yoff), 0, 1, -100, 100);
            xArray[x] = noise2;
            xoff += 0.2;
            if (noise2 > highest) {
                highest = noise2;
            }
        }
        yoff += 0.2;

        landscape[y] = xArray;
    }
    background(0);
    stroke(255);
    noFill();
    rotateX(PI / (3 + angle));
    translate(-w / 2, -h / 2 - 100);
    stroke(255);

    for (let y = 0; y < rows - 1; y++) {
        beginShape(TRIANGLE_STRIP);
        for (let x = 0; x < cols; x++) {
            if (highest === landscape[y][x]) {
                stroke(100);
                strokeWeight(2);
                fill(255);
                vertex(x * scale, y * scale, landscape[y][x] + 50);
                // strokeWeight(1);
                stroke(255);
            }
            vertex(x * scale, y * scale, landscape[y][x]);
            vertex(x * scale, (y + 1) * scale, landscape[y + 1][x]);

        }
        endShape();
        noFill();
        model(heli);
    }
}