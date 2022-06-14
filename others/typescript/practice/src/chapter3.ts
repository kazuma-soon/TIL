type User = {
  name: string;
  age: number;
  premiumUser: boolean;
}

const users: User[] = [];

const data: string = `
uhyo, 26, 1
Joun Smith, 17, 0
Mary Sue, 14, 1
`;

const lines = data.split('\n')
lines.shift()
lines.pop()

for (const line of lines) {
  const [name, ageString, premiumUserString] = line.split(',');
  const age = Number(ageString)
  const premiumUser = Boolean(Number(premiumUserString));
  users.push({
    name: name,
    age: age,
    premiumUser: premiumUser,
  });
}

for (const user of users) {
  if (user.premiumUser) {
    console.log(`${user.name} (${user.age})はプレミアムユーザーです。`);
  }
  else {
    console.log(`${user.name} (${user.age})はプレミアムユーザーではありません。`); 
  }
}