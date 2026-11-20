//1.
// let n=4;
// let num=1
// for(let i=1; i<=n; i++){
//     let row=""
//     for(let j=1; j<=i; j++){
//         row+=num+" "
//         num++
//     }
//     console.log(row)
// }

//2.
// let n=4;
// let num=1
// for(let i=1; i<=n; i++){
//     let row=""
//     for(let j=1; j<=i; j++){
//         row+=i+" "
        
//     }
//     console.log(row)
// }

//3.
//see solution of question-1

//4.
// let n=4;
// for(let i=1; i<=n; i++){
//     let row="";
//     for(let j=1; j<=n; j++){
//         if (j==1 ||j==n||i==1 ||i==n){
//             row+="*"
//         }else{
//             row+=" "
//         }
//     }
//     console.log(row)
// }

//5.
// let n=6;
// for(let i=1; i<=n; i++){
//     let bag=""
//     if(i%2==1){
//         for(let j=1; j<=i; j++){
//         bag+="#"+" "
//     }
//     }else{
//         for(let k=1; k<=i; k++){
//             bag+="$"+" "
//         }
//     }
//     console.log(bag)
// }

//6.
// let n=5;
// for(let i=1; i<=n; i++){
//     let bag=""
//     for(let j=1;j<=i; j++){
//         bag+=chr(j+64)+" "
//     }
//     console.log(bag)
// }

//7.
// let n=5;
// for(let i=1; i<=n; i++){
//     if(i==1 || i==2 || i==n){
//         let bag=""
//         for(let j=1; j<=i; j++){
//           bag+="*"
//         }
//     }else{
//         console.log("*"+" "*(i-2)+"*")
//     }
    
// }
// console.log(bag)

//8.
// let n=5;
// for(let i=n; i>=1; i--){
//     let bag=""
//     for(let j=1; j<=i; j++){
//         bag+="*"
//     }
//     console.log(bag)
// }

//9.
// let n=5;
// for(let i=n; i>=1; i--){
//     let bag=""
//     for(let j=1; j<=i; j++){
//         bag+=i+""
//     }
//     console.log(bag)}

//10.
// let n=5;
// for(let i=n; i>=1; i--){
//     let bag=""
//     for(let j=1; j<=i; j++){
//         bag+=j+" "
//     }
//     console.log(bag)
// }

//11.
let n=15;
for(let i=n; i>=1; i--){
    let bag=""
    for(let j=1; j<=i; j++){
        bag=j+" "
    }
    console.log(bag)
}