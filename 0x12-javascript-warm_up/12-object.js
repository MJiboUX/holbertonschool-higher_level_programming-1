#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

Reflect.set(myObject, 'value', 98);

console.log(myObject);
