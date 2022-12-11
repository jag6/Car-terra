//BACK TO LISTIGNS  
document.getElementById('close-btn').addEventListener('click', () => {
    window.open('','_self').close();
}); 

//LISTINGS MODAL
const photoModal = document.getElementById('listing-photos-modal');

//open modal
if(!document.querySelector('.listing-photos-other')) {
    console.log('no other photos');
}else {
    const listingPhotos = document.getElementsByClassName('listing-photos-other');
    for (let i = 0; i < listingPhotos.length; i++) {
        listingPhotos[i].addEventListener('click', () => {
            photoModal.style.display = 'flex';
            document.querySelector('body').style.overflow = 'hidden';
        });
    }
}

//close modal
document.getElementById('close-modal').addEventListener('click', () => {
    photoModal.style.display = 'none';
    document.querySelector('body').style.overflow = 'auto';
});

//cycle through modal
if(!document.querySelector('.modal-slide')) {
    console.log('no slides');
}else {
    const showSlides = (n) => {
        let i;
        let slides = document.getElementsByClassName('modal-slide');
        if(n > slides.length) { slideIndex = 1 }
        if(n < 1) { slideIndex = slides.length }
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = 'none';
        } 
        slides[slideIndex - 1].style.display = 'flex';
    };
    
    let slideIndex = 1;
    showSlides(slideIndex);
    
    document.getElementById('next-modal').addEventListener('click', (n) => {
        n = 1;
        showSlides(slideIndex += n);
    });
    document.getElementById('prev-modal').addEventListener('click', (n) => {
        n =-1;
        showSlides(slideIndex += n)
    });
}

//INQUIRY MODAL
const inquiryModal = document.getElementById('inquiry-modal');

//open inquiry
document.getElementById('make-inquiry').addEventListener('click', () => {
    inquiryModal.style.display = 'flex';
    document.querySelector('body').style.overflow = 'hidden';
});

//close inquiry
const clickOffInquiry = () => {
    inquiryModal.style.display = 'none';
    document.querySelector('body').style.overflow = 'auto';
};

document.getElementById('close-inquiry-modal').addEventListener('click', () => {
    clickOffInquiry();
});
inquiryModal.addEventListener('click', (e) => {
    if(e.target == inquiryModal) {
        clickOffInquiry();
    }
});