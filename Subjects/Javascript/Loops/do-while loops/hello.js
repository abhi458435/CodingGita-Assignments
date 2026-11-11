//Q1. Print Numbers in Reverse
// let i=10;
// let n=1;
// do{
//     console.log(i)
//     i--
// }while(i>=n)

//Q2. Print Even Numbers
// let i=1;
// let n=20;
// do{
// if (i%2==0){
//     console.log(i)
    
// }
// i++
// }while(i<=n)

//Q3. Sum of Natural Numbers
// let i=1;
// let n=5;
// let sum=0
// do{
// sum+=i
// i++

// }while(i<=n)
// console.log(sum)

//Q4. Product of Digits
// let num=234;
// let product=1
// do{
//     let x=num%10
//     num=Math.floor(num/10)
//     product*=x
    
// }while(num>0)
//     console.log(product)

//Q5. Find the First Digit
// let num=58372;
// let rev=0
// let firstDigit;
// do{
//     let x=num%10;
//     num=Math.floor(num/10)
//     rev=rev*10+x
//     firstDigit=rev%10;
// }while(num>0)
//     console.log(firstDigit)

//Q6.Calculate a Power
// let base=3;
// let exponent=4;
// let count=0;
// let result=1;
// do{
//     result*=base
//     count++
// }while(exponent>count)
//     console.log(result)

//Q7. Print Multiples with Conditions
// let i=1
// let n=100
// do{
//     if ((i%4==0) && (i%8!=0)){
//         console.log(i)
        
//     }
//     i++
// }while(i<=n)

//Q8. Check a Palindrome Number
// let num=1221
// let rev=0
// let original=num
// do{
//     let x=num%10
//     rev=rev*10+x
//     num=Math.floor(num/10)

// }while(num>0){
//     if (rev==original){
//         console.log("Palindrome")
//     }else{
//         console.log("Nonpalindome")
//     }
// }

//Q9. Find the Greatest Common Divisor (GCD)
// let a=48
// let b=18
// do{
//     let q=a%b
//     a=b
//     b=q

// }while(b!=0)
//     console.log("GCD:",a)

//Q10. Convert Decimal to Binary
// let n=13
// let binary=""
// do{
//     let x=n%2
//     binary=x+binary
//     n=Math.floor(n/2)
// }while(n!=0)
// console.log(binary)