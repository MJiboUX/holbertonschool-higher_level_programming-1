#!/usr/bin/node

module.exports = {
  addMeMaybe: function (n, func) {
    const nb = n;
    func(nb + 1);
  }
};
