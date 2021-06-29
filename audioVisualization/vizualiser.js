function preload() {
  sound = loadSound("./test.js");
}

function setup() {
  let cnv = createCanvas(window.innerWidth, window.innerHeight);
  cnv.mouseClicked(togglePlay);
  fft = new p5.FFT();
  sound.amp(0.2);
}

function draw() {
  background(220);
  noStroke();
  fill(255, 0, 255);

  let freq = map(mouseX, 0, windowWidth, 20, 10000);
  freq = constrain(freq, 1, 20000);

  let spectrum = fft.analyze(); //Analyze creates an array with 1024 objects, each one represents a frequency
  var graves,
    medios,
    agudos = 0;
  for (let i = 0; i < spectrum.length; i++) {
    if (spectrum[i] < 381) {
      // Ondas Graves
      spectrum[i] > 0 ? (graves += 0.29) : {};
    } else if (spectrum[i] > 381 && spectrum[i] < 682) {
      // Ondas Médias
      spectrum[i] > 0 ? (medios += 0.29) : {};
    } else if (spectrum[i] > 682) {
      // Ondas Agudas
      spectrum[i] > 0 ? (agudos += 0.29) : {};
    }

    document.getElementById("grave").style.opacity = graves / 100;
    document.getElementById("medio").style.opacity = agudos / 100;
    document.getElementById("agudo").style.opacity = graves / 100;
  }

  stroke(255);
}

function togglePlay() {
  if (sound.isPlaying()) {
    sound.pause();
  } else {
    sound.loop();
  }
}
