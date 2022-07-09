RECURSION

What is recursion within programming?
- A function repeatedly calling itself until a specified condition is met.

Why is it useful?
- It simplifies the code needed for complex tasks such as graph and tree traversal.
- Personally it also looks cooler than a loop :)

Efficiency
- Less efficient on small amounts of data due to overhead of calling a function
- Can increase efficiency of recursive algorithm by switching to a different algorithm when the input becomes small (more efficient, but increases complexity of the code)

Pieces of Recursive Function
- Function definition with input(s)
- A break case for when a certain condition is met
- Calling itself until the break case is met
- voiceover
  - To create a recursive function there are 3 basic steps to follow. First, define a function that usually takes in one or more inputs. Second, define a break case for when a certain condition is met. This will tell the code to cease execution because it found what it is looking for. And third, it will call itself until the break case is met.
  - Here's an example. In the first image we define a function called "factorial" that takes in a variable "n", in this case it will be an integer. In the second image we define a break case for the function to return 2 if "n" is 2. And lastly, if "n" is not 2, we tell the function to call itself with "n" minus 1, and multiply the returned value by "n".
  - Here you can see the steps the function takes to arrive at the desired solution. Say we initialize the recursion by calling factorial where "n" equals 6. The function is going to identify 6 as not equaling 2, and say, "okay, I want to return the factorial of 6 minus 1, multiplied by 6." Then the function called with 5 is going to identify 5 as not equaling 5 and say, "okay, I want to return the factorial of 5 minus 1, multiplied by 5." The same will occur for the cases of 4 and 3. Once it arrives at 2, the function is going to say, "okay, n equals 2, so I want to return 2." Then the value gets passed back up the chain. 2 is multiplied by 3, resulting in 6. Then 6 is multiplied by 4 resulting in 24. Twenty-four is multiplied by 5 resulting in 120. And finally 120 is multiplied by 6 resulting in 720.

Iterative Alternative
- Although recursion works for this particular problem, it is not necessary. Calculating a factorial is easy enough with a loop, and without the overhead of a function call it is actually more efficient.

Binary Search
- Let's take a look at another example of recursion. In this case we will be writing a binary search algorithm. A binary search algorithm takes a sorted array or list and splits it in half over and over again until it finds the target value. Each time it splits the array in half, it determines if the value it is searching for is in the left half, or the right half, then continues searching in that section.
- In this implementation our recursive function takes in a sorted array, a starting index, an ending index, and a target value to find. It then calculates the center point of the array based upon the two indices passed in. If the value in the middle of the sorted array starting at "start index" and ending at "end index" matches the target value, then it returns a little message. This is the break case. If not, then it continues. If the target value is lower than the value in the middle of the sorted array, then perform a binary search on the left side of the array. If the target value is higher than the value in the middle of the sorted array, then perform a binary search on the right side of the array.
- Let's walk through the path the binary search takes. We initialize the recursion with an array of five elements. The "start index" has a value of zero, the "end index" has a value of 4 (length of array minus 1), and is looking for the number five. It calculates the midpoint of the array, in this case two. Since the value at index two, in this case the number 3, is not equal to our target value of five, it does not return our little message. It then determines if the target value is to the left or right of the midpoint value. In this case the value is to the right, so it calls binary search again with the same array and target value, but now "start index" is three and "end index" is four. Again it calculates the midpoint and checks the middle value against the target value. Then it determines the target value is to the right of the midpoint.
- This time it performs a binary search on the values between index four, and index four. This is a list with a single element, the number five. Since five matches our target, our little message is returned.