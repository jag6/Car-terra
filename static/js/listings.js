//LISTINGS PAGINATION
const pagNums = document.getElementById('pag-nums');
const pagList = document.getElementById('listings-total');
const listings = pagList.querySelectorAll('.listing');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');

const pagLimit = 6;
const pagCount = Math.ceil(listings.length/pagLimit);
let currentPag = 1;

const appendPagNum = (index) => {
    const pagNum = document.createElement('button');
    pagNum.className = 'pag-num';
    pagNum.innerHTML = index;
    pagNum.setAttribute('pag-index', index);
    pagNum.setAttribute('aria-label', 'Page ' + index);
    
    pagNums.appendChild(pagNum);
};

const getPagNums = () => {
    for (let i = 1; i <= pagCount; i++) {
        appendPagNum(i);
    }
};

const handleActivePagNum = () => {
    document.querySelectorAll('.pag-num').forEach((btn) => {
        btn.classList.remove('active');

        const pagIndex = Number(btn.getAttribute('pag-index'));
        if(pagIndex == currentPag) {
            btn.classList.add('active');
        }
    });
};

const disableBtn = (btn) => {
    btn.classList.add('disabled');
    btn.setAttribute('disabled', true);
};

const enableBtn = (btn) => {
    btn.classList.remove('disabled');
    btn.removeAttribute('disabled');
};

const handlePagBtnsStatus = () => {
    if(currentPag === 1) {
        disableBtn(prevBtn);
    }else {
        enableBtn(prevBtn);
    }

    if(pagCount === currentPag) {
        disableBtn(nextBtn);
    }else {
        enableBtn(nextBtn);
    }
};

const setCurrentPag = (pagNum) => {
    currentPag = pagNum;

    handleActivePagNum();
    handlePagBtnsStatus();

    const prevRange = (pagNum - 1) * pagLimit;
    const currRange = pagNum * pagLimit;

    listings.forEach((item, index) => {
        item.classList.add('hidden');
        if(index >= prevRange && index < currRange) {
            item.classList.remove('hidden');
        }
    });
};

window.addEventListener('load', () => {
    getPagNums();
    setCurrentPag(1);

    prevBtn.addEventListener('click', () => {
        setCurrentPag(currentPag - 1);
        window.location.href = '#all-listings';
    });

    nextBtn.addEventListener('click', () => {
        setCurrentPag(currentPag + 1);
        window.location.href = '#all-listings';
    });

    document.querySelectorAll('.pag-num').forEach((btn) => {
        btn.addEventListener('click', () => {
            window.location.href = '#all-listings';
        });

        const pagIndex = Number(btn.getAttribute('pag-index'));

        if(pagIndex) {
            btn.addEventListener('click', () => {
                setCurrentPag(pagIndex);
            });
        }
    });
});