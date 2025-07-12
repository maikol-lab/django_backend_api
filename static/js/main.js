const btn = document.querySelector('#menu-btn');
const menu = document.querySelector('#sidebar');
const btnCollapse = document.querySelector('#btn-collapse');
const menuNav = document.querySelector('#menu-nav');

const itemIcon1 = document.querySelector('#item-icon-1')
const itemIcon2 = document.querySelector('#item-icon-2')
const itemIcon3 = document.querySelector('#item-icon-3')
const itemIcon4 = document.querySelector('#item-icon-4')
const itemIcon5 = document.querySelector('#item-icon-5')
/* const itemIcon6 = document.querySelector('#item-icon-6') */

const itemTitle1 = document.querySelector('#item-title-1')
const itemTitle2 = document.querySelector('#item-title-2')
const itemTitle3 = document.querySelector('#item-title-3')
const itemTitle4 = document.querySelector('#item-title-4')
const itemTitle5 = document.querySelector('#item-title-5')
/* const itemTitle6 = document.querySelector('#item-title-6') */

btn.addEventListener('click', () => {
    menu.classList.toggle('menu-expanded');
    menu.classList.toggle('menu-collapsed');

    itemIcon1.classList.toggle('hint--right');
    itemIcon2.classList.toggle('hint--right');
    itemIcon3.classList.toggle('hint--right');
    itemIcon4.classList.toggle('hint--right');
    itemIcon5.classList.toggle('hint--right');
    /* itemIcon6.classList.toggle('hint--right'); */
    
    itemIcon1.classList.toggle('posicion-item-icon');
    itemIcon2.classList.toggle('posicion-item-icon');
    itemIcon3.classList.toggle('posicion-item-icon');
    itemIcon4.classList.toggle('posicion-item-icon');
    itemIcon5.classList.toggle('posicion-item-icon');
    /* itemIcon6.classList.toggle('posicion-item-icon'); */

    itemTitle1.classList.toggle('item-title');
    itemTitle2.classList.toggle('item-title');
    itemTitle3.classList.toggle('item-title');
    itemTitle4.classList.toggle('item-title');
    itemTitle5.classList.toggle('item-title');
    /* itemTitle6.classList.toggle('item-title'); */

    document.querySelector('body').classList.toggle('body-collapsed');
    document.querySelector('body').classList.toggle('body-expanded');
});

btnCollapse.addEventListener('click', () => {
    menuNav.classList.toggle('menu-nav-expanded');
    menuNav.classList.toggle('menu-nav-collapsed');
});