#include <stddef.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the head of the linked list.
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * find_middle - Finds the middle of a linked list.
 * @head: Pointer to the head of the linked list.
 * Return: Pointer to the middle of the list.
 */
listint_t *find_middle(listint_t *head)
{
	listint_t *slow = head, *fast = head;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	return (slow);
}

/**
 * compare_lists - Compares two linked lists.
 * @list1: Pointer to the first linked list.
 * @list2: Pointer to the second linked list.
 * Return: 1 if lists are equal, 0 otherwise.
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);

		list1 = list1->next;
		list2 = list2->next;
	}

	return (1);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1); /* An empty list or a single-node list is a palindrome */

	listint_t *mid = find_middle(*head);
	listint_t *second_half = reverse_list(mid->next);

	int is_palindrome = compare_lists(*head, second_half);

	second_half = reverse_list(second_half);
	mid->next = second_half;

	return (is_palindrome);
}
