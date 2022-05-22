const sum = (...args: number[]): number => {
  let results = 0;
  for (const num of args) {
    results += num;
  }
  return results;
}

console.log(sum(1, 2, 3))