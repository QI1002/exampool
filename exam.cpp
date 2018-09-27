    t.insertse use this Google doc to code during your interview. To free your hands for coding, we recommend that you use a headset or a phone with speaker option.



Guess word game
Puzzle: tires:
Guess 1: fever: ---e-
Guess 2: tales: t--es
…
…
tires

Write a function to output the result (e.g. “t--es”) based on the puzzle and the guess.

#include <string>

using namespace std;

// p => puzzle
// g => guess 
// a => answer 
void scoreWithPuzzle(string &p, string &g, string &a)
{
    a = “”;
    int i;
    for(i = 0; i < p.size() && i < g.size(); i++)
    { 
        if (p[i] == g[i]) a += p[i];
        else a += ‘-’; 
    }

    for(; i < p.size(); i++) a += ‘-’;
}


2. Assume you are given a library function scoreWithPuzzle(string guess, string& result), which scores your guess automatically. Create a game to find the puzzle by results from scoreWithPuzzle()
minimize calls to scoreWithPuzzle()
try to be fast

#incldue <vector>
#include <string>
#include <iostream>
#include <rand.h>
#include <time.h>

using namespace std;
void scoreWithPuzzle(string guess, string& result);
bool game(string &puzzle, string &result)
{
    vector<vector<int>> check;
    const int count = 26;
    
    vector<int> vi(count, -1);
    for(int i = 0; i < puzzle.size(); i++) 
        check.emplace_back(vi);
    
    string guess;
    result = “”;
    int match;
    for(int i = 0; i < puzzle.size(); i++) result += “-”;
    do
    { 
        guess = result;
        for(int i = 0; i < puzzle.size(); i++)
        {
            if (result[i] != ‘-’) continue; 
            for(int j = 0; j < count; j++) 
                if (check[i][j] == -1) break;
            if (j >= count) 
            { cout << “can’t guess this puzzle” << endl; return false; }
            guess[i] = (char)(’a’+j);  
        }

        scoreWithPuzzle(guess, result);
        match = 0;
        for(int i = 0; i < puzzle.size(); i++) 
        {    
            if (result[i] == ‘-’) 
            { check[i][guess[i]-’a’] = 0; continue; }
            match++; 
            check[i][guess[i]-’a’] = 1;
        } 
    }while(match != puzzle.size());

    return true;
}


void testPuzzle()
{
    
    const int count = 26;
    int n = 5;
    string puzzle = “     ”;  
    srand((unsigned int)time(NULL));
    for(int i = 0; i < n; i++) puzzle[i] = (char)(‘a’+(rand()%count)); 

    string result;
    bool r = game(puzzle, result);
    if (r == true) 
    {
        if (result == puzzle) cout << “guess “ << puzzle << “ right” << endl;
        else cout << “guess “ << puzzle << “ wrong” << endl;
    }else
    {
        cout << “can’t guess ” << puzzle << endl;
    }
}
    

sorry, the average guess times of scoreWithPuzzle() is supposed be more than 13 but less than or equal to 26 due to if one char is not guessed, we shall continue to guess.

The average times can be estimated by possibility 
if puzzle.size() = n

avg = 1/(26^n) * (1*(1^n-0^n)+2*(2^n-1^n)+... n*(n^n-(n-1)^n))
 
(t.begin(), -1);

