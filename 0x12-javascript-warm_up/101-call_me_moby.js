#!/usr/bin/node
function callMeMoby (x, theFunction) {
  while (x-- > 0) {
    theFunction();
  }
}
module.exports = {
  callMeMoby
};
