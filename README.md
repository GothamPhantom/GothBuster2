<h1>What is GothBuster2?</h1>
GothBuster2 is basically a directory scanner/finder. It works like this:

1. We are requesting GET from http://{URL}/{words from our wordlists}.
2. We are testing every word from our wordlists to see if there is such directory.
3. If there is a response, the full URL will be printed in the CLI
4. This eases users instead of manually typing each word into the browser search bar.
<hr>
<b>Enter URL input from the user:</b>
<img src="https://i.imgur.com/Ns7P99f.png">
<br>
<b>Enter wordlist path</b>
<img src="https://i.imgur.com/bOZbH7X.png">
<br>
<b>Example of wordlist path. Try to locate your built-in wordlist path using the command `locate {wordlist name}.txt`:</b>
<img src="https://i.imgur.com/gPeWPuH.png">
<br>
<b>Scanning directories:</b>
<img src="https://i.imgur.com/L3Md71W.png">
<img src="https://i.imgur.com/K20tObe.gif">
<br>
<b>Don3!</b>
<img src="https://i.imgur.com/hJESAdg.png">
<img src="https://i.imgur.com/glrnRPw.gif">
<hr>
<h2>How to install and run?</h2>
You can clone the git repo. Here's how you run it:
<br>
`git clone https://github.com/GothamPhantom/GothBuster2.git`
<br>
`cd GothBuster2`
<br>
`python GothBuster2.py`
<hr>
<h2>Note:</h2>
The requirements.txt file should list all Python libraries that your system depends on, and they will be installed using:
<br>
`pip install -r requirements.txt`
<hr>
<h2>License</h2>
The code is licensed under <s>the Gotham's Dent Act License</s>GPL v3 License. Do not be afraid.
