//스크롤 표시 클릭시에 아래 페이지로 이동
document
  .getElementById('scroll-link_icon')
  .addEventListener('click', function (event) {
    event.preventDefault();
    document.querySelector('.base_div').scrollIntoView({
      behavior: 'smooth',
    });
  });
document
  .getElementById('scroll-link_text')
  .addEventListener('click', function (event) {
    event.preventDefault();
    document.querySelector('.base_div').scrollIntoView({
      behavior: 'smooth',
    });
  });
