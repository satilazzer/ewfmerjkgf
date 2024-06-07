let header = document.querySelector('#header');
let header_navbar = document.querySelector('.navbar')
let bottom_header = document.querySelector('.bottom_header');
let burger = document.querySelector('.header_burger');
let book = document.querySelector('.booking a');
let calendar = document.querySelector('.calendar');
let date_days = document.querySelectorAll('.date_day');
let timings = document.querySelector('#timings');
let close = document.querySelector('.calendar .close');
form_ = document.querySelector('#timings .form');
select_form = document.querySelector('.select_form');
book_btn = document.querySelector('.book_btn');

burger.addEventListener('click', function(){
    bottom_header.classList.toggle('bottom_header_burger');
    header_navbar.classList.toggle('nav_list_burger');
});

const week_days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
const months = {'January': 1 , 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

book.addEventListener('click', function(){
    calendar.classList.add('visible');
});



for (let date_day of date_days){
    date_day.addEventListener('click', function(){
        timings.classList.add('visible');
    });
}



close.addEventListener('click', function(){
    calendar.classList.remove('visible');
    timings.classList.remove('visible');
});
