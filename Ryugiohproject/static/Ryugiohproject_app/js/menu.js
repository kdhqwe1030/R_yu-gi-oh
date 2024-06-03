// // 맨 위 메뉴와 중간 메뉴 변수 할당
// const topMenu = document.getElementById('top-menu');
// const middleMenu = document.getElementById('middle-menu');

// // 중간 메뉴바의 위치 계산
// let middleMenuTop = middleMenu.offsetTop;
// let middleMenuHeight = middleMenu.offsetHeight;

// // 스크롤 이벤트 핸들러
// window.addEventListener('scroll', function () {
//   // 스크롤하는 높이를 체크
//   let scrollPosition = window.scrollY;

//   // 스크롤하는 위치가 중간 메뉴보다 클 경우 (중간 메뉴보다 더 아래로 스크롤 할 경우)
//   if (scrollPosition >= middleMenuTop) {
//     // 맨 위 메뉴바의 display 속성을 none으로 변경

//     topMenu.style.display = 'none';

//     // 중간 메뉴바의 position을 맨 위 메뉴바의 속성으로 변경
//     middleMenu.style.position = 'fixed';
//     middleMenu.style.top = '0';
//     // middleMenu.style.left = '0';
//     // middleMenu.style.width = '100%';
//     middleMenu.style.opacity = 1;
//     middleMenu.style.left = '50%';
//     middleMenu.style.width = '90%';
//     middleMenu.style.transform = 'translateX(-50%)';
//     middleMenu.classList.add('fixed');
//     // 중간 메뉴바의 투명도 이벤트 리스너 해제
//     middleMenu.removeEventListener('mouseover', setOpacityToOne);
//     middleMenu.removeEventListener('mouseout', setOpacityToHalf);
//   } else {
//     // 맨 위 메뉴바의 display 속성을 block으로 변경
//     topMenu.style.display = 'block';

//     // 중간 메뉴바를 다시 원래 속성으로 변경
//     middleMenu.style.position = 'static';

//     // 중간 메뉴바의 투명도 이벤트 리스너 등록
//     middleMenu.addEventListener('mouseover', setOpacityToOne);
//     middleMenu.addEventListener('mouseout', setOpacityToHalf);
//   }
// });

// // 투명도 1로 설정
// function setOpacityToOne() {
//   middleMenu.style.opacity = '1';
// }

// // 투명도 0.5로 설정
// function setOpacityToHalf() {
//   middleMenu.style.opacity = '0.5';
// }

// 맨 위 메뉴와 중간 메뉴 변수 할당
const topMenu = document.getElementById('top-menu');
const middleMenu = document.getElementById('middle-menu');

// 중간 메뉴바의 위치 계산
let middleMenuTop = middleMenu.offsetTop;
let middleMenuHeight = middleMenu.offsetHeight;

// 스크롤 이벤트 핸들러
window.addEventListener('scroll', function () {
  // 스크롤하는 높이를 체크
  let scrollPosition = window.scrollY;

  // 스크롤하는 위치가 중간 메뉴보다 클 경우 (중간 메뉴보다 더 아래로 스크롤 할 경우)
  if (scrollPosition >= middleMenuTop ) {
    // 맨 위 메뉴바의 display 속성을 none으로 변경
    topMenu.style.display = 'none';

    // 중간 메뉴바에 fixed 클래스를 추가하여 고정
    // 중간 메뉴바의 투명도 이벤트 리스너 해제
    // middleMenu.removeEventListener('mouseover', setOpacityToOne);
    // middleMenu.removeEventListener('mouseout', setOpacityToHalf);
    middleMenu.classList.add('fixed');

  } else {
    // 맨 위 메뉴바의 display 속성을 block으로 변경
    topMenu.style.display = 'block';

    // 중간 메뉴바의 fixed 클래스를 제거하여 원래 상태로 복원
    middleMenu.classList.remove('fixed');

    // 중간 메뉴바의 투명도 이벤트 리스너 등록
    // middleMenu.addEventListener('mouseover', setOpacityToOne);
    // middleMenu.addEventListener('mouseout', setOpacityToHalf);
  }
});

// 투명도 1로 설정
function setOpacityToOne() {
  middleMenu.style.opacity = '1';
}

// 투명도 0.5로 설정
function setOpacityToHalf() {
  middleMenu.style.opacity = '0.5';
}
