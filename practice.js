const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter the first number? ', (input1) => {
    const number1 = parseInt(input1);

    rl.question('Enter the second number?', (input2) => {
        const number2 = parseInt(input2);
        
        rl.question('Enter the second number?', (input3) => {
            const number3 = parseInt(input3);
        
        
        rl.close(); // Close the interface when done
    });
});
});
