char stack[100000];
int top = -1;

void push(char ch) {
    stack[++top] = ch;
}

char pop() {
    if (top == -1) {
        return '#';
    }
    return stack[top--];
}

int matchpairs(char open, char close) {
    if (open == '(' && close == ')') return 1;
    if (open == '{' && close == '}') return 1;
    if (open == '[' && close == ']') return 1;
    return 0;
}

bool isValid(char* s) {
    top=-1;
    for (int i = 0; s[i] != '\0'; i++) {
        char ch = s[i];
        if (ch == '(' || ch == '{' || ch == '[') {
            push(ch);
        } else if (ch == ')' || ch == '}' || ch == ']') {
            char topstack = pop();
            if (topstack == '#' || !matchpairs(topstack, ch)) {
                return false;
            }
        }
    }
    return top == -1;
}