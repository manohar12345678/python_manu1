const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const numbers = [];

function getInput(i) {
  if (i < 5) {
    rl.question(`Enter number ${i + 1}: `, (input) => {
      const number = parseInt(input);
      numbers.push(number);
      getInput(i + 1);
    });
  } 
  
  else {
    rl.close(); // Close the interface when done
    processInput();
  }
}

function processInput() {
  console.log("Numbers entered:", numbers);
}

getInput(0);
