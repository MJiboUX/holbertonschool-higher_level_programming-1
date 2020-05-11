#!/usr/bin/node
exports.esrever = function (list) {
  if (list === undefined) {
    return undefined;
  }
  const l = [];
  for (let i = 0; i < list.length; i++) {
    l.unshift(list[i]);
  }
  return l;
};
