type A = ReadonlyArray<{
  name: string
}>

const arr2: A = [
  {name: 'aaa'}
]

type B = Array<
  boolean
>

const ar2: B = [
  true, false
]

type C = (number | string | boolean)[]

const ar3: C = [100, 'aaa', true]
ar3.includes(100);