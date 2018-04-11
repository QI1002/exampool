
//1. Write a function to output the result (e.g. “t--es”) based on the puzzle and the guess.
//2. Assume you are given a library function scoreWithPuzzle(string guess, string& result), which scores your guess automatically. Create a game to find the puzzle by results from scoreWithPuzzle()
// minimize calls to scoreWithPuzzle()
// try to be fast
//3. if puzzle.size() = n
//avg = 1/(26^n) * (1*(1^n-0^n)+2*(2^n-1^n)+... 26*(26^n-(25)^n))

#include <vector>
#include <set>
#include <string>
#include <iostream>
#include <math.h>
#include <time.h>

using namespace std;
void scoreWithPuzzle(string guess, string& result);

// p => puzzle
// g => guess 
// a => answer 
void scoreWithPuzzle(string &p, string &g, string &a)
{
    a = "";
    int i;
    for(i = 0; i < p.size() && i < g.size(); i++)
    { 
        if (p[i] == g[i]) a += p[i];
        else a += '-'; 
    }

    for(; i < p.size(); i++) a += '-';
}

int game(string &puzzle, string &result)
{
    const int count = 26;
    int calls = 0;
    string guess;
    result = "";
    int match;
    for(int i = 0; i < puzzle.size(); i++) result += "-";
    
    do
    { 
        guess = result;
        for(int i = 0; i < puzzle.size(); i++)
        {
	    if (result[i] != '-') continue; 
            if (calls >= count) 
            { cout << "can’t guess this puzzle" << endl; return -1; }
            guess[i] = (char)('a'+ calls);  
        }

        scoreWithPuzzle(puzzle, guess, result); calls++;
        match = 0;
        for(int i = 0; i < puzzle.size(); i++) 
            if (result[i] != '-') match++;

	cout << calls << "(" << match << "):" << result << endl;
    }while(match != puzzle.size());

    return true;
}


int main(int argc, char* argv[])
{
    const int count = 26;
    int n = 5;
    string puzzle = "     ";   
    srand((unsigned int)time(NULL));
    for(int i = 0; i < n; i++) puzzle[i] = (char)('a'+(rand()%count)); 

    string result;
    int r = game(puzzle, result);
    if (r > 0) 
    {
        if (result == puzzle) cout << "guess " << puzzle << " right" << endl;
        else cout << "guess " << puzzle << " wrong" << endl;
    }else
    {
        cout << "can’t guess " << puzzle << endl;
    }

    return 0;
}
    


