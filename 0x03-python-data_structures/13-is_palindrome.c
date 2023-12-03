#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list. */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/* Function to reverse a linked list */
listint_t *reverse_list(listint_t *head) {
    listint_t *prev = NULL, *current = head, *next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

/* Function to check if a linked list is a palindrome */
int is_palindrome(listint_t **head) {
    if (*head == NULL || (*head)->next == NULL) {
        return 1;  /* An empty list or a single-node list is a palindrome */
    }

    listint_t *slow = *head, *fast = *head, *second_half, *prev_of_slow = *head;
    listint_t *mid = NULL;
    int is_palindrome = 1;  /* Assume it's a palindrome by default */

    /* Move 'fast' at twice the speed of 'slow', and find the middle of the linked list */
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;

        prev_of_slow = slow;
        slow = slow->next;
    }

    /* If the linked list has an odd number of elements, skip the middle node */
    if (fast != NULL) {
        mid = slow;
        slow = slow->next;
    }

    /* Reverse the second half of the linked list */
    second_half = reverse_list(slow);

    /* Compare the first half and the reversed second half */
    while (second_half != NULL) {
        if ((*head)->n != second_half->n) {
            is_palindrome = 0;
            break;
        }

        *head = (*head)->next;
        second_half = second_half->next;
    }

    /* Restore the linked list to its original state by reversing the reversed second half */
    second_half = reverse_list(second_half);

    /* If the linked list has an odd number of elements, reconnect the middle node */
    if (mid != NULL) {
        prev_of_slow->next = mid;
        mid->next = second_half;
    } else {
        prev_of_slow->next = second_half;
    }

    return is_palindrome;
}
