#include "lists.h"
/**
 * check_length - Count the number of elements in a linked list.
 * @head: A pointer to the head of the linked list.
 *
 * This function counts the number of elements in the linked list starting
 * from 'head'.
 *
 * Return: The number of elements in the linked list.
 *
 * Author: AhMeDMaGDY28
 * School: ALX CO 1 BLENDED
 */
int check_length(listint_t *head)
{
	int i = 0;
	listint_t *curr = head;
	
	if (!head)
		return (0);
	while (curr)
	{
		i++;
		curr = curr->next;
	}
	return (i);
}
/**
 * array_maker - Create an array from a linked list.
 * @head: A pointer to the head of the linked list.
 * @array: An array to store the elements of the linked list.
 *
 * This function creates an array containing the elements of the linked list
 * starting from 'head'.
 *
 * Return: A pointer to the array.
 *
 * Author: AhMeDMaGDY28
 * School: ALX CO 1 BLENDED
 */
int *array_maker(listint_t *head, int *array)
{
	int i = 0;
	listint_t *number_taker = head;

	while (number_taker)
	{
		array[i] = number_taker->n;
		number_taker = number_taker->next;
		i++;
	}
	return (array);
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
	int length_of_array = 0;
	int mover_in_the_array = 0;
	listint_t *sender = *head;
	static int array[100000];

	length_of_array = check_length(sender);
	if (length_of_array == 0)
		return (1);

	array_maker(sender, array);
	while (mover_in_the_array < length_of_array)
	{
		if (array[mover_in_the_array] != array[length_of_array - 1])
		{
			return (0);
		}
		mover_in_the_array++;
		length_of_array--;
	}
	return (1);
}
