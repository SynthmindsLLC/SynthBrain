[Wes Roth Video](https://www.youtube.com/watch?v=Cl19yWHhc2g&t=598s)

# 1. Set Up Environment

1. Download [Python](https://www.python.org/downloads/)
2. Download [Anaconda](https://www.anaconda.com/download)
3. Open Anaconda Prompt (can find in your search bar) - This is a terminal
4. In Terminal type after ">"
```
conda create -n [INSERT NAME] python=3.9
```
and hit "Enter"
5. Type "y" to proceed

# 2. Activating Autogen
1. In the Terminal type after ">"
```
conda activate [INSERT NAME]
```
Press "Enter"

2. In the Terminal type after ">"
```
pip install pyautogen
```
Press "Enter"

3. In the Terminal type after ">"
```
pip install autogenstudio
```
Press "Enter"

4. Get your API key from OpenAI and in the Terminal type after ">"
```
FOR PC TYPE:
set OPENAI_API_KEY=[INSERT KEY]

FOR MAC TYPE:
export OPENAI_API_KEY=[INSERT KEY]
```

5. In the Terminal type after ">"
```
autogenstudio ui --port 8081
```

6. Open the studio by copy and pasting the local address into your preferred web browser. It should look like something below:
```
http://123.0.0.1:8081
```