const openModalButtons = document.querySelectorAll('.open-modal'),
      modal = document.querySelectorAll('.modal'),
      closeModalButtons = document.querySelectorAll('.close-modal');
      CLICKED_CLASS = "clicked"

openModalButtons.forEach((openBtn,idx) => {
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


