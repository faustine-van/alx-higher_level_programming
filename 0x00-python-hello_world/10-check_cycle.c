#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - detect and check loop or cycle in lists
 *@list: pointer to the Head list
 * Return: Always 0 if there is no cycle or 1 if there is cyle.
 */
int check_cycle(listint_t *list)
{
	listint_t *new_head, *newHead = list;
	new_head = list;

	while(newHead && new_head)
	{
		new_head = new_head->next;
		newHead = newHead->next->next;
		if (new_head == newHead)
			return (1);
	}
	return (0);
}
