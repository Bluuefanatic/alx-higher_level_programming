#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    Py_ssize_t i, size;
    PyObject *item;

    if (!PyList_Check(p)) {
        fprintf(stderr, "  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t i, size;
    char *bytes_data;

    if (!PyBytes_Check(p)) {
        fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_GET_SIZE(p);
    bytes_data = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes_data);

    if (size > 10)
        size = 10;

    printf("  first %ld bytes: ", size);
    for (i = 0; i < size; ++i) {
        printf("%02hhx", bytes_data[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
