let cols, rows;
const scale = 20;
const w = 2000;
const h = 1600;
let flying = 0;
let side = 0;
var landscape = [];

function setup() {
    createCanvas(1000, 1000, WEBGL);
    cols = w / scale;
    rows = h / scale;
    landscape = new Array(cols);

}

function draw() {
    if (keyIsDown(LEFT_ARROW)){
        side = side -0.1;
        console.log(side)
    }else if(keyIsDown(RIGHT_ARROW)){
        side = side +0.1;
        console.log(side)
    }
    flying -= 0.1;
    let yoff = flying;
    for (let y = 0; y < rows; y++) {
        let xoff = side;
        let xArray = [rows];
        for (let x = 0; x < cols; x++) {
            xArray[x] = map(noise(xoff, yoff), 0, 1, -100, 100);
            xoff += 0.2;
        }
        yoff += 0.2;

        landscape[y] = xArray;
    }

    background(0);
    stroke(255);
    noFill();
    rotateX(PI / 3);
    translate(-w / 2, -h / 2 - 100);
    for (let y = 0; y < rows-1; y++) {
        beginShape(TRIANGLE_STRIP);
        for (let x = 0; x < cols; x++) {

            vertex(x * scale, y * scale, landscape[y][x]);
            vertex(x * scale, (y + 1) * scale, landscape[y + 1][x]);
        }
        endShape();
    }
}