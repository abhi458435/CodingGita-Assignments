//Part A] For Loop

//1.Q1. Counting Numbers 🔢
// for (i=1; i<=15; i++){
// console.log(i)
// }

//Q2. Even Numbers 🎯
// for (i=2; i<=40; i+=2 ){
//     console.log(i)
// }

//Q3. Odd Numbers 🏃
// for (i=1; i<=35; i+=2){
//     console.log(i)
// }

//Q4. Saving Money 💰
// let sum=0
// let saveMoney=10
// for (day=1; day<=10; day++){
//     sum=sum+saveMoney*day
// }
// console.log("Total savings after 10 days:",sum)

//Q5. Multiplication Table 📚
// for (i=1; i<=10; i++){
//     console.log(`12x${i}=${i*12}`)
// }

//Q6. Daily Water Intake 💧
// let noOfGlass=3
// for (day=1; day<=7; day++){
//     sum=noOfGlass*day
//     console.log(`Day ${day}:${sum} glasses`)
// }

//Q7. Shopping Calculation 🛍️
// let costOfOneChocolates=15
// for (number=1; number<=10; number++){
//     x=costOfOneChocolates*number
//     console.log(`${number} chocolate= ₹${x}`)
// }

//Q8. Sum of Even Number
// let sum=0
// for (i=2; i<=30; i+=2){
//     sum=sum+i
// }
// console.log("Sum of Even Number:",sum)

//Q9. Weekly Exercise 💪
// let noOfPushupsInOneDay=5
// for(day=1; day<=7; day++){
//     y=noOfPushupsInOneDay*day
//     console.log(`Day ${day}: ${y} push-ups`)
// }

//Q10. Movie Tickets 🎬
// let ticketCostPerPerson=150
// for (person=1; person<=8; person++){
//     z=ticketCostPerPerson*person
//     console.log(`${person} person:₹${z}`)
// }

//Part B] For Loop (Additional advanced questions)

//1.
// let array=[28,32,25,40,18,35]
// count=0
// for(let i=0; i<=array.length-1; i++){
//     count+=array[i]>=30
// }
// console.log(`There are ${count} many days were hotter than 30°C. `)

//2.
// let num="4729";
// sum=0
// for (i=0; i<=num.length-1; i++){
//     sum+=Number(num[i])
// }
// console.log(sum)

//3.
// for (i=1; i<=100; i++){
//     if (i%3==0 && i%5==0 && i%7!=0){
//         console.log(i)
//     }

// }

//4.
// let str="JavaScript"
// let consonants=""
// for (let i=0; i<=str.length-1; i++){
//    if (str[i]!="a" && str[i]!="e" && str[i]!="i" && str[i]!="o" && str[i]!="u"){
//     consonants+=str[i]
// }
    
// }
// console.log(consonants)

//5.
// arr=[10,2,7,20,74]
// max=0
// for (i=0; i<=arr.length-1; i++){
//    if((arr[i])>max){
//     max=arr[i]
//    }
// }
// console.log(max)

//6.
// let num=67;
// sum=0;
// for(let i=1; i<num; i++){
//     if (num%i==0){
//         sum+=i
//     }
// }
// if (sum==num){
//     console.log("Perfect Number")
// }

//7.
// let bag=""
// for (let i=0; i<=7; i++){
// bag+=2**i+" "

// }
// console.log(bag)

//8.
//fibonasi series:- 0,1,1,2,3,5,8,13,21.......

// let a=0
// let b=1
// let fib_series="0 1 "
// for (i=1; i<=18; i++){
//     let c=a + b;
//     fib_series+=c+" "
//     a=b;
//     b=c;
// }
// console.log(fib_series)

//9.
// let arr=[45,78,90,32,56,88]
// let sum=0
// let count=0
// let i=0
// for(let i=0; i<=arr.length-1; i++){
//     sum+=arr[i]
//     averageMarks=sum/arr.length
// }
// console.log(i)
// if (arr[i]>averageMarks){
//     count+=1
// }
// console.log("Average Marks of Student Scores are",averageMarks,"and",count,"Students Score More Than Average Marks")

//10.
// let num = 49;
// let binary = "";

// for(; num != 0;){
//   let remainder = num % 2;
//   binary = remainder+binary;
//   num = Math.floor(num / 2);
// };
// console.log(binary)


//Part C-a] break inside a for Loop
//1.
// let arr=[10,43,7,29]
// for(let i=0; i<=arr.length-1; i++){
//     if ((arr[i])==7){
//         console.log(i, arr[i])
//         break
//     }
// }

//2.
// let correct = "abhi@123";
// let found = false;

// for (let i = 1; i <= 5; i++) {
//     let password = prompt("Enter your password: "); //prompt works in js compiler so you can test the code on that website

//     if (password == correct) {
//         console.log("Access granted");
//         found = true;
//         break;
//     }
// }

// if (found === false) {
//     console.log("Account locked");
// }

3.
// let sum=0
// let i=1
// for (let i=1; i++;){
// sum+=i
// if (sum>=100){

// }
// }

//4.
// let a=14;
// let b=15;
// let arr=[];
// for (let i=0;i<15;i++){
//     arr[i] = a;
//     let c=a+b;
//     a=b;
//     b=c;
// }
// for (let i = 14; i >= 0; i--) {
//     console.log(arr[i]);
// }

//5.
// let num="121"
// let bag=""
// for (i=num.length-1; i>=0; i--){
//     bag+=num[i]+""
// }
// if (num==bag){
//     console.log("Palindrome")
// }

//6.
// let arr=[12,45,7,23,56,89,34]
// let max=-Infinity
// for (let i=arr.length-1; i>=0; i--){
//     if ((arr[i])>max && arr[i]<50){
//         max=arr[i]
//     }
// }
// console.log(max)

//7.
// let temp=[32,28,42,19,35,27,38]
// let count=0
// for (let i=temp.length-1; i>=0; i--){
//     if (temp[i]<30){
//         count+=1
//     }
// }
// console.log(count)

//8.
// let num=13
// let binary=""
// for(; num!=0;){
//     let remainder=num%2;
//     binary=remainder+binary;
//     num=Math.floor(num/2)
// }
// // console.log(binary)
// let ans=""
// for(i=binary.length-1; i>=0; i--){
// ans +=binary[i]
// }
// console.log(ans)

//9.
// let arr=[90,85,70,95,60,88,75]
// for(let i=arr.length-1; i>=0; i--){
//     if ((arr[i])>80){
//         console.log(i,arr[i])
//     }
// }

//10.
// for(let i=40; i>=1; i--){
//     // console.log(i**0.5)
//     if((i**0.5)%1==0){
//         continue;
//     }
//     console.log(i)
// }




// let names=["Nishit","Sumit","Abhishek","Masoom"];
// for(let i=0; i<=names.length-1; i++){
//   // console.log(names[i])
//   if(names[i][0]==="S"){
//     console.log(names[i])
//     break;
//   }
// }
















































































//................................................................
//Part D] Reverse For Loop
//1.
// for (let i=50; i>=1; i--){
//     if (i%3==0 && i%9!=0){
//         console.log(i)
//     }
// }

//2.
// let num="4729"
// let product=1
// for (i=num.length-1; i>=0; i--){
// if (i%2==1){
//     product*=num[i]
// }
// }
// console.log("Products Of Odd Number:",product)

//3.
// let str="Programming"
// let consonants=""
// for(let i=str.length-1; i>=0; i--){
//     if (str[i]!=="a" && str[i]!=="e" && str[i]!=="i" && str[i]!=="o" && str[i]!=="u"){
//         consonants+=str[i]+" "
//     }
// }
// console.log(consonants)

//4.

