class Chord {
    constructor(chord, time) {
       this.chord = chord;
       this.time = time;
       this.pos = createVector(random(100,displayWidth-100)/3,50);
       this.vel = createVector(0,2);
       this.acc = createVector();
       this.move = false;
       this.started = null;
    }

    

    update(){
        this.vel.add(this.acc);
        this.pos.add(this.vel);
        this.acc.mult(0)
        if(this.pos.y > 350){
            this.pos.y = 1000;
            var microSecondsDiff = Math.abs(this.started - new Date().getTime());
        }
        if (this.started === null) {
            this.started = new Date().getTime();
        }
    }

    show(){
        push()
        translate(this.pos.x,this.pos.y);
        textSize(20);
        fill(50);
        text(this.chord, this.pos.x, this.pos.y)
        pop()
    }
    
} 