#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
  * is_palindrome - check if singly linked list is  palindrome
  * @head: The head of the singly linked list
  * Return: 0 if not a palindrome, and 1 if not a palindrome
  */

int is_palindrome(listint_t **head)

{
    listint_t *start = NULL, *end = NULL;
    unsigned int i = 0, len = 0, len_cyc = 0, len_list = 0;

    if (head == NULL)
        return (0);

    if (*head == NULL)
        return (1);
    
    start = *head;
    len = listint_len(start);
    len_cyc = len * 2;
    len_list = len_cyc - 2;
    end = *head;

    for (; i < len_cyc; i = i + 2)
    {
        if (start[i].n != end[len_list].n)
            return (0);

        len_list = len_list - 2;
    }

    return (1);
}

/**
  * get_nodeint_at_index - get node from linked list
  * @head: head of linked list
  * @index: index to find in linked list
  * Return: specific node of linked list
  */

listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)

{
	listint_t *current = head;
	unsigned int iter_times = 0;

	if (head)
	{
		while (current != NULL)
		{
			if (iter_times == index)
				return (current);

			current = current->next;
			++iter_times;
		}
	}

	return (NULL);
}

/**
  * slistint_len - count number of elements in  linked list
  * @h: linked list to count
  * Return: number of elements in linked list
  */

size_t listint_len(const listint_t *h)

{
	int lenght = 0;

	while (h != NULL)
	{
		++lenght;
		h = h->next;
	}

	return (lenght);
}
