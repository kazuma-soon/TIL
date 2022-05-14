type User<T> = {
  name: string;
  age: T;
}

const obj3_4: User<number> = {
  name: 'aa',
  age: 12,
}

type HasName = {
  name: string;
}

type Family<Parent extends HasName, Child extends HasName> = {
  mother: Parent;
  father: Parent;
  child: Child;
}

type Parent = {
  name: string;
  gender: string;
}

