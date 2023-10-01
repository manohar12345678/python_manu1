const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

numbers=[];
for (let i = 0; i < 5; i++) {
    rl.question('Enter the first number? ', (input1) => {
        const number1 = parseInt(input1);
        numbers.push(number1);
        rl.close(); // Close the interface when done
    });
}
console.log(numbers);