double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int first = 0, second = 0;
    int merged_index = 0, merged_size = nums1Size + nums2Size;
    int merged[merged_size];

    while ((first < nums1Size) && (second < nums2Size)) {
        if (nums1[first] < nums2[second]) {
            merged[merged_index] = nums1[first];
            first++;
        }
        else {
            merged[merged_index] = nums2[second];
            second++;
        }
        merged_index++;
    }
    
    for (int i = first; i < nums1Size; i++) {
        merged[merged_index] = nums1[i];
        merged_index++;
    }
    for (int i = second; i < nums2Size; i++) {
        merged[merged_index] = nums2[i];
        merged_index++;
    }

    float median;
    if (merged_size % 2 != 0) {
        median = merged[merged_size / 2] / 1.0;
    }
    else {
        int a = merged[merged_size / 2];
        int b = merged[(merged_size / 2) - 1];
        median = (a + b) / 2.0;
    }
    return median;
}