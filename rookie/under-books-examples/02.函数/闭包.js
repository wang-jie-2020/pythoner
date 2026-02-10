function createCounter() {
    let count = 0;
    return function() {
        count++;
        return count;
    };
}

const counter = createCounter();
console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3

for (var i = 0; i < 5; i++) {
    setTimeout(function () {
        console.log(i)
    }, 1000)
}


for (let i = 0; i < 5; i++) {
    setTimeout(function () {
        console.log(i)
    }, 1000)
}