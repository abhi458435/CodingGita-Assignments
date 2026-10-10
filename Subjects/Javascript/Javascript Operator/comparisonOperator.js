// 1.Loose Equality
Q1.
console.log("25"==25)

//Q2.
console.log(0==false)

//3.
console.log(10 == "10");
console.log(null == undefined);

//4.
console.log("" == 0);
console.log([] == false);

//5.
console.log(NaN==NaN) //Because i don't know NaN means which are the specific number so that's why NaN==NaN return false

//2. Loose Inequality !=
// Q-1
console.log("18"!=18)
// Q-2
let storedPassword="1234"
let enteredPasssword=1234
console.log(enteredPasssword!=storedPassword)

//Q3.
console.log(5 != "5");
console.log(0 != false);


//Q4.
console.log(null != undefined);
console.log("" != 0);

//5.
console.log(NaN!=NaN)

//3].Strict Equality ===
//Q1.
console.log("25"===25) //because of different datatype ,one is string and another is number

//Q2.
console.log(0===false)
console.log(null===undefined)
//Q3.
console.log(10 === "10");
console.log(true === 1);

//Q4.
console.log("" === 0);
// console.log([] === false);

Q5.
// Bacause === strict equality clearly show the comparison with value and adata type 
// which help for computer and real-world

// 4].Strict Inequality(!==)
Q-1
console.log("18"!==18)
//Q-2
console.log(0!==false)
console.log(null!==undefined)

//Q-3
console.log(5 !== "5");
console.log(true !== 1);
//Q-4
console.log("" !== 0);
console.log(NaN !== NaN);

//Q-5.
let num;
console.log(num!=="0")