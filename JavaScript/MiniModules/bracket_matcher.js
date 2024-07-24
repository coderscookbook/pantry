/* 
key is to use a stack data structure
- if "(", append to stack
- if ")", pop "(" from stack
- must end up with empty stack
- Two Cases that fail:
  1. ())hi
  2. (((hi))
- Complexity: O of N time and space (optimal solution)
*/

function BracketMatcher(str) {
  const stack = [];

  for (let i = 0; i < str.length; i++) {
    if (str[i] === '(') {
      stack.push('(');
    } 
    else if (str[i] === ')') {
      if (stack.length === 0) {
        return 0;
      } else {
        stack.pop();
      }
    }
  }

  return stack.length === 0 ? 1 : 0;

}

// function call
console.log(BracketMatcher(readline()));
