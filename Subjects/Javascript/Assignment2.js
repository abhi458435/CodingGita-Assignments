// ==========================================
// JavaScript Assignment 2 - Complete Solutions
// ==========================================

// --- Part-1 / Part-a ---

// Question 1
let name = "Abhishek";
let age = 18;
let city = "Begusarai";

console.log(name);
console.log(age);
console.log(city);


// Question 2
let score = 50;
score = 80;
console.log(score);


// Question 3
const pi = 3.14;
console.log(pi);


// Question 4
var num1 = 20;
let num2 = 40;

console.log(num1);
console.log(num2);



// --- Part-b ---

// Question 5
const studentName = "Abhishek";
let marks = 96;
const schoolName = "KORAI";

marks = 92; // Re-assigning new marks value

console.log(studentName);
console.log(marks);
console.log(schoolName);


// Question 6 (Scope demonstration)
let ageVal = 50;
if (ageVal > 20) {
    var a = 10;
    let b = 20;
    const c = 30;
}
console.log(a); // Accessible because 'var' is function/globally scoped
// console.log(b); // ReferenceError: 'let' is block-scoped
// console.log(c); // ReferenceError: 'const' is block-scoped


// Question 7 (Re-declaration rules)
var user = "Abhishek";
var user = "Saurav"; // 'var' allows re-declaration
console.log(user);

let userLet = "Abhishek";
userLet = "Saurav"; // 'let' allows re-assignment (not re-declaration in same scope)
console.log(userLet);


// Question 8 (Re-assignment rules)
var name1 = "Abhishek";
name1 = "Saurav"; // Allowed

let age1 = 18;
age1 = 20; // Allowed

const marks1 = 65;
// marks1 = 75; // Error! const variables cannot be re-assigned

console.log(name1);
console.log(age1);
console.log(marks1);


// Question 9 (Block scope & shadowing)
var x = 10;
if (true) {
    var x = 20; 
    let y = 30; 
    const z = 40; 
}
console.log(x);
// console.log(y); // Throws error (block scoped)
// console.log(z); // Throws error (block scoped)


// Question 10 (Final debugging example)
const fullName = "Abhishek";
let userAge = 20;

if (true) {
    var cityVal = "Delhi";
    let country = "India";
}
console.log(cityVal);    // Accessible ('var')
// console.log(country); // Error ('let' is block-scoped)

let finalScore = 50;
finalScore = 80;         // Correct way to re-assign a variable
// const finalScore = 80; // Error if you use const to re-assign
console.log(finalScore);