#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    size = Py_SIZE(p);
    for (i = 0; i < size; i++) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *bytes_str;

    printf("[.] Python bytes info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("  Size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    bytes_str = PyBytes_AsString(p);
    printf("  first %ld bytes: ", size + 1 > 10 ? 10 : size + 1);
    for (i = 0; i < size + 1 && i < 10; i++) {
        printf("%02hhx", bytes_str[i]);
        if (i + 1 < size + 1 && i + 1 < 10) {
            printf(" ");
        }
    }
    printf("\n");
}
