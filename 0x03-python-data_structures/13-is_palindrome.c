#include "lists.h"

/**
 * reverse_listint - Reverse a linked list.
 * @head: A pointer to the head of the linked list.
 *
 * This function reverses the linked list starting from 'head'.
 *
 * Return: A pointer to the new head of the reversed linked list.
 *
 * Author: AhMeDMaGDY28
 * School: ALX CO 1 BLENDED
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
    return *head;
}
/**
 * is_palindrome - Check if a linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * This function determines whether the linked list starting from 'head'
 * is a palindrome or not.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 *
 * Author: AhMeDMaGDY28
 * School: ALX CO 1 BLENDED
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *mid, *second_half;

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    second_half = reverse_listint(&slow);
    mid = second_half;

    while (*head != NULL && second_half != NULL)
    {
        if ((*head)->n != second_half->n)
            return 0;

        *head = (*head)->next;
        second_half = second_half->next;
    }
    reverse_listint(&mid);

    return 1;
}

