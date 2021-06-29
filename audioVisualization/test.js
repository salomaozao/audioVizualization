let fft;

function setup() {
  let cnv = createCanvas(100, 100);
  cnv.mousePressed(startSound);
  fft = new p5.FFT();
}

function draw() {
  /*
    background(220);
  
    let spectrum = fft.analyze();
    stroke(10, 10, 10);
    fill(255, 0, 255);
    for (let i = 0; i < window.innerWidth; i++) {
      let x = map(i, 0, window.innerWidth, 0, width);
      let h = -height + map(spectrum[i], 0, 255, height, 0);
      rect(x, height, width / window.innerWidth, h);
    }
    */
  /*
    let waveform = fft.waveform();
  
    noFill();
    beginShape();
    stroke(20);
    // for (let i = 0; i < waveform.length; i++) {
    for (let i = 0; i < window.innerWidth; i++) {
      // let x = map(i, 0, waveform.length, 0, width);
      let x = i;
  
      // let y = map(waveform[i], -1, 1, 0, height);
      let y = floor(map(waveform[i], -1, 1, 0, height));
  
      vertex(x, y);
    }
    endShape();
    */
}
