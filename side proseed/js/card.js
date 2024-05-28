//css파일 불러오기
function loadCSS(filename) {
  var link = document.createElement('link');
  link.rel = 'stylesheet';
  link.type = 'text/css';
  link.href = filename;
  document.getElementsByTagName('head')[0].appendChild(link);
}

loadCSS('./css/index.css');
loadCSS('./css/menu.css');
loadCSS('./css/scroll.css');

//카드 나타나기
const observer = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in');
      } else {
        entry.target.classList.remove('fade-in');
      }
    });
  },
  { threshold: 0.1 }
);

const targetElements = document.querySelectorAll('.fade-wrap');
targetElements.forEach((element) => {
  observer.observe(element);
});

//카드 뒤집기

// var container = document.querySelector('.container');
// var overlay = document.querySelector('.overlay');
// container.addEventListener('mousemove', function (e) {
//   var x = e.offsetX;
//   var y = e.offsetY;
//   console.log(x, y);
//   var rotateY = (-2 / 11) * x + 30; // updated for width 330
//   var rotateX = (4 / 31) * y - 30; // updated for height 465

//   overlay.style = `background-position : ${
//     x / 5 + y / 5
//   }%; filter : opacity(${x / 200}) brightness(1.2)`;

//   container.style = `transform : perspective(350px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
// });

// container.addEventListener('mouseout', function () {
//   overlay.style = 'filter : opacity(0)';
//   container.style =
//     'transform : perspective(350px) rotateY(0deg) rotateX(0deg)';
// });

document.addEventListener('DOMContentLoaded', () => {
  const containers = document.querySelectorAll('.container');

  containers.forEach((container) => {
    const overlay = container.querySelector('.overlay');

    overlay.style.opacity = '0';

    container.addEventListener('mousemove', function (e) {
      var x = e.offsetX;
      var y = e.offsetY;
      var rotateY = (-2 / 11) * x + 30; // updated for width 330
      var rotateX = (4 / 31) * y - 30; // updated for height 465

      overlay.style = `background-position : ${
        x / 5 + y / 5
      }%; filter : opacity(${x / 200}) brightness(1.2)`;

      container.style = `transform : perspective(350px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });

    container.addEventListener('mouseout', function () {
      overlay.style = 'filter : opacity(0)';
      container.style =
        'transform : perspective(350px) rotateY(0deg) rotateX(0deg)';
    });
  });
});
