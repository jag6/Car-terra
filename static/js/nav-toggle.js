const mobile_nav = document.getElementById('mobile-nav');
const nav_overlay = document.getElementById('nav-overlay');
const body = document.querySelector('body');

const clickOff = () => {
    nav_overlay.style.display = 'none';
    mobile_nav.style.width = '0%';
    body.style.overflow = 'auto';
};

document.getElementById('hamburger-icon').addEventListener('click', () => {
    if(mobile_nav.style.width === '80%') {
        clickOff();
    }else {
        mobile_nav.style.width = '80%';
        nav_overlay.style.display = 'flex';
        body.style.overflow = 'hidden';
    }
});

nav_overlay.addEventListener('click', (e) => {
    if(e.target == nav_overlay) {
        clickOff();
    }
});
