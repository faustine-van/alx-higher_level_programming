#!/usr/bin/node
// class Rectangle define rectangle
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return new Rectangle();
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Rectangle;
module.exports = Square;
