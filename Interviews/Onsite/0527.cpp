  
#include <algorithm>
#include <iostream>
#include <utility>

#include <cstring>
#include <climits>
#include <ostream>
#include <sstream>
#include <list>
#include <string>
#include <deque>
#include <vector>
#include <memory>
#include <functional>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>

using namespace std;

static void add(char **num, int n) {  
  char *source = *num;
  int c = 0;
  for(int i = strlen(source)-1; i >= 0; --i) {
     c += n % 10; n = n/10;
     c += source[i]-'0'; 
     if (c >= 10) {
         source[i] = '0'+c-10;
         c = 1; 
     } else {
         source[i] = '0'+c;
         c = 0;
     }
  }
  n += c;
  if (n) {
     string s = to_string(n); 
     char* d = (char*)malloc(strlen(source)+s.length());
     memcpy(d, s.c_str(), s.length());
     memcpy(d+s.length(), source, strlen(source)*sizeof(char));
     *num = d;
  }  
}

static void sub(char **num, int n) {
  int val = 1, a = 0;
  char *source = *num;
  for(int i = strlen(source)-1; i >= 0; --i, val *= 10) {
    a = (source[i]-'0')*val;
    if (a >= n) { 
        a -= n;
        memset(source+i, '0', strlen(source)-i);
        string s = to_string(a);
        memcpy(source+(strlen(source)-s.length()), s.c_str(), s.length());
        break;   
    } else {
        n -= a;
    }
  }

  for(a = 0; a < strlen(source)-1; ++a) {
      if (source[a] != '0') break;
  }
  *num = source+a;
}


bool validate_args(int argc, char **argv) {
  if (argc != 3) return false;
  for(int i = 1; i < 3; ++i) {
    for(int j = strlen(argv[i])-1; j >= 0; --j) {
      if (argv[i][j] < '0' || argv[i][j] > '9') 
        return false;  
    }
  }
  return true;
}

static void add2(char **num, int n) {
  char *s = *num;
  int t = max((int)strlen(s), 32)+1;
  char* result = new char[t];
  int i, j = t-1, c = 0;

  for(i = strlen(s)-1; n || i >= 0; --i, n /= 10) {
    c += (n % 10 + ((i < 0) ? 0 : s[i]-'0'));
    if (c >= 10) { result[--j] = '0'+c-10; c = 1; } 
    else { result[--j] = '0'+c; c = 0; }
  }
  if (c) result[--j] = '0'+c;
  if (t) {
    for(i = 0; j < t; ++j, ++i) result[i] = result[j];
    result[i] = 0;
  }
  *num = result;
}

static void sub2(char **num, int n) {
  long long a = 1, b = n;
  for(n = 0; a < b; a *= 10, ++n);
  b = a-b; 
  add2(num, (int)b);
  char *s = *num;
  for (n = strlen(*num)-n-1; n >= 0; --n) {
    if (s[n] != '0') { --s[n]; break; }
    s[n] = '9';
  }

  for(n = 0; s[n] == '0' && n < strlen(s)-1; ++n);
  if (n) {
    int i; 
    for(i = 0; n < strlen(s); ++n, ++i) s[i] = s[n];
    s[i] = 0;
  }
}

int main(int argc, char **argv) {
  // Make sure argv[1] is a non-negative integer string, and argv[2] is an integer.
  if (!validate_args(argc, argv)) {
    printf("usage: <non-negative integer> <integer>\n");
    return -1;
  }

  char *num = strdup(argv[1]);
  int n = atoi(argv[2]);
  char* result = num;

  //add(&num, n); // When num="678",  n=2 => "680"
  //sub(&result, n); // When num="678",  n=79 => "599"

  //add2(&result, n);
  sub2(&result, n);

  printf("%s\n", result);
  free(num);
  return 0;
}

