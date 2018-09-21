# NS-SockAssgnmt-TestCases
Some test cases for the NetSec Socket Assignment (UNO game)

## How to use VerifyOutput.py
1) **Prerequisites**:\
Download the files _VerifyOutput.py_ and _expectedOutput.txt_. These two files must be in the same directory. Ensure that you have Python2 installed on your system.
2) **Preparing the input file for _VerifyOutput.py_**: \
    Open two terminals. On one, enter the following command:-
	
    `netcat -l port-number > OutputFilename` \
    Eg: `netcat -l 65000 > output.txt`
      
  	This creates a TCP server which listens on port 65000 and whatever the process receives is written to the file _output.txt_.
  
  	On the second terminal, run your client program, like so:-\
    `python2 client.py localhost port-number`\
    Note: The _"port-number"_ should be the same as the on you mentioned in the netcat command. In our example, your command would be:-\
    Eg: `python2 client.py localhost 65000`
	
  	Now copy the first line from the file _testCases.txt_ (which is the first test case), paste it on the server terminal and press enter. Do this for all test cases; line by line, starting from the very first line in the file _testCases.txt_.
	When you are done entering all the test cases, type 0 and press enter on the server terminal. When you do so, your client program should exit cleanly, i.e., without any errors or exceptions. You may close both the terminals at this point.
	
3) **Verifying the output of your client program**\
	On a terminal, change your present working directory to where _VerifyOutput.py_ and _expectedOutput.txt_ are present. Then, run the following command:-
	
	`python2 VerifyOutput.py OutputFilename`
	
	_"OutputFilename"_ would be the same file name which you had given while starting the server process. For our example, the command would be:-\
	Eg: `python2 VerifyOutput.py output.txt`
	
	The program will display whether your program passed all the test cases or not.\
	If the message displayed is `The program passed all the test cases!!`; then your program is fine and you can upload your solution to autolab.\
	Else, if you get a message saying `The program failed for the following test case(s)`, then you would also be shown the test case numbers which your program failed.\
	The first test case is on the first line of the file _testCases.txt_, the second test case on the second line and so on. Try debugging your code with the test case(s) for which your solution failed.
	
