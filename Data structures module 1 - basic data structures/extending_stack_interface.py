def extending_stack_interface(q, operations):
    """
    Correct implementation using auxiliary max stack

    Key insight: Use two stacks:
    1. Main stack for elements
    2. Max stack to track maximum at each level
    """
    stack = []
    max_stack = []  # Keeps track of max at each level
    results = []

    for operation in operations:
        parts = operation.split()

        if parts[0] == 'push':
            value = int(parts[1])
            stack.append(value)

            # Update max_stack: current max is either the new value
            # or the previous max (whichever is larger)
            if not max_stack:
                max_stack.append(value)
            else:
                max_stack.append(max(value, max_stack[-1]))

        elif parts[0] == 'pop':
            if stack:  # Check if stack is not empty
                stack.pop()
                max_stack.pop()  # Remove corresponding max

        elif operation == 'max':
            if max_stack:  # Check if stack is not empty
                results.append(max_stack[-1])

    # Print results
    for result in results:
        print(result)

    return results


if __name__ == '__main__':
    q = int(input())
    operations = []
    for _ in range(q):
        operation = input()
        operations.append(operation)
    extending_stack_interface(q=q, operations=operations)
