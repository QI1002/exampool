
//1. Write a function to output the result (e.g. “t--es”) based on the puzzle and the guess.
//2. Assume you are given a library function scoreWithPuzzle(string guess, string& result), which scores your guess automatically. Create a game to find the puzzle by results from scoreWithPuzzle()
// minimize calls to scoreWithPuzzle()
// try to be fast
//3. if puzzle.size() = n
//avg = 1/(26^n) * (1*(1^n-0^n)+2*(2^n-1^n)+... 26*(26^n-(25)^n))

#include <vector>
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

bool game(string &puzzle, string &result)
{
    vector<vector<int>> check;
    const int count = 26;
    
    vector<int> vi(count, -1);
    for(int i = 0; i < puzzle.size(); i++) 
        check.emplace_back(vi);
    
    string guess;
    result = "";
    int match;
    for(int i = 0; i < puzzle.size(); i++) result += "-";
    do
    { 
        guess = result;
        for(int i = 0; i < puzzle.size(); i++)
        {
            int j;
	    if (result[i] != '-') continue; 
            for(j = 0; j < count; j++) 
                if (check[i][j] == -1) break;
            if (j >= count) 
            { cout << "can’t guess this puzzle" << endl; return false; }
            guess[i] = (char)('a'+j);  
        }

        scoreWithPuzzle(puzzle, guess, result);
        match = 0;
        for(int i = 0; i < puzzle.size(); i++) 
        {    
            if (result[i] == '-') 
            { check[i][guess[i]-'a'] = 0; continue; }
            match++; 
            check[i][guess[i]-'a'] = 1;
        } 
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
    bool r = game(puzzle, result);
    if (r == true) 
    {
        if (result == puzzle) cout << "guess " << puzzle << " right" << endl;
        else cout << "guess " << puzzle << " wrong" << endl;
    }else
    {
        cout << "can’t guess " << puzzle << endl;
    }

    return 0;
}
    


