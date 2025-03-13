#include <stdlib.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int carry = 0;

    struct ListNode *result = malloc(sizeof(struct ListNode));
    result->val = 0;  // Placeholder value
    result->next = NULL;
    struct ListNode *current = result;

    while (l1 || l2 || carry)
    {
        int val1 = (l1) ? l1->val : 0;
        int val2 = (l2) ? l2->val : 0;

        int sum = val1 + val2 + carry;
        carry = sum / 10;
        sum = sum % 10;

        struct ListNode *temp = malloc(sizeof(struct ListNode));
        temp->val = sum;
        temp->next = NULL;
        current->next = temp;
        current = temp;

        if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;
    }

    struct ListNode *head = result->next;
    free(result);
    return head;
}