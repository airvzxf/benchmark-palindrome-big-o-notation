#!/bin/bash -xve

SCRIPT_PATH="$(cd -P -- "$(dirname -- "$0")" && pwd -P)"



#DEBUG_PATH=${SCRIPT_PATH}/cmake-build-debug
#rm -fR ${DEBUG_PATH}
#mkdir -p ${DEBUG_PATH}
#cd ${DEBUG_PATH}
#cmake -DCMAKE_BUILD_TYPE=Debug ../
#cmake --build ./ --target generate_palindrome -- -j 4
#cd ${SCRIPT_PATH}



RELEASE_PATH=${SCRIPT_PATH}/cmake-build-release
rm -fR ${RELEASE_PATH}
mkdir -p ${RELEASE_PATH}
cd ${RELEASE_PATH}
cmake -DCMAKE_BUILD_TYPE=Release ../
cmake --build . --target generate_palindrome -- -j 4
cd ${SCRIPT_PATH}



cd ${RELEASE_PATH}
./generate_palindrome 1
mv palindrome.txt 00-tiny.txt

./generate_palindrome 1000
mv palindrome.txt 01-small.txt

./generate_palindrome 100000
mv palindrome.txt 02-medium.txt

./generate_palindrome 1000000
mv palindrome.txt 03-big.txt

./generate_palindrome 10000000
mv palindrome.txt 04-huge.txt

./generate_palindrome 100000000
mv palindrome.txt 05-immense.txt
