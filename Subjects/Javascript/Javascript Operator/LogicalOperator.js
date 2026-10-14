//1. Logical AND &&
//1.
// let userName="admin"
// let password=1234
// let isValid=userName && password
// console.log("Is Valid?",isValid)

//2.
// let isLoggedIn = true
// let hasPermission = true
// let canAccess=isLoggedIn && hasPermission
// console.log("Can Access?",canAccess)

//3.
// let inStock = true
// let price = 800
// let canBuy=inStock && price<1000
// console.log("Can Buy?",canBuy)

//4.
// let marks=75
// let attendance=80
// let passingRequired=marks>65 && attendance>70
// console.log("Is Pass?",passingRequired)

//5.
// let isWeekend = true
// isHoliday = false
// isPartyHappen=isWeekend && isHoliday
// console.log("Is Party Happen?",isPartyHappen)

//6.
// let a = 0;
// let b = 10;
// let result = a && b;
// console.log(result);
// //7.
// let x = 5;
// let y = 10;
// let result1 = (x > 3 && y) || 0;
// console.log(result1);

//8.
// let p = "Hello";
// let q = "";
// let r = "World";
// let result = p && q && r;
// console.log(result);

//9.
// let val = 5;
// let condition = val && (val = 0);
// console.log(condition);
// console.log(val);

//10.
// let x = 10;
// let y = 20;
// let result = (x && y) && (x > y);
// console.log(result);

//2. Logical OR ||
//1.
// let passwordCorrect = true
// let  otpValid = false
// let isLoginAllow=passwordCorrect || otpValid
// console.log("Is Login Allow?",isLoginAllow)

//2.
// let isMember = false
// let hasCoupon = true
// isDiscountApplies= isMember || hasCoupon
// console.log("Is Discount Applies?",isDiscountApplies)

//3.
// let age=16
// let height=155
// let isEntryAllow= age>18 || height>150
// console.log("Is Entry Allow?",isEntryAllow)

//4.
// let emailGiven = true
// let phoneGiven=false
// let isFormValid=emailGiven || phoneGiven
// console.log("Is Form Valid?",isFormValid)

//5.
// let score=500
// let timeBonus=true
// let canGameOpens=timeBonus || score>1000
// console.log("Can Game Opens?",canGameOpens)

//6.
// let a = 0;
// let b = false;
// let c = "";
// let d = null;
// let e = 42;
// let result = a || b || c || d || e;
// console.log(result);

//7.
// let x = "Hello" || 0;
// let y = 0 || "Hi";
// console.log(x, y);

//8.
// let a = 10;
// let b = 20;
// let result = (a < 5) || (b > 15);
// console.log(result);

//9.
// let val = 5;
// let condition = val || (val = 0);
// console.log(condition);
// console.log(val);

//10.
// let x = "" || 0 || false || null || undefined || "OK";
// console.log(x);


//3.Logical NOT !
//1.
// let isBanned = false
// let canLoGin=!isBanned
// console.log("Can Login?",canLoGin)

//2.
// let isCompleted = false
// let isStillPending=!isCompleted
// console.log("Is Still Pending?",isStillPending)

//3.
//  let isOn = true
//  let isOff=!isOn
//  console.log("Is Off?",isOff)

//4.
// let isActive = false
// let cannotAccessPremiumContent=!isActive
// console.log("Cannot Access Premium Content?",cannotAccessPremiumContent)

//5.
// let isReadOnly = false
// let canBeEdited=!isReadOnly
// console.log("Can Be Edited?",canBeEdited)

//6.
// let a = 0;
// let b = 1;
// console.log(!a, !b);
// //7.
// let x = "Hello";
// let y = "";
// console.log(!x, !y);
// //8.
// let val = 5;
// let result = !val;
// console.log(result);
//9.
// let a = 10;
// let b = 20;
// let result = !(a && b);
// console.log(result);

//10.
// let x = 0;
// let y = 1;
// let result = !(x || y);
// console.log(result);

//Part-G:typeof Operator
//part-a
//1.
// let name="Rahul"
// console.log(typeof(name))

//2.
// let age=25
// console.log(typeof age)

//3.
// let isStudent = true
// console.log(typeof isStudent)

//4.
// let city;
// console.log(typeof city)

//5.
// console.log(typeof(null))

//6.
// console.log(typeof 42);
// console.log(typeof "Hello");
// console.log(typeof true);
// console.log(typeof undefined);
// //7.
// console.log(typeof null);
// console.log(typeof {});
// console.log(typeof []);
// //8.
// console.log(typeof NaN);
// console.log(typeof Infinity);
// console.log(typeof function(){});
// //9.
// console.log(Boolean(0));
// console.log(Boolean(""));
// console.log(Boolean("0"));
// console.log(Boolean([]));
// console.log(Boolean({}));
// console.log(Boolean(null));

// // //10.
// console.log(String(100));
// console.log(String(true));
// console.log(String(null));
// console.log(String(undefined));
// console.log(100 + "");

// //11.
// console.log("5" + 3 + 2);
// console.log(5 + 3 + "2");
// console.log("5" - 3 + 2);
// console.log(5 - "3" + "2");

// //12.
// console.log(true + true);
// console.log(true + false);
// console.log(true + "false");
// console.log(false + "true");

// //13.
// console.log(null + 5);
// console.log(undefined + 5);
// console.log(null + "5");
// console.log(undefined + "5");

// //14.
// console.log([] + []);
// console.log([] + {});
// console.log({} + []);
// console.log({} + {});

//15.
// let a = "10";
// let b = 5;
// let c = a + b;
// let d = a - b;
// let e = +a + b;
// console.log(c, typeof c);
// console.log(d, typeof d);
// console.log(e, typeof e);

// //16.
// console.log(!!"Hello");
// console.log(!!"");
// console.log(!!0);
// console.log(!!1);
// console.log(!!null);
// console.log(!!undefined);

// //17.
// console.log(Number(""));
// console.log(Number(" "));
// console.log(Number("0"));
// console.log(Number("  25  "));
// console.log(Number("25px"));

// //18.
// let val1 = "5";
// let val2 = 2;
// console.log(val1 + val2);
// console.log(+val1 + val2);
// console.log(val1 - val2);
// console.log(val1 * val2);
// console.log(val1 / val2);

// //19.
// let count = 5;
// console.log(typeof count++);
// console.log(count);
// console.log(typeof ++count);
// console.log(count);

// //20.
// let x = "10";
// let y = ++x;
// console.log(x, y, typeof x, typeof y);

// //21.
// let a = "5";
// let b = a++;
// console.log(a, b, typeof a, typeof b);

// //22.
// console.log(typeof (1 + "2"));
// console.log(typeof (1 - "2"));
// console.log(typeof (1 * "2"));
// console.log(typeof (1 / "2"));

// //23.
// let val = null;
// console.log(typeof val);
// console.log(val + 1);
// console.log(val - 1);
// console.log(val * 1);
// console.log(Boolean(val));