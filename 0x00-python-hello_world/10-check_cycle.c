#include "lists.h"
/**
 * check_cycle - Check if a linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * This function determines whether the linked list starting from 'list'
 * contains a cycle (loop) or not.
 *
 * Return: 1 if a cycle is detected, 0 otherwise.
 *
 * Author: AhMeDMaGDY28
 * School: ALX CO 1 BLENDED
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
