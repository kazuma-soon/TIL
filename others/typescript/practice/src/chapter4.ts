const map = (array: number[], callback: (value: number) => number) => {
  const newArray: number[] = [];
  for (const i of array) {
    const newVal = callback(i);
    newArray.push(newVal);
  }
  return newArray;
}

const a: number[] = [1, 2, 3, 4, 5];

console.log(map(a, (x) => x * 10));

