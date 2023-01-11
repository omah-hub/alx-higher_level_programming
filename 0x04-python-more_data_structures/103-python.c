#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_bytes - prints info about python lists
 * @p: address of pyobject struct
 */
void print_python_bytes(PyObject *p)
{
	size_t i, len, size;
	char *str;
