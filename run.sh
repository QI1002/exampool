g++ -std=c++11 -std=c++0x $1 -o a.exe && ./a.exe ${@:2} && sleep 1 && rm a.exe
