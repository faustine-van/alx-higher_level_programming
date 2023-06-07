#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - insert data ain sorted list of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;
	listint_t *current = *head;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	/*if list is empty or the value of node is smaller the value of head*/
	if (*head == NULL || (*head)->n >= newNode->n)
	{
		newNode->next = *head;
		*head = newNode;
	}
	else
	{
		while (current->next != NULL && current->next->n < newNode->n)
			current = current->next;
		newNode->next = current->next;
		current->next = newNode;
	}
	return (newNode);
}
