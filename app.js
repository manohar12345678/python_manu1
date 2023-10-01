
// How to take the input from the console

// Import the 'readline' module to enable user input from the console in a Node.js application
// 'readline is a built in module'
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Prompt the user for the first number
rl.question('Enter the first number: ', function (num1) {
  // Prompt the user for the second number
  rl.question('Enter the second number: ', function (num2) {
    // Convert the input strings to numbers
    const number1 = parseFloat(num1);
    const number2 = parseFloat(num2);

    // Check if the conversion was successful
    if (!isNaN(number1) && !isNaN(number2)) {
      // Perform the addition
      const sum = number1 + number2;
      console.log(`The sum of ${number1} and ${number2} is ${sum}`);
    } else {
      console.log('Invalid input. Please enter valid numbers.');
    }

    // Close the readline interface
    rl.close();
  });
});

// Handle the close event
rl.on('close', function () {
  console.log('Thank you for using the number addition program.');
  process.exit(0);
});

