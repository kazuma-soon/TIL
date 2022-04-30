const message = 'こんにちは、webpack！';
const APP_NAME = 'webpackハンズオン';

function hello() {
    console.log(message);
}
class Figure {
  static getTriangle(base, height) {
    return base * height / 2;
  }
}

module.exports = {
  message,
  APP_NAME,
  hello,
  Figure
};

