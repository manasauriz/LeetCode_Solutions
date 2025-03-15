#include <string.h>

int lengthOfLongestSubstring(char* s) {
    int arr[130];
    for (int i = 0; i < 130; i++) {
        arr[i] = -1;
    }

    int start = 0, end = 0, max = 0;
    while (end < strlen(s)) {
        int end_char = s[end];
        int end_index = arr[end_char];

        if ((start <= end_index) && (end_index <= end)) {
            start = end_index + 1;
        }
        arr[end_char] = end;
        end += 1;
        max = ((end - start) > max) ? (end - start) : max;
    }
    return max;
}