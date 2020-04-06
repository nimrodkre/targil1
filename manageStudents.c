/**
 * @file main.c
 * @author  Nimrod Kremer <nimrod.kremer@.mail.huji.ac.il>
 * @version 1.0
 * @date 6 April 2020
 *
 * @brief Ex1
 *
 * @section LICENSE
 * This program is not a free software; bla bla bla...
 *
 * @section DESCRIPTION
 * Ex 1
 */

#include <stdio.h>
#include <string.h>

#define USAGE_ARGUMENTS 2
#define MAX_STUDENTS 5500
#define MAX_STRING_LEN 42
#define MAX_LINE_LEN 60
#define EXPECTED_ARGUMENTS 6
#define ID_DIGITS 10
#define MIN_GRADE 0
#define MAX_GRADE 100
#define MIN_AGE 18
#define MAX_AGE 120
#define START_BEST "best"
#define START_QUICK "quick"
#define START_MERGE "merge"
/**
 * Structs which holds the Student data
 * ID - long ID
 * name - name of student - string
 * grade - int
 * age - int
 * country - string
 * city - string
 */
typedef struct Student
{
    long id;
    char name[MAX_STRING_LEN];
    int grade;
    int age;
    char country[MAX_STRING_LEN];
    char city[MAX_STRING_LEN];
} Student;

int getStudents(Student students[]);

Student getStudent(int *lineNumber);

unsigned int countDigits(long num);

int checkId(long id);

int checkGrade(int grade);

int checkAge(int age);

int checkName(char name[]);

int checkCountryCity(char countryCity[]);

int checkCity(char city[]);
;
int checkCountry(char country[]);

int checkData(int sscanfResult, long id, char name[], int grade, int age,
              char country[], char city[]);

void printBest(Student students[], int arrLen);

void mergeSort(Student students[], int left, int right);

void merge(Student students[], int left, int middle, int right);

void swap(Student students[], int left, int right);

void swap2(Student students1[], Student students2[], int left, int right);

void quickSort(Student students[], int left, int right);

int partition(Student students[], int left, int right);

void printAllStudents(Student students[], int numStudents);

int runBest(void);

int runMerge(void);

int runQuick(void);

/*************************************************************************************/

/**
 * Checks that the data result is legal
 * @param sscanfResult the parameter returned by sscan
 * @param id This ID of the student
 * @param name the name of the student
 * @param grade the grade of the strudent
 * @param age the age of the student
 * @param country the country of the student
 * @param city the city of the student
 * @return 0 is bad else 1 if good
 */
int checkData(int sscanfResult, long id, char name[], int grade, int age,
              char country[], char city[])
{
    if (sscanfResult != EXPECTED_ARGUMENTS)
    {
        printf("ERROR: info must match specified format\n");
        return 0;
    }

    if (checkId(id) == 0)
    {
        return 0;
    }

    if (checkName(name) == 0)
    {
        return 0;
    }

    if (checkGrade(grade) == 0)
    {
        return 0;
    }

    if (checkAge(age) == 0)
    {
        return 0;
    }

    if (checkCountry(country) == 0)
    {
        return 0;
    }

    if (checkCity(city) == 0)
    {
        return 0;
    }

    return 1;
}

/**
 * Counts the number of digits in the given number
 * @param num the number to check
 * @return the number of digits in the number
 */
unsigned int countDigits(long num)
{
    unsigned int count = 0;

    do
    {
        count++;
        num /= 10;
    } while (num != 0);

    return count;
}

/**
 * Checks if the given ID is legal
 * @param id the id to check
 * @return 1 if good else 0
 */
int checkId(long id)
{
    unsigned int numDigits = countDigits(id);

    if (numDigits != ID_DIGITS)
    {
        printf("ERROR: id must be a 10 digits number that does not start with 0\n");
        return 0;
    }
    return 1;
}

/**
 * Checks if teh given grade is legal
 * @param grade the grade to check
 * @return 1 if good else 0
 */
int checkGrade(int grade)
{
    if ((grade < MIN_GRADE) || (grade > MAX_GRADE))
    {
        printf("ERROR: grade must be an integer between 0 and 100\n");
        return 0;
    }
    return 1;
}

/**
 * Checks if the given age is good
 * @param age the age to check
 * @return 1 if good else 0
 */
int checkAge(int age)
{
    if ((age < MIN_AGE) || (age > MAX_AGE))
    {
        printf("ERROR: age must be an integer between 18 and 120\n");
        return 0;
    }
    return 1;
}

/**
 * Checks if the given name is legal
 * @param name the name to check
 * @return 1 if good else 0
 */
int checkName(char name[])
{
    unsigned long len = strlen(name);
    if (len < 1)
    {
        printf("ERROR: name can only contain alphabetic characters, whitespaces or '-'\n");
        return 0;
    }
    for (unsigned long i = 0; i < len; i++)
    {
        if (!((name[i] >= 'A' && name[i] <= 'z') || (name[i] == '-') || (name[i] == ' ')))
        {
            printf("ERROR: name can only contain alphabetic characters, whitespaces or '-'\n");
            return 0;
        }
    }

    return 1;
}

/**
 * Checks if the given string for country or city is legal
 * @param countryCity the country or city to check
 * @return 1 if good else 0
 */
int checkCountryCity(char countryCity[])
{
    unsigned long len = strlen(countryCity);
    if (len < 1)
    {
        return 0;
    }
    for (unsigned long i = 0; i < len; i++)
    {
        if (!((countryCity[i] >= 'A' && countryCity[i] <= 'z') || (countryCity[i] == '-')))
        {
            return 0;
        }
    }

    return 1;
}

/**
 * checks city
 * @param city city to check
 * @return  0if bad else 1
 */
int checkCity(char city[])
{
    if (checkCountryCity(city) == 0)
    {
        printf("ERROR: city can only contain alphabetic characters or '-'\n");
        return 0;
    }
    return 1;
}

/**
 * checks country
 * @param country checks the given country
 * @return  0 if bad else 1
 */
int checkCountry(char country[])
{
    if (checkCountryCity(country) == 0)
    {
        printf("ERROR: country can only contain alphabetic characters or '-'\n");
        return 0;
    }
    return 1;
}

/**
 * Gets the user data for the student from the user
 * @param lineNumber the line number of the whole system
 * @return a legal student
 */
Student getStudent(int *lineNumber)
{
    Student student = {0, "", 0, 0, "", ""};
    int answer = 0;

    while (answer != 1)
    {

        char input[MAX_LINE_LEN];

        printf("Enter student info. To exit press q, then enter\n");
        fgets(input, sizeof(input), stdin);

        // check if q was received
        if (strncmp(input, "q", 1) == 0)
        {
            Student retStudent = {0, {'a'}, 0, 0, {'a'}, {'a'}};
            return retStudent;
        }

        // remove newline
        unsigned long len = strlen(input);
        if (input[len - 1] == '\n')
        {
            input[len - 1] = 0;
        }

        int sscanfResult = sscanf(input, "%ld,%[^,],%d,%d,%[^,],%[^,]", &student.id, student.name,
                                  &student.grade, &student.age, student.country, student.city);

        if (!checkData(sscanfResult, student.id, student.name, student.grade, student.age, student.country,
                       student.city))
        {
            printf("in line %d\n", *lineNumber);
            answer = 0;
        }
        else
        {
            answer = 1;
        }
        (*lineNumber)++;
    }

    return student;
}

/**
 * Gets a list of students
 * @param students An array to fill with students
 * @return the number of students gotten
 */
int getStudents(Student students[])
{
    int numStudents = 0;
    int lineNumber = 0;
    Student student = getStudent(&lineNumber);

    while (student.age != 0)
    {
        students[numStudents] = student;
        numStudents++;
        student = getStudent(&lineNumber);
    }

    return numStudents;
}

/**
 * Finds and prints the best student
 * @param students students to check
 * @param arrLen how many students in the array
 */
void printBest(Student students[], int arrLen)
{
    Student retStudent = {0, {'a'}, 0, 0, {'a'}, {'a'}};
    double best = -1;

    for (int i = 0; i < arrLen; i++)
    {
        double score = (double) (students[i].grade) / students[i].age;
        if (score > best)
        {
            best = score;
            retStudent = students[i];
        }
    }
    if (retStudent.age == 0)
    {
        return;
    }
    printf("best student info is: %ld,%s,%d,%d,%s,%s\n", retStudent.id, retStudent.name, retStudent.grade, retStudent.age,
           retStudent.country, retStudent.city);
}

/**
 * Runs the best algorithm
 * @return 0 if worked
 */
int runBest(void)
{
    Student students[MAX_STUDENTS];

    int numStudents = getStudents(students);
    printBest(students, numStudents);

    return 0;
}

/**
 * Prints all of the students given in the list
 * @param students an array with all of the students
 * @param numStudents how many students in the array
 */
void printAllStudents(Student students[], int numStudents)
{
    for (int i = 0; i < numStudents; i++)
    {
        if (students[i].age == 0)
        {
            continue;
        }
        printf("%ld,%s,%d,%d,%s,%s\n", students[i].id, students[i].name, students[i].grade, students[i].age,
               students[i].country, students[i].city);
    }
}

/**
 * Swaps between the 2 given array indexes
 * @param students an array with all of the students
 * @param left first index
 * @param right second index
 */
void swap(Student students[], int left, int right)
{
    Student temp = students[left];
    students[left] = students[right];
    students[right] = temp;
}

/**
 * swaps between the two given students from different arrays
 * @param students1 array 1
 * @param students2 array 2
 * @param left loc of array 1
 * @param right loc of array 2
 */
void swap2(Student students1[], Student students2[], int left, int right)
{
    Student temp = students1[left];
    students1[left] = students2[right];
    students2[right] = temp;
}

/**
 * merge function for merge sort
 * @param students an array with all of the students
 * @param left the most left index
 * @param middle middle index
 * @param right right index
 */
void merge(Student students[], int left, int middle, int right)
{
    int sizeLeft = middle - left + 1;
    int sizeRight = right - middle;
    int currLeft = 0;
    int currRight = 0;
    Student studentsLeft[sizeLeft];
    Student studentsRight[sizeRight];
    for (int i = 0; i < sizeLeft; i++)
    {
        studentsLeft[i] = students[left + i];
    }
    for (int j = 0; j < sizeRight; j++)
    {
        studentsRight[j] = students[middle + j + 1];
    }

    while ((currLeft + currRight) < (sizeLeft + sizeRight))
    {
        if (currLeft == sizeLeft)
        {
            swap2(students, studentsRight, left + currLeft + currRight, currRight);
            currRight++;
        }
        else if (currRight == sizeRight)
        {
            swap2(students, studentsLeft, left + currLeft + currRight, currLeft);
            currLeft++;
        }
        else
        {
            if (studentsLeft[currLeft].grade <= studentsRight[currRight].grade)
            {
                swap2(students, studentsLeft, left + currLeft + currRight, currLeft);
                currLeft++;
            }
            else
            {
                swap2(students, studentsRight, left + currLeft + currRight, currRight);
                currRight++;
            }
        }
    }
}

/**
 * does the merge sorrt
 * @param students array of students
 * @param left first index to start from the sort
 * @param right the second index from which we will finish the sort
 */
void mergeSort(Student students[], int left, int right)
{
    if (left >= right)
    {
        return;
    }

    int middle = 0;
    middle = left + ((right - left) / 2);
    mergeSort(students, left, middle);
    mergeSort(students, middle + 1, right);
    merge(students, left, middle, right);
}

/**
 * runs the merge sort algoirthm
 * @return 0
 */
int runMerge(void)
{
    Student students[MAX_STUDENTS];
    int numStudents = 0;

    numStudents = getStudents(students);
    mergeSort(students, 0, numStudents - 1);
    printAllStudents(students, numStudents);

    return 0;
}

/**
 * runs the quick sort algorithm
 * @param students array of students
 * @param left the starting sort index
 * @param right the last index
 */
void quickSort(Student students[], int left, int right)
{
    if (left >= right)
    {
        return;
    }
    int currentPos = partition(students, left, right);
    quickSort(students, left, currentPos - 1);
    quickSort(students, currentPos + 1, right);
}

/**
 * partition algorithm for quicksort
 * @param students students array
 * @param left the most left index to start from
 * @param right the last index to finish from
 * @return 0
 */
int partition(Student students[], int left, int right)
{
    char *pivot = students[right].name;
    int currentSwap = left;

    for (int i = left; i < right; i++)
    {
        if (strcmp(students[i].name, pivot) < 0)
        {
            swap(students, currentSwap, i);
            currentSwap++;
        }
    }
    swap(students, currentSwap, right);
    return currentSwap;
}

/**
 * Runs the quick sort algorithm
 * @return  0
 */
int runQuick(void)
{
    Student students[MAX_STUDENTS];
    int numStudents = 0;

    numStudents = getStudents(students);
    quickSort(students, 0, numStudents - 1);
    printAllStudents(students, numStudents);

    return 0;
}

/**
 * The main of the program
 * @param argc number of user arguments
 * @param argv the arguments
 * @return 0 if good else 1
 */
int main(int argc, char *argv[])
{
    runMerge();
    if (argc != USAGE_ARGUMENTS)
    {
        printf("USAGE: sortStudents <action>\n");
        return 1;
    }

    if (strcmp(argv[1], START_BEST) == 0)
    {
        runBest();
        return 0;
    }

    if (strcmp(argv[1], START_MERGE) == 0)
    {
        runMerge();
        return 0;
    }

    if (strcmp(argv[1], START_QUICK) == 0)
    {
        runQuick();
        return 0;
    }

    printf("USAGE: sortStudents <action>\n");
    return 1;
}
