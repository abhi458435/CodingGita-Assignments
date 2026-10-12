//Part C] Relational Operator
//Q.5.Greater Than
//1.
let marks2=78
let p1assingMarks=40
let isPassed=marks2>p1assingMarks
console.log("Is Student Scored More than Passing Marks:",isPassed)

// //2.
let todayTemperature=35
let yesterdayTemperature=28
let whichDayIsHotter=todayTemperature>yesterdayTemperature
console.log("Which Day is Hotter",todayTemperature,whichDayIsHotter)

//3.
console.log(15 > 10);
console.log(10 > 15);
console.log(10 > 10);
// //4.
console.log("20" > 15);
console.log("5" > "10");
console.log("abc" > 10);

//5.
console.log(null>0,Number(null))
console.log(undefined>0,Number(undefined))

//6.
let totalStock=120
let buyStock=85
let checkSufficient=totalStock>buyStock
console.log("Is stock Item is Sufficient?",checkSufficient)

//7.
console.log(true > false);
console.log("10" > "2");
console.log(NaN > 5);

//Less Than.
//1.
let currentWeight=42
let canHold=50
let isMoreItemsCanBeAdded=currentWeight<canHold
console.log("Is More Items Can Be Added?",isMoreItemsCanBeAdded)

//2.
let age=16
let requiredAge=18
let checkUnderage=age<requiredAge
console.log("Is That Person Is Underage?",checkUnderage)

//3.
console.log(8 < 12);
console.log(20 < 10);
console.log(7 < 7);

// //4.
console.log("8" < 10);
console.log("20" < "3");
console.log("hello" < 5);

// //5.
console.log(null<0,Number(null))
console.log(undefined<0,Number(undefined))

//6.
let tankCapacity=500
let currentWaterLevel=375
let isTankNotFull=currentWaterLevel<tankCapacity
console.log("Is Tank Not Full",isTankNotFull)

//7.
console.log(false < true);
console.log("5" < "15");
console.log(NaN < 10);

//Greater Than or Equal To >=
//1.
let minMarksForDistinction=75
let marks1=75
let getsDistinction=minMarksForDistinction>=marks1
console.log("Is Student Gets Distinction",getsDistinction)

//2.
let ticketPrice=300
let _PersonHas=300
let isBuy=ticketPrice>=_PersonHas
console.log("is they can buy ticket?",isBuy)

// //3.
console.log(25 >= 25);
console.log(30 >= 25);
console.log(20 >= 25);

// //4.
console.log("25" >= 25);
console.log("10" >= "2");
console.log(null >= 0);

// //5.
// console.log(undefined >= 0)
//6.
let liftSize=8
let peopleInside=8
isLiftFull=liftSize>=peopleInside
console.log("Is Lift Full?",isLiftFull)

//7.
console.log(true >= 1);
console.log("" >= 0);
console.log(NaN >= NaN);

//Less Than or Equal To <=
//1.
let maxSpeed=60
let vehicleSpeed=60
console.log("is within the limit?",vehicleSpeed<=maxSpeed)

//2.
let passingMarks=40
let marks=39
console.log("is Failed?",marks<=passingMarks)

//3.
console.log(15 <= 20);
console.log(20 <= 15);
console.log(15 <= 15);

// //4.
console.log("15" <= 20);
console.log("30" <= "5");
console.log(null <= 0);

// //5.
console.log(undefined<=0)

// //6.
let canHoldBooks=10
let currentBook=10
console.log(currentBook<=canHoldBooks)

//7.
console.log(false <= 0);
console.log("" <= 0);
console.log(NaN <= 5);

//MixedPractice
//1.
let age=18
let votingAge=18
console.log("is i should take vote?",age>=votingAge)

let temperature=32
let maxTemperature=35
console.log("Is Temperature is less than 35?",temperature<maxTemperature)

let score=90
let requiredScore=85
console,log(score>requiredScore)

//2.
console.log(10 > 5 && 5 < 10);
console.log("10" >= 10);
console.log(null <= undefined);
console.log("5" < "10" && 5 > 2);

//3.
let productCosts=499
let customerHave=500
console.log("Can Customer Can Buy?",productCosts<customerHave)

//4.
console.log("10">"2") //false B/c Number("10","2")=NaN
console.log(10>2) //true according to basic mathematics
