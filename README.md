# Swift-Sort-Using-Divide-and-Conquer-Technique
This project relates to the field of design and analysis of algorithms, in particular to a divide-and-conquer based sorting algorithm in sorting an array of elements to achieve quick and efficient sorting of elements.<p>
# Background of Invention
Divide-and-conquer is probably the best-known general algorithm design technique. The time spent on executing the divide-and-conquer plan turns out to be smaller than solving a problem by a different method. The divide-and-conquer approach yield some of the most important and efficient algorithms in computer science like merge sort, quick sort, binary search, etc. which offers several advantages, including modularity, reusability, and the potential for parallelization. The availability of numerous sorting algorithms has accomplished the process of sorting datas and made it easier and much simpler for the programmers in sorting large amount of datasets. These algorithms have been refined over the years, and various optimizations have been introduced to improve their performance in different scenarios. 
The motivation behind the invention of this sorting technique was to overcome the limitations of existing sorting methods that had higher time complexities, space complexities, incapability of handling larger datasets and many more. For example, traditional methods like bubble sort and insertion sort had time complexities of O(N2), which made them inefficient for large datasets.<p>
# Summary of Invention
The objective of this project is to provide a divide-and-conquer approach-based sorting algorithm which offers several advantages, including modularity, reusability, and the potential for parallelization. 
This algorithm takes the first value (104) or second value (105) of the input array as the key element based on the condition (103) and divides the array into two sub-arrays. The left sub-array contains the elements whose values are smaller than that of the key element (106) and the right sub-array contains the elements whose values are greater than or equal to that of the key element (106). And this process continues with the sub-arrays recursively (107). Finally, by default, all the leaf arrays (i.e., the array that contain only one element) will be sorted. All the leaf arrays are merged (108) and produced as the output (109) that is required. 
This algorithm works for the values of different datatypes such as integer (both positive and negative integers), float, double, character and strings, and also with duplicate elements.
The invention of this sorting technique that utilize the divide and conquer approach was driven by the need for faster and more efficient sorting algorithms as computers became more prevalent.<p>
# Flowchart
<img width="1984" height="2164" alt="Flowchart (2)" src="https://github.com/user-attachments/assets/d4676f52-255e-4f73-81e1-a5c66500341c" /><p>
# Detail Description
The flowchart is divided into 11 steps depending on the stage of the process.<p>
Step 1(100) depicts the beginning of the program where the system boots up and loads the project.<p>
Step 2(101) is where the input array is taken from the user. The elements can be of any datatypes such as integer (both positive and negative integers), float, double, character and strings. It can also have duplicate elements.<p>
Step 3(102) is where two empty arrays are created, namely, left sub-array and right sub-array. The left sub-array is used to store the elements whose values are lower than that of the key element. The right sub-array is used to store the elements whose values are higher than or equal to that of the key element.<p>
Step 4(103) checks for the condition that if the value of the first element in the array is minimum of all other elements. If the condition fails, the control proceeds to Step 5(104) of the algorithm. Otherwise, the control proceeds to Step 6(105) of the algorithm.<p>
Step 5(104) takes the first element as the key element and proceeds to Step 7(106).<p>
Step 6(105) takes the second element as the key element and proceeds to Step 7(106).<p>
Step 7(106) is where the elements, whose values are lower than that of the key element, is appended into the left sub-array and the elements, whose values are higher than or equal to that of the key element, is appended into the right sub-array.<p>
Step 8(107) checks for the condition that if the length of left sub-array and that of right sub-array is equal to 1. If true, the control proceeds to Step 9(108). Otherwise, the control will go back to Step 3(102) and the process continues recursively.<p>
Step 9(108) just merges all the leaf arrays (i.e., arrays with only one element) as all the leaf arrays, by default, will already be sorted.<p>
Step 10(109) displays the sorted array which is the required output.<p>
Step 11(110) the user can close the program once they are done with its usage and this will end all its functionalities and end the program’s RAM usage.<p>



