const openModalButtons = document.querySelectorAll('.open-modal'),
      modal = document.querySelectorAll('.modal'),
      closeModalButtons = document.querySelectorAll('.close-modal');


openModalButtons.forEach(openBtn => {
   openBtn.addEventListener('click', openModal)
});

closeModalButtons.forEach(closeBtn => {
  closeBtn.addEventListener('click', closeModal)
});

function openModal(e) {
  e.target.parentElement.querySelector('.modal').classList.add('visible');
}

function closeModal(e) {

  e.target.parentElement.parentElement.parentElement.classList.remove('visible');

}


