const canvas = document.getElementById('canvas1');
const ctx = canvas.getContext('2d');
console.log(ctx);

const CANVAS_WIDTH = canvas.width= 600;
const CANVAS_HEIGHT = canvas.height = 600;

const playerIMAGE = new Image()
playerIMAGE.src = 'static/images/shadow_dog.png'
const spriteWidth = 575;
const spriteHeight = 523;
let frameX = 0;
let frameY = 6;

function animate(){
  ctx.clearRect(0, 0, CANVAS_HEIGHT,CANVAS_WIDTH);
  // ctx.fillRect(50,50,100,100);
  ctx.drawImage(playerIMAGE, frameX* spriteWidth, frameY* spriteHeight,spriteWidth,spriteHeight,0,0,spriteWidth,spriteHeight);
  if (frameX <6)frameX++;
  else frameX = 0;
  requestAnimationFrame(animate)
};

// animate();