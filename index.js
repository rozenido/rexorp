
function fizzbuzz(input) {
    if (input % 3 === 0 && input % 5 === 0)
    return 'FizzBuzz'
    if (typeof input !== 'number')
    return 'Not a number';
    if (input % 3 === 0)
    return 'Fizz'
    if (input % 5 === 0)
    return 'Buzz';
}

console.log(fizzbuzz(15));