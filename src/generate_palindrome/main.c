#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    FILE *new_file;

    char alphabet[] = "abcdefghijklmnopqrstuvwxyz";
    char alphabet_reverse[] = "zyxwvutsrqponmlkjihgfedcba";
    char character_space[] = " ";

    unsigned long palindrome_size;
    unsigned long count;


    if (argc == 2) {
        palindrome_size = strtoul(argv[1], NULL, 10);
    } else {
        if (argc > 2) {
            printf("Error: Too many arguments supplied.\n");
        } else {
            printf("Error: One argument expected.\n");
        }
        printf("Example: ./generate_palindrome 12\n");
        return -1;
    }

    if (palindrome_size < 1) {
        printf("Error: The size of the palindrome should be greater than 0.\n");
        return 0;
    }

    printf("Creating palindrome...\n");
    printf("Size: %lu\n", palindrome_size);

    new_file = fopen("./palindrome.txt", "w");

    for (count = 1; count <= palindrome_size; count++) {
        fputs(alphabet, new_file);
    }

    fputs(character_space, new_file);

    for (count = 1; count <= palindrome_size; count++) {
        fputs(alphabet_reverse, new_file);
    }

    fclose(new_file);

    printf("Finished!\n");

    return 0;
}
