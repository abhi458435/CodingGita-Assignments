// ## # 1. What Is an Array?
//Ans:-Array is collection of Different Data types Value
// 1. What is the definition of an array in JavaScript?
//Ans:-An array is a special JavaScript data structure used to store a list of values
// 2. What is the technical term for the position of a value inside an array?
//Ans:- Index
// 3. At which number does the index of an array always start?
//Ans:- 1
// 4. Given the array `var numbers = [10, 20, 30, 40];`, what value is stored at index `2`?
//Ans:- 30
// 5. For the same array `var numbers = [10, 20, 30, 40];`, what is the index of the number `40`?
//Ans:- 3

// ## # 2. Creating Arrays
// 1. What are the two ways mentioned in the notes to create an array in JavaScript?
//Ans:- (i)Using Square Brackets, (ii)Using new Array keyword 
// 2. Which method of creating an array is recommended by the notes?
//Ans:-Using Square Brackets
// 3. Write the syntax to create an array named `students` containing the names `"Jenil"`, `"Mahir"`, `"Priyesha"`, and `"Yashvi"` using the recommended method.
//Ans:-
// var students=["Jenil", "Mahir", "Priyesha","Yashvi"]
// console.log(students)
// 4. Write the syntax to create an array named `marks` containing `85`, `90`, and `78` using the `Array` constructor.
//Ans:-
// var marks=new Array(85,90,78)
// console.log(marks)
// 5. What keyword is used when instantiating an array using the constructor approach?
//Ans:- new Array

// ## # 3. Accessing Values in an Array
// 1. What do you use to access a specific value stored in an array?
//Ans:- Indexing
// 2. Given `var students = ["Jenil", "Mahir", "Priyesha"];`, what does `console.log(students[0]);` output?
//Ans:- jenil
// 3. For the same array, what does `console.log(students[2]);` output?
//Ans:-Priyasha
// 4. What value does JavaScript return if you attempt to access an index that does not exist (such as `students[10]`)?
//Ans:-undefined
// 5. Write a line of code to log the first element of an array named `colors`.
// let colors=["White","Black","Blue","Pink","Yellow"]
// console.log(colors[0])

// ## # 4. Updating Values
// 1. How do you update a specific value inside an existing JavaScript array?
//Ans:-Using Assignment operator ,assign a new value to the old value
// 2. Given `var marks = [80, 75, 90];`, what code would you write to change the second element (`75`) to `95`?
//Ans:-
// var marks = [80, 75, 90]
// marks[1]=95
// console.log(marks)

// 3. After executing the update from the previous question, what will `console.log(marks);` output?
//Ans:-[80,95,90]
// 4. True or False: You need to use a special built-in method like `update()` to change an array element's value.
//Ans:-False
// 5. Can you update a value at an index that is currently outside the bounds of the array? What happens if you assign a value to a much higher index?

