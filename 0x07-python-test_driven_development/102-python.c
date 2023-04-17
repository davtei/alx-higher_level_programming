#include <Python.h>
#include <object.h>
#include <unicodeobject.h>

/**
 * print_python_string - A function that prints Python strings.
 *
 * @p: the Python string to print.
*/
void print_python_string(PyObject *p)
{
	const char *type = NULL;
	Py_ssize_t length = 0;
	wchar *string = NULL;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		type = "compact ascii";
	else
		type = "compact unicode object";

	string = PyUnicode_AsWideCharString(p, &length);
	printf(" type: %s\n", type);
	printf(" length: %ld\n", lenght);
	printf(" value: %ls\n", string)
}
